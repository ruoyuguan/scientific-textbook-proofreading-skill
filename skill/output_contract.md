# Output Contract

Every reported issue should include:

1. Location.
2. Original formula or statement.
3. Problem type.
4. Re-derivation or check.
5. Judgement.
6. Corrected formula or statement.
7. Suggested replacement prose when needed.
8. Confidence.

The assistant should not report correct formulae unless the user asks for a complete derivation log.

The assistant must not invent page numbers, equation numbers, citations, or claims about sources.

## Local File Report Contract

When operating in Local File Report Mode, the assistant should write review outputs to Markdown files under `reports/`.

Required files for multi-chapter review:

```text
reports/
├── chapter_01_errata.md
├── chapter_02_errata.md
├── ...
├── processing_notes.md
└── summary.md
```

Each `chapter_NN_errata.md` file must include:

1. Chapter title or review unit.
2. Manuscript under review.
3. Reference sources used.
4. List of reported issues.
5. Chapter-level summary.

The assistant should not dump a full multi-chapter report into chat when the user has requested file output.

The chat response should only summarize what files were created or updated.
