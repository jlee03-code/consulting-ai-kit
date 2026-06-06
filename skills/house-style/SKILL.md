---
name: house-style
description: |
  BCG-register Korean slide-authoring engine. Enforces assertion-first, number-anchored
  headlines and 6 canonical BCG slide structures on every deliverable.
  Use when asked to write a slide, format an analysis, structure a finding, or produce
  any consulting output. All other kit skills route output through this skill.
  Trigger phrases: "format this", "structure this as a slide", "write this BCG-style",
  "apply house style", or implicitly whenever producing a consulting deliverable.
allowed-tools: "Read,Write,Edit"
version: "1.0.0"
---

# House Style — BCG Korean Register

모든 출력은 한국어 컨설턴트 어투 (BCG 레지스터)로 작성한다.
단정형 / 숫자 선행 / 실행 지향.

다음 영문 약어는 절대 번역하지 않고 한국어 문장에 그대로 혼용한다:
CAGR, TAM, SAM, SOM, JV, KSF, O&M, M&A, KOL, SKU, EPC, WACC, FCF, EBITDA,
NOPAT, EV, P&L, B2C, B2B, NRC, EPU, R&R, SA

---

## Output Contract (every deliverable must contain all 5)

### 1. Headline
2줄 이내. 아래 5개 공식 중 정확히 1개 사용. 결론과 숫자를 반드시 함께 포함.

Formula 1: [주제] | [결론 + 숫자]
  e.g. "O&M | 시장 규모 ~$650M, <CLIENT> 총 매출의 ~50% 차지"

Formula 2: 기존 [전략]은 유효하나, [항목] 고도화 必
  e.g. "기존 온라인 전략은 유효하나, 오프라인 병행 확장 고도화 必"

Formula 3: <CLIENT> [사업]은 X% 성장했으나 목표와 Gap 존재
  e.g. "<CLIENT> 중국 사업은 연평균 18% 성장했으나 '27년 목표와 큰 Gap 존재"

Formula 4: 온라인 [장점]하나 한계 → 온/오프라인 동시 공략 필수
  e.g. "온라인 채널은 신속 성장 유리하나 지속 성장 한계 → 동시 공략 필수"

Formula 5: [Step N] [action]을 통해, [N]개 [result] 도출
  e.g. "[Step 2] 정량 평가를 통해, 3개 최우선 파트너 도출"

### 2. Body Structure
아래 6개 구조 중 정확히 1개 선택.

assertion+columns
  결론 + 2-4개 컬럼 (각 컬럼: 헤더 + 3-5개 불렛)

tam-sam-waterfall
  TAM → SAM → SOM 단계별 Q x P 산출. [참고] 방법론 블록 포함

scoring-matrix
  후보/옵션(열) x KSF 기준(행), H/M/L 평가. 하단 종합 판정

screening-funnel
  Step 1(Long-list) → Step 2(스코어링) → Step 3(심층검증)

gap-to-target
  실적 바차트 + CAGR → 목표 점선 화살표 + 장벽 callout 2-3개

issue-stack
  컬럼당 3단: 이슈 사항 / 발생 원인 / 시사점

### 3. BCG 의견 Callout
근거(evidence)와 의견을 반드시 분리. 의견 형식:

  [BCG 의견]
  핵심 시사점 1-3줄. 근거와 구분된 editorial 판단.

### 4. Source Footer
  Source: [출처1], [출처2], BCG analysis
  - "analysis" 는 반드시 소문자
  - 출처 불명확 시: "출처 불명확 — 추가 검증 필요"

### 5. Units
모든 수치: 억/조 단위와 USD M/B 를 병기.
예: ~$650M (약 9,000억 원), 3조 원 ($2.2B)

---

## Bullet Rhythm

- 최상위 불렛: bold assertion, 대시 없음, -함 / -적임 / -필요 로 마무리
- 2레벨: → 로 원인/결과 또는 조건/권고 연결
- 괄호 caveat 인라인: (전국 영업력 요구), (BCG 추정)
- 숫자는 불렛 내 인라인 — 차트 축에만 두지 않는다

## Anti-Patterns (금지)

- 숫자 없는 헤드라인
- 영문 약어 한국어 직역 (CAGR → "연평균 성장률" 금지)
- 근거와 의견 혼재 (BCG 의견 callout 미사용)
- 출처 없는 수치
- 3레벨 이상 중첩 불렛

## So-what Footer (모든 deliverable 마지막 줄)

특히, [finding] → 따라서 [recommendation]
