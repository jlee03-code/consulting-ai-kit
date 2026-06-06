# Consulting AI Kit

Portable BCG-register consulting toolkit for Claude Code (Mode A) and browser AI (Mode B).
All output defaults to Korean consultant register: assertive, number-anchored, action-oriented.

---

## What's Inside

| Path | Purpose |
|------|---------|
| `skills/house-style/` | BCG slide authoring engine -- all deliverables route through this |
| `skills/consult-research/` | TAM/SAM/SOM sizing + competitive analysis |
| `skills/finance-model/` | DCF / P&L / sensitivity (Excel MCP or text tables) |
| `skills/karpathy-guidelines/` | Reasoning guardrails (verbatim, MIT) |
| `prompts/research-agent.md` | Mode B: paste into ChatGPT for research tasks |
| `prompts/finance-agent.md` | Mode B: paste into ChatGPT for financial modeling |
| `CLAUDE.md` | Session-level directives -- copy to your project root |

---

## Quick Start

### Mode A -- Claude Code (full features, Excel MCP)

Requirements: Claude Code, Node 18+

```bash
git clone https://github.com/jlee03-code/consulting-ai-kit
cd consulting-ai-kit
bash install.sh
# Start a new Claude Code session
```

The installer copies skills to `~/.claude/skills/` and rules to `~/.claude/rules/`.
Copy `CLAUDE.md` to your project root to activate BCG register directives.

### Mode B -- Browser (ChatGPT, Claude.ai, no installation)

1. Open `prompts/research-agent.md` and copy the entire file contents
2. Paste as the **first message** in a fresh ChatGPT or Claude.ai chat
3. The agent will ask for context, then produce BCG-register Korean output

Two prompts available:
- `prompts/research-agent.md` -- market sizing, competitive analysis
- `prompts/finance-agent.md` -- DCF, P&L, sensitivity tables

---

## Skills Reference

### house-style
BCG-register slide authoring. Enforces 5 headline formulas, 6 body structures,
BCG 의견 callout, source footer, and unit conventions (억/조 + USD M/B).
All other skills route final output through this skill.

### consult-research
TAM/SAM/SOM waterfall with Q x P methodology. [사실]/[추론]/[권고] claim tagging.
Triangulation (sell-side vs BCG bottom-up). Competitive scoring matrix (H/M/L).

### finance-model
DCF with 5-year FCF projection, Gordon Growth terminal value, 2-way sensitivity.
- **Mode A**: generates `.xlsx` via `@negokaz/excel-mcp-server`
- **Mode B**: outputs pandas-style text tables (browser compatible)

### karpathy-guidelines
Verbatim behavioral guardrails from Andrej Karpathy's LLM coding observations.
Appended directive: output stays in Korean consultant register regardless.

---

## Output Contract

Every deliverable must contain:

1. **Headline** -- conclusion + number, 2 lines max
2. **Body** -- one of 6 BCG structures
3. **BCG 의견** -- opinion fenced from evidence
4. **Source** -- `Source: [...], BCG analysis`
5. **Units** -- 억/조 + USD M/B on every figure

---

## License

`karpathy-guidelines` is MIT. All other kit files are released under MIT.
See LICENSE for details.
