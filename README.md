<!--
  joymin5655 · profile README — plain-text terminal edition (2026-09-03)
  · No emoji, no badges. One animated SVG at the top (assets/terminal-banner.svg —
    SMIL typing, regenerate with scripts/gen-banner.py); everything else is a fenced
    code block so it renders identically in light/dark mode and in any client.
  · Every number below is measured and traceable (SSOT: 취업/master/session_summary_report.md).
    Traffic = requests, never users. No commit counts on screen.
  · Lines that contain Korean have no right-hand border — CJK glyph width is
    not stable across monospace fonts, so boxes are left-anchored only.
-->

<p align="center">
  <img src="https://raw.githubusercontent.com/joymin5655/joymin5655/main/assets/terminal-banner.svg" width="880" alt="Terminal: whoami — Yongmin Cho, AI Agent · Infrastructure Engineer. airlens status: 66,307 requests, 55 countries, 10 sources, 5 ML engines. agent enforce: 3 runtimes, 17 hooks, 296 blocked, 0 false positives, blind benchmark 8/8. What I don't measure, I don't claim." />
</p>

```text
██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗██╗███╗   ██╗        ██████╗██╗  ██╗ ██████╗
╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝ ████╗ ████║██║████╗  ██║       ██╔════╝██║  ██║██╔═══██╗
 ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗██╔████╔██║██║██╔██╗ ██║       ██║     ███████║██║   ██║
  ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║       ██║     ██╔══██║██║   ██║
   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║       ╚██████╗██║  ██║╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝        ╚═════╝╚═╝  ╚═╝ ╚═════╝

  AI Agent · Infrastructure Engineer                 ships AI to production — solo, governed
  ─────────────────────────────────────────────────────────────────────────────────────────
  LIVE  https://airlens.cloud        PORTFOLIO  https://joymin5655.github.io        KR / EN
```

```text
$ whoami
```

```text
조용민 (Yongmin Cho) — AI를 프로덕션까지 도달시키는 엔지니어.

기능 하나가 아니라 "일하는 방식 전체"를 시스템으로 설계합니다.
AI 에이전트 팀을 지휘해 혼자서 기획 → 모델 → 인프라 → 배포 → 운영까지 가고,
그 결과(배포·운영·거버넌스)를 책임집니다.

  · 방향 · 검증 · 운영 ................ 사람 (저)
  · 코드 작성의 대부분 ................ AI 에이전트 (Claude Code 등)
  · 모든 머지와 보안 게이트 ........... 사람의 결정 — 기계 게이트(gitleaks · 정책 훅) 통과 후

  "Context is the weapon · Defense-in-depth · Distill, don't copy."
```

```text
$ airlens status --window 30d
```

```text
┌─ airlens.cloud ──────────────────────────────────────────────────────────────┐
│  STATUS        LIVE · single-operator · AI-agent-built                       │
│  REQUESTS      66,307  / 30 days   (requests — not users)                    │
│  COUNTRIES     55                                                            │
│  DATA SOURCES  10      MAIAC · FIRMS · Sentinel-5P · AERONET · ERA5 · CAMS   │
│                        AirKorea · Open-Meteo · EDGAR · WorldBank             │
│  ML ENGINES    5       DQSS · AOD-XGBoost · SDID · DINOv2-ONNX · TFT         │
│  AGENT         GPT-4o AnalysisEngine — natural language → pandas/plotly      │
│  DATABASE      Supabase Postgres · 121 migrations · RLS · pgvector RAG       │
│  EDGE          35 Edge Functions · 41 GitHub Actions pipelines               │
│  OBSERVABILITY Sentry · PostHog · Prometheus                                 │
└──────────────────────────────────────────────────────────────────────────────┘

  SDID causal inference   estimable countries      6 ──▶ 53
  RLS lint cleanup        multiple_permissive     132 ──▶ 6    (no access change)
  RAG quality (RAGAS)     faithfulness           0.958   answer relevancy 0.938
  Sky segmentation        mIoU                   91.5%   boundary F1 87.6%
  Camera PM2.5 (ordinal)  exact 57.9%  ·  within-one-band 92.9%
```

```text
$ agent enforce --stats
```

```text
┌─ github.com/joymin5655/Agent ────────────────────────── MIT · Claude Code plugin ─┐
│  RUNTIMES        3     Claude Code · Codex · Gemini  — one YAML policy            │
│  HOOKS          17     portable, vendor-neutral                                   │
│  BLOCKED       296     high-risk ops denied in production repos                   │
│  FALSE POS       0                                                                │
│  BLIND BENCH   8/8     seeded bugs caught                                         │
│  SECRETS         0     gitleaks full-history scan · pre-commit · pre-push · CI    │
└───────────────────────────────────────────────────────────────────────────────────┘

  plan-approved edit ............................................ PASS
  read-only reviewer ............................................ PASS
  git reset --hard .............................................. DENIED
  secret file read .............................................. DENIED
```

```text
$ ls -la ~/projects
```

```text
projects/
├── AirLens/          대기질 인텔리전스 SaaS · LIVE · 1인 책임·운영
│   ├── data/         위성·지상·기상 10개 소스 융합 파이프라인
│   ├── ml/           GTWR-XGBoost · PINN · SDID · TFT · DINOv2→ONNX · quantile
│   ├── agent/        GPT-4o AnalysisEngine · pgvector hybrid RAG (BM25+vector+RRF)
│   ├── web/          React 19 · Vite · Three.js 3D globe · KO/EN
│   └── infra/        FastAPI · Supabase · Docker · GitHub Actions · Cloudflare Pages
│                     → https://airlens.cloud   ·   github.com/joymin5655/AirLens
│
├── Agent/            멀티런타임 거버넌스 하네스 · Policy-as-Code · MIT OSS
│                     → github.com/joymin5655/Agent
│
├── posture-guard/    바른자세 지킴이 — KT AIVLE 빅프로젝트 · 6인 팀 · FE ~80% 주도
│                     2026: 서버 없이 브라우저 ONNX로 재점화 · 원본 대비 오차 0.000005
│                     → Collaboration상 (KT × 고용노동부) · joymin5655.github.io/projects/posture
│
├── pitter-petter/    반려견 WGS 파이프라인 — 단독 · 계산/추론 플레인 분리 · 사전등록 측정
│                     8/8 라이프사이클 실측 · Jaccard 0.3677 · FAIL도 그대로 보고
│                     → joymin5655.github.io/projects/pitter
│
├── second-brain/     타입드 지식 그래프 268노드 · 890 edge · lint 0 · 3D 뉴런 뷰 4,985노드
│                     → joymin5655.github.io/projects/brain
│
└── craft/            FABLE 65p 디자인 쇼케이스 · ALL-IN-ONE IA 재설계 · Wardenkit
                      → fable-collection.netlify.app · joymin5655.github.io/projects/craft
```

```text
$ cat field-notes.txt        # 실측으로 배운 것
```

```text
01  통과 지표를 잘못 고르면 불량이 그대로 통과한다
    LLM 조언 생성물 게이트 — 금지어 0% · 페르소나 일관성 100% · 파싱 실패 0% 전부 PASS.
    "가이드라인 충실도"를 LLM judge로 추가하자 65.6% → 전체 판정 FAIL로 뒤집혔다.

02  총계는 위험 구간을 가린다
    PM2.5 예측구간 커버리지(PICP@80) 전체 93% — 고농도(≥150) 구간에선 14%.
    관측소 단위 leave-station-out 교차검증으로 구간별 실측을 파일에 남겼다.

03  개선이 없었던 실험도 기록한다
    RAG 리랭커 on/off A/B — answer relevancy −0.0014. "효과 없음"을 그대로 커밋.

04  측정 도구부터 검증한다
    WebGL 캔버스 캡처 경로 3개가 전부 낡은 픽셀을 돌려줘 오진 3회.
    측정을 고치자 실제 결함 2개가 드러났다. "구성으로 검증됨"은 검증이 아니다.
```

```text
$ history --experience
```

```text
2026.03 ─ now   AirLens 제품 개발 · Agent 하네스              1인 책임 · AI 에이전트 협업
                캡스톤 대기질 연구를 상용 SaaS로 고도화. GPT-4o 에이전트 탑재,
                30일 55개국 66,307 요청(사용자 아님) 처리. 거버넌스 하네스 병행 운영.

2025           Sigma · Welodata (Google 협력사)               AI 데이터 QA · 평가 (~8개월)
                한영 오디오 전사·언어 QA (SOW 7건) · 광고·검색 적합성 평가 Tier 1·2.
                평가 기준 V5→V6 개정 대응 — 인간-AI 피드백 루프의 "기준" 쪽 경험.

2024.07 ─ 25.01 에듀인소프트                                  교육 운영 · 기획
                SQLD·ADsP 자격증 과정 운영·담당(대학생 ~30명), 진도·정산 행정, 과정 제안 보조.

2023.08 ─ 24.01 KT AIVLE School · AI 개발자 트랙 (840h)       빅프로젝트 Collaboration상
                프론트엔드 ~80% 주도. 마지막 배포 단계에서 실패 —
                "아무리 좋은 모델도 배포되지 않으면 의미가 없다" → 인프라·CI/CD로 방향 전환.

2023.01 ─ 05   로지체인                                       기획 인턴
                온디바이스 AI·비전 분석 솔루션 신규 사업 제안서 5건. 구조·시각 개선 제안이
                채택되어 제안 통과에 기여. 기획만으로는 닿지 못하는 "구현"의 벽을 느낀 시점.

2018.03 ─ 12   자율주행 인지 데이터 구축                         GT 바운딩박스 라벨링 (~10개월)
                보행자·차량·도로시설물 클래스 · 발주처 입력 기준 준수 · 차수별 납품·검수.

────────────────────────────────────────────────────────────────────────────────
EDU   강릉원주대학교 — 산업경영공학 (주전공) · 헬스케어 데이터사이언스 (융합전공)
      졸업논문 「미세먼지 저감 정책의 효과 분석: 중국과 한국의 비교 분석」
AWARD KT AIVLE 빅프로젝트 Collaboration상 · 정밀의료 메이커톤 사업단장상 (강원지역혁신플랫폼)
      미래내일 일경험 최우수상
CERT  Microsoft Azure AI Fundamentals (AI-900) · 6시그마 GB
```

```text
$ cat stack.txt
```

```text
LANG      Python · TypeScript · SQL
AI/AGENT  OpenAI GPT-4o · Anthropic Claude · Model Context Protocol · LangChain · RAG
ML        PyTorch · scikit-learn · XGBoost · ONNX · GTWR · PINN · SDID · TFT
BACKEND   FastAPI · Supabase (Postgres · RLS · pgvector · Edge Functions) · Redis · Docker
INFRA     GitHub Actions · Cloudflare Pages · Sentry · PostHog · Prometheus · gitleaks
FRONTEND  React 19 · Vite · Three.js · Astro
```

```text
$ cat README.en
```

```text
Yongmin Cho — AI Agent / Infrastructure Engineer. I ship AI to production, solo, with governance.

I design how the work happens, not just one feature. I direct a team of AI agents from
plan to model to infra to deploy to ops, and I own the outcome.

  AirLens   live air-quality SaaS — 66,307 requests across 55 countries in 30 days
            (requests, not users). 10 data sources, 5 ML engines, GPT-4o analysis agent,
            121 DB migrations, 35 edge functions. Built with AI agents, operated by one person.
  Agent     multi-runtime governance harness (Claude Code · Codex · Gemini, one YAML policy).
            296 high-risk ops blocked, 0 false positives, 8/8 blind benchmark. MIT.

  Most code in these repos was written by AI agents. Problem definition, architecture,
  verification design, every merge decision and production operations are mine.
```

```text
$ contact --open
```

```text
EMAIL      joymin5655@gmail.com
GITHUB     https://github.com/joymin5655
PORTFOLIO  https://joymin5655.github.io        (6 case studies · KO/EN)
RESEARCH   https://joymin5655.github.io/research   (interests · methods · thesis)
LIVE       https://airlens.cloud

$ _
```
