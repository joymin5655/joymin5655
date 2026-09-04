#!/usr/bin/env python3
"""Generate assets/terminal-banner.svg · a declarative SMIL "typing" terminal.

No JS, no CSS classes (GitHub strips both from README-embedded SVG); typing is a
per-line clipPath whose width steps one glyph at a time. Edit LINES, run, commit.
"""
from pathlib import Path

W, H = 880, 300
CH = 8.4            # px per glyph at 14px ui-monospace
LH = 26
X0, Y0 = 28, 78
LINES = [
    ("cmd", "$ whoami"),
    ("out", "Yongmin Cho · AI Agent & Infrastructure Engineer · ships AI to production, solo, governed"),
    ("cmd", "$ airlens status --window 30d"),
    ("out", "LIVE  airlens.cloud   66,307 requests · 55 countries · 10 sources · 5 ML engines · GPT-4o agent"),
    ("cmd", "$ agent enforce --stats"),
    ("out", "3 runtimes · 17 hooks · 296 high-risk ops blocked · 0 false positives · blind benchmark 8/8"),
    ("cmd", "$ cat research.md | head -1"),
    ("out", "What I don't measure, I don't claim.  →  joymin5655.github.io/research"),
]
CPS_CMD, CPS_OUT, GAP = 0.028, 0.006, 0.35
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

t = 0.6
defs, parts, cursor = [], [], []
for i, (kind, text) in enumerate(LINES):
    y = Y0 + i * LH
    n = len(text)
    dur = n * (CPS_CMD if kind == "cmd" else CPS_OUT)
    keys = ";".join(f"{k/n:.4f}" for k in range(n + 1))
    vals = ";".join(f"{k*CH+4:.1f}" for k in range(n + 1))
    defs.append(
        f'<clipPath id="c{i}"><rect x="{X0-2}" y="{y-16}" height="{LH}" width="0">'
        f'<animate attributeName="width" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze" calcMode="discrete" keyTimes="{keys}" values="{vals}"/>'
        f'</rect></clipPath>'
    )
    fill = "#e6edf3" if kind == "cmd" else "#8b949e"
    body = f'<tspan fill="#d7ff3f">$</tspan>{esc(text[1:])}' if kind == "cmd" else esc(text)
    parts.append(f'<text x="{X0}" y="{y}" fill="{fill}" clip-path="url(#c{i})" xml:space="preserve">{body}</text>')
    xs = ";".join(f"{X0 + k*CH:.1f}" for k in range(n + 1))
    cursor.append(f'<set attributeName="y" to="{y-13}" begin="{t:.2f}s"/>')
    cursor.append(f'<animate attributeName="x" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze" calcMode="discrete" values="{xs}"/>')
    t += dur + GAP

yf = Y0 + len(LINES) * LH
cursor.append(f'<set attributeName="y" to="{yf-13}" begin="{t:.2f}s"/>')
cursor.append(f'<set attributeName="x" to="{X0 + CH*2:.1f}" begin="{t:.2f}s"/>')
cursor.append(f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" begin="{t:.2f}s" repeatCount="indefinite"/>')
final_prompt = f'<text x="{X0}" y="{yf}" fill="#e6edf3" opacity="0" xml:space="preserve"><tspan fill="#d7ff3f">$</tspan> <set attributeName="opacity" to="1" begin="{t:.2f}s"/></text>'

label = " ".join(l for _, l in LINES)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)}">
  <title>joymin5655 · terminal</title>
  <defs>{"".join(defs)}</defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="#0a0c10" stroke="#232936"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="38" rx="10" fill="#12151c"/>
  <rect x="0.5" y="20" width="{W-1}" height="19" fill="#12151c"/>
  <line x1="0.5" y1="38.5" x2="{W-0.5}" y2="38.5" stroke="#232936"/>
  <circle cx="20" cy="19.5" r="5.5" fill="#ff5f57"/><circle cx="38" cy="19.5" r="5.5" fill="#febc2e"/><circle cx="56" cy="19.5" r="5.5" fill="#28c840"/>
  <text x="{W/2}" y="24" text-anchor="middle" fill="#7e8798" font-family="{MONO}" font-size="11" letter-spacing="0.12em">joymin5655 · zsh · 110×24</text>
  <g font-family="{MONO}" font-size="14">
    {"".join(parts)}
    {final_prompt}
    <rect x="{X0}" y="{Y0-13}" width="{CH:.1f}" height="17" fill="#d7ff3f" opacity="0.9">{"".join(cursor)}</rect>
  </g>
</svg>
'''
out = Path(__file__).resolve().parent.parent / "assets" / "terminal-banner.svg"
out.write_text(svg, encoding="utf-8")
print(f"wrote {out} ({len(svg)} bytes, animation ends at {t:.1f}s)")
