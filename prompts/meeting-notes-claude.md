---
name: Meeting Notes Summarizer — Anthropic (Mode B)
purpose: Structured synthesis of uploaded meeting notes into key findings and takeaways
mode: Browser-only — paste as first message in a fresh Claude.ai chat, then upload your notes
---

<context>
The user has uploaded meeting notes and needs a structured summary document
derived from those notes. The output is a synthesis artifact — not a
transcript — intended to surface key findings concisely for a reader who
was not present.
</context>

<instructions>
Read the uploaded meeting notes in full before writing anything.

Produce the summary in this exact structure:

1. SECTION BLOCKS
   Identify the key topics or themes from the notes and create one block per
   theme.
   Each block follows this exact format:

   • (Keyword) One sentence stating what this section covers — what was new,
     what was discovered, or what the key finding is.
       – Concise fact, quote, or finding drawn directly from the notes.
       – Concise fact, quote, or finding drawn directly from the notes.
       – (Add sub-bullets as needed; omit any that add no new information.)

   Rules for every block:
   - The (Keyword) is a 1–3 word label that acts as the section header.
   - The opening sentence must state a finding, not a description of the topic.
   - Sub-bullets parse the evidence: specific facts, direct quotes (in
     quotation marks), or discrete findings.
   - Do not repeat information across blocks.

2. MEETING SUMMARY
   After all section blocks, add a divider line, then:

   Key Takeaways
   • [Most important finding or decision from the meeting]
   • [Second most important finding or decision]
   • [Third most important finding or decision — omit if fewer than 3 exist]

   Maximum 3 bullets. Each bullet is one sentence. No sub-bullets.
</instructions>

<constraints>
Total length: 2 pages maximum (approximately 600–800 words).
Every bullet and sub-bullet must be traceable to the uploaded notes — do not
infer or editorialize beyond what is stated.
If a direct quote is used, reproduce it exactly and place it in quotation marks.
Omit any section for which the notes contain no substantive finding.
</constraints>

<output_format>
Section blocks in the order they appear most logically (not necessarily
chronological).
Each block: one (Keyword) opening bullet + sub-bullets indented one level.
Divider after the last section block.
"Key Takeaways" label followed by 2–3 standalone bullets.
No headers, no bold section titles — the (Keyword) pattern carries all
structure.
</output_format>
