---
name: finance-model
description: |
  DCF / P&L / sensitivity modeling in BCG Korean register.
  Mode A (Claude Code + Excel MCP): builds .xlsx via @negokaz/excel-mcp-server.
  Mode B (browser / no MCP): outputs pandas-style text tables.
  Use when asked to build a DCF, projection, or financial model.
  Trigger: "DCF", "밸류에이션", "재무 모델", "sensitivity", "FCF", "projection"
allowed-tools: "Read,Write,Edit,Bash(npx:*)"
version: "1.0.0"
---

# Finance Model — BCG Korean Register

결과 해설은 한국어. 단위 억/조 + USD M/B 병기. 셀 규칙 준수.
최종 출력은 house-style 스켈레톤을 통과시켜 작성한다.

---

## Mode Detection

**Mode A — Excel MCP available** (Claude Code + Node 18+ + `@negokaz/excel-mcp-server`):
→ `npx --yes @negokaz/excel-mcp-server` 로 .xlsx 생성

**Mode B — Browser / no MCP**:
→ pandas DataFrame 형태 텍스트 표로 동일 구조 출력

---

## Input Gathering (묻고 시작)

모델 시작 전 확인:
- 모델 유형: DCF / P&L / 기타
- 대상 기업·사업 및 기준 연도
- 보유 수치 (매출, 마진, WACC 등)
- 누락 시: 업종 평균 기본값 적용 + 가정 블록 명시

---

## Input Validation

진행 전 검증:
- 매출 성장률 0-30%
- EBITDA 마진 양수
- 세율 0-40%
- WACC 7-15%
- terminal growth < WACC (위반 시 수정 요청)

---

## Output Skeleton (6개 섹션)

### 1. 헤드라인
house-style Formula 1: [주제] | [결론 + 숫자]
예: "Subject DCF | EV ~$147B, implied price $52.00/주"

### 2. 가정 블록 [입력]
```
매출 성장률:  Y1: X%  Y2: X%  Y3: X%  Y4: X%  Y5: X%
EBITDA 마진: X%
D&A (% 매출): X%
CapEx (% 매출): X%
NWC 변화 (% 매출): X%
세율: X%
WACC: X%
Terminal growth: X%
Net debt: $XM
Shares outstanding: XM
```

### 3. 추정 [수식]
연도 헤더: YYYY A (실적) → YYYY F (추정) | CAGR 열 맨 오른쪽

```
(단위: $M)          | 2024A | 2025F | 2026F | 2027F | 2028F | 2029F | CAGR
Revenue             |       |       |       |       |       |       |
EBITDA              |       |       |       |       |       |       |
EBIT                |       |       |       |       |       |       |
NOPAT               |       |       |       |       |       |       |
+ D&A               |       |       |       |       |       |       |
- CapEx             |       |       |       |       |       |       |
- ΔNWC              |       |       |       |       |       |       |
Unlevered FCF       |       |       |       |       |       |       |
```

### 4. 밸류에이션 [연결]
```
PV FCF (합계):       $XM
Terminal value (TV): $XM  (Gordon Growth: FCF_n+1 / (WACC - g))
PV of TV:            $XM
Enterprise Value:    $XM
- Net Debt:          $XM
Equity Value:        $XM
Shares outstanding:  XM
Implied price/share: $X.XX
TV as % of EV:       X%
```

시나리오 3개: Base / Bull / Bear (성장률 ±2pp, WACC ±1pp)

### 5. 민감도 2-way
행: WACC (base ±2%, 1pp 간격)
열: Terminal growth (1.5%, 2.0%, 2.5%, 3.0%, 3.5%)
셀: Enterprise Value ($M)

```
EV ($M)    | TGR 1.5% | 2.0% | 2.5% | 3.0% | 3.5%
WACC  8%   |          |      |      |      |
      9%   |          |      |      |      |
     10%   |          |      | BASE |      |
     11%   |          |      |      |      |
     12%   |          |      |      |      |
```

### 6. BCG 의견
```
[BCG 의견]
TV % 경고 (>80% EV 시): terminal growth 가정 재검토 권고.
가정 합리성 코멘트.
주요 민감 변수 식별.
```

---

## Cell Rules (셀 규칙)

- **[입력]** = 하드코딩 (Mode A: 파란 셀)
- **[수식]** = 산출 공식 (Mode A: 검은 셀)
- **[연결]** = 시트 간 연결 (Mode A: 초록 셀)

---

## Mode A — Excel MCP Instructions

Sheet 구성: Assumptions → FCF Projections → Valuation → Sensitivity
- 색상: 파란(입력) / 검은(수식) / 초록(연결)
- 상단 행·좌측 열 고정
- 헤더 볼드, 셀 테두리
- 민감도 테이블 조건부 서식 (green=high, red=low)

## Mode B — Text Table Instructions

pandas 재현 가능 행/열 구조로 위 스켈레톤 전체 텍스트 출력.
각 섹션 구분선 `---` 사용.
마지막에 Python 재현 코드 블록 제공 (선택).

---

## Error Handling

| 상황 | 대응 |
|------|------|
| terminal growth >= WACC | 수정 요청, 이유 설명 |
| 음수 FCF | 마진/CapEx 가정 재검토 권고 |
| TV > 80% EV | 경고 + 성장 가정 재검토 권고 |
| 입력 부재 | 업종 평균 기본값 + 가정 블록 명시 |

---

## Templates

추가 파이썬 유틸리티:
- `templates/tam_sam_som.py` — TAM/SAM/SOM 사이징 계산기
- `templates/projection.py` — FCF projection 테이블 생성기
- `templates/exhibit.py` — BCG 스타일 텍스트 exhibit 렌더러
