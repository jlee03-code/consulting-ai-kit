# CLAUDE.md — Consulting AI Kit (Portable)

## Top Directive

Default reply language: Korean (consultant register / BCG 레지스터).
단정형·숫자 선행·실행 지향. 모든 헤드라인은 결론과 숫자를 함께 포함한다.
English only for: code identifiers, machine-readable metadata, and acronyms
with no clean Korean equivalent (CAGR, SAM, SOM, TAM, JV, KSF, O&M, M&A,
KOL, SKU, EPC, WACC, FCF, EBITDA). 이 약어들은 절대 번역하지 않는다.

## Skills (install.sh copies to ~/.claude/skills/)

- house-style       -- BCG 슬라이드 작성 엔진. 모든 산출물이 통과
- consult-research  -- TAM/SAM/SOM 사이징 + 경쟁 분석
- finance-model     -- DCF / P&L / 민감도 (Mode A: Excel MCP / Mode B: pandas 표)
- karpathy-guidelines -- 추론·표현 가드레일 (verbatim + Korean directive)

## Two Browser Prompts (Mode B)

- prompts/research-agent.md  -- ChatGPT GPT #1 (리서치)
- prompts/finance-agent.md   -- ChatGPT GPT #2 (재무 모델링)
Paste as first message in a fresh chat. No installation required.

## Workflow Defaults

- Plan First -- 3+단계 또는 구조 결정 -> plan mode
- Verify Before Done -- 출력 없이 완료 처리 금지
- 어긋나면 즉시 멈추고 재계획

## 6-Step Task Ritual

1. Plan    -- 체크 가능한 항목으로 계획 작성
2. Confirm -- 구현 전 계획 합의
3. Track   -- 진행하며 항목 완료 표시
4. Explain -- 단계별 상위 수준 요약
5. Verify  -- house-style 스켈레톤 통과 확인
6. Document -- 결과·교훈 기록

## Output Contract (모든 deliverable에 5개 섹션)

1. 헤드라인 (결론 + 숫자, 2줄 이내)
2. 본문 구조: assertion+columns / tam-sam-waterfall / scoring-matrix /
   screening-funnel / gap-to-target / issue-stack
3. BCG 의견 callout (근거와 분리)
4. Source: [sources], BCG analysis (소문자)
5. 단위: 억/조 + USD M/B

## Anti-Patterns (금지)

- 숫자 없는 헤드라인
- 영문 약어 한국어 직역
- 근거와 의견 혼재 (BCG 의견 callout 미사용)
- 출처 없는 수치
