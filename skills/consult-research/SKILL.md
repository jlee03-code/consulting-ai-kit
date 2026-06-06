---
name: consult-research
description: |
  TAM/SAM/SOM sizing and competitive analysis engine in BCG Korean register.
  Forks market-research with consulting-grade triangulation, [사실]/[추론]/[권고]
  claim tagging, and Q×P waterfall methodology.
  Use when asked to size a market, analyze competitors, identify KSF, or produce
  any research deliverable. Routes final output through house-style.
  Trigger: "size this market", "competitive analysis", "어떤 시장", "파트너 스크리닝"
allowed-tools: "Read,Write,Edit"
version: "1.0.0"
---

# Consult Research — BCG Korean Register

결과는 한국어 컨설턴트 어투. 수치에 출처·가정 명시. [사실]/[추론]/[권고] 구분.
최종 출력은 house-style 스켈레톤을 통과시켜 작성한다.

---

## Research Standards

1. 모든 수치에 출처와 가정 명시 — 출처 없는 수치 금지
2. [사실] / [추론] / [권고] 태그로 모든 주장 구분
3. 반대 근거와 하방 케이스 포함
4. 결론에서 결정 사항 도출 — 단순 요약 금지
5. 데이터 없으면 [추론] + 가정 명시, 추정 방법론 공개

---

## Output Skeleton (6개 섹션, 전부 필수)

### 1. 헤드라인
house-style Formula 1 사용 우선: [주제] | [결론 + 숫자]
2줄 이내. 결론과 숫자 반드시 포함.

### 2. 핵심 요약 (Key Summary)
최대 3줄. 각 줄은 사용자 질문에 직접 답하는 독립적 완결 문장.
① [가장 중요한 발견 — 직접적인 답]
② [핵심 근거 또는 두 번째 발견]
③ [주요 시사점, 리스크, 또는 고려사항]
본문과 BCG 의견은 ①→②→③ 순서로 전개. 줄 수는 주제에 맞게 줄일 수 있음.

### 3. TAM/SAM/SOM 워터폴
단계별 Q × P 산출. 억/조 + USD M/B 병기.

```
TAM: [전체 시장] = Q (수요량) × P (단가)
     → $[X]B / 약 [X]조 원
     가정: [공급자 수 × 평균 계약 규모] or [소비자 수 × 1인당 지출]
     출처: [출처]

SAM: [접근 가능 시장] = TAM × [접근 비율]
     → $[X]M / 약 [X]억 원
     가정: [지역 한정 / 채널 한정 / 인증 요건]
     출처: [출처]

SOM: [현실적 점유] = SAM × [점유율 가정]
     → $[X]M / 약 [X]억 원
     가정: [영업력 / 파트너 커버리지 / 브랜드 인지도]
     출처: BCG 추정
```

### 4. [참고] 추정 방법론
Q × P 로직 트리. 가정 분기 명시.

```
[참고] SAM 추정 방법론
  공급 측: 공급자 수 × 평균 매출
  수요 측: 소비자 수 × 구매 빈도 × 단가
  채택 근거: [이유]
  주요 가정: [가정1], [가정2]
```

### 5. 경쟁 구도 스코어링
후보/경쟁사(열) × KSF 기준(행), H/M/L 평가.

| KSF | Client | 경쟁사A | 경쟁사B |
|-----|--------|---------|---------|
| 채널 커버리지 | M | H | L |
| 브랜드 인지도 | H | M | M |
| 기술 역량 | H | H | M |
| **종합 판정** | **우위** | **대등** | **열위** |

### 6. 삼각 검증 (가능 시)
Sell-side vs BCG 바텀업, % gap 레이블.

```
Sell-side 추정: $[X]B
BCG 바텀업:    $[X]B
Gap:          +[X]% → [이유 설명]
```

---

## Claim Tags (모든 주장에 1개 태그 필수)

- **[사실]** 출처 확인 가능한 데이터 또는 시장 공개 정보
- **[추론]** 제한된 데이터에서 도출한 논리적 추정
- **[권고]** BCG 판단 또는 전략적 권고

---

## BCG 의견 Callout

근거(evidence)와 의견 반드시 분리.

```
[BCG 의견]
핵심 시사점 1-3줄. 근거와 구분된 editorial 판단.
```

---

## Source Footer

```
Source: [출처1], [출처2], BCG analysis
```
출처 불명확 시: "출처 불명확 — 추가 검증 필요"

---

## So-what Footer (마지막 줄, bold)

**특히, [finding] → 따라서 [recommendation]**

---

## Action Protocol

1. 먼저 묻고 시작: 대상 시장·지역, 분석 목적(진입/사이징/경쟁), 보유 데이터
2. 데이터 부재 시: [추론] 태그 + 가정 블록 공개
3. 삼각 검증 가능 시: sell-side와 바텀업 비교 제시
4. 출력 완료 후: house-style 스켈레톤 통과 확인
