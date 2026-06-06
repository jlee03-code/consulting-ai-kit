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
| `prompts/research-agent-openai.md` | Mode B: paste into ChatGPT for research tasks |
| `prompts/research-agent-claude.md` | Mode B: paste into Claude.ai for research tasks |
| `prompts/finance-agent-openai.md` | Mode B: paste into ChatGPT for financial modeling |
| `prompts/finance-agent-claude.md` | Mode B: paste into Claude.ai for financial modeling |
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

**On Windows?** See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for a step-by-step guide — no Git or bash required.

### Testing in Isolation (without touching your existing ~/.claude setup)

```bash
mkdir -p /tmp/claude-kit-test
HOME=/tmp/claude-kit-test bash install.sh
HOME=/tmp/claude-kit-test claude
```

This gives a completely clean `~/.claude/` — no existing skills, settings, or CLAUDE.md.
Only the kit's 4 skills and rules are loaded. When done: `rm -rf /tmp/claude-kit-test`.

### Mode B -- Browser (ChatGPT, Claude.ai, no installation)

1. Open `prompts/research-agent.md` and copy the entire file contents
2. Paste as the **first message** in a fresh ChatGPT or Claude.ai chat
3. The agent will ask for context, then produce BCG-register Korean output

Four prompts available:
- `prompts/research-agent-openai.md` -- market sizing, competitive analysis (ChatGPT)
- `prompts/research-agent-claude.md` -- market sizing, competitive analysis (Claude.ai)
- `prompts/finance-agent-openai.md` -- DCF, P&L, sensitivity tables (ChatGPT)
- `prompts/finance-agent-claude.md` -- DCF, P&L, sensitivity tables (Claude.ai)

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
