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

- prompts/research-agent.md       -- ChatGPT or Claude.ai (리서치)
- prompts/finance-agent-openai.md -- ChatGPT (재무 모델링)
- prompts/finance-agent-claude.md -- Claude.ai (재무 모델링)
Paste as first message in a fresh chat. No installation required.

---

## Core Principles

- **Simplicity First** -- every change as simple as possible; touch only what's necessary.
- **No Laziness** -- find root causes, not temporary fixes. Senior-developer standards.
- **Minimal Impact** -- keep diffs surgical to avoid introducing bugs.

## Workflow

### Plan Mode
- Enter plan mode for any non-trivial task (3+ steps or structural decisions).
- If something goes sideways, stop and re-plan immediately.
- Use plan mode for verification steps, not just building.
- Write detailed specs upfront to reduce ambiguity.

### Subagent Strategy
- Use subagents to keep main context clean.
- Offload research, exploration, and parallel analysis to subagents.
- For complex problems, use parallel subagents for speed and diversity.
- One task per subagent for focused execution.

### Verification Before Done
- Never mark a task complete without proving it works.
- Run smoke tests, inspect logs, demonstrate output.
- Ask: "Would a staff engineer approve this?"

### Autonomous Problem Solving
- Given a bug or error: diagnose root cause and fix it. Don't ask for hand-holding.
- Point at logs, errors, failing scripts — then resolve them.

## 6-Step Task Ritual

1. Plan    -- 체크 가능한 항목으로 계획 작성
2. Confirm -- 구현 전 계획 합의
3. Track   -- 진행하며 항목 완료 표시
4. Explain -- 단계별 상위 수준 요약
5. Verify  -- house-style 스켈레톤 통과 확인
6. Document -- 결과·교훈 기록

---

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
