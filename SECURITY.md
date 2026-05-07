# Security Policy

## Scope

This repository provides an AI-agent skill for scientific textbook proofreading and errata auditing. It is not a hosted service and does not process user files on its own.

Security concerns may still arise because users may run the skill locally with AI coding agents, PDFs, manuscripts, scripts, and external tools.

## Supported versions

During the alpha stage, only the latest commit on the `main` branch and the latest pre-release are actively maintained.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| latest pre-release | Yes |
| older alpha releases | Best effort |
| forks or modified copies | No |

## Sensitive materials

Do not commit or upload:

- Private manuscripts.
- Copyrighted textbooks or solution manuals.
- Proprietary teaching materials.
- Personal data.
- API keys or access tokens.
- Local `.env` files.
- Generated reports that contain large copyrighted excerpts.
- Confidential review comments.

The repository is intended to store the skill, schemas, examples, and synthetic test cases—not private source documents.

## Local file safety

When using this skill with Codex, Claude Code, or another local agent:

1. Keep manuscripts and reference PDFs in a local project directory.
2. Use explicit file-role prefixes such as `UNDER_REVIEW_`, `REFERENCE_`, `ANSWER_KEY_`, and `IGNORE_`.
3. Review generated reports before sharing them.
4. Do not allow an agent to delete or overwrite source PDFs.
5. Back up important manuscripts before running automated workflows.

## Reporting a vulnerability

If you discover a security issue in this repository, please do not open a public issue if the report includes private files, credentials, or sensitive paths.

Instead, report the issue privately through GitHub's security reporting tools if available, or contact the maintainer directly.

Please include:

- A clear description of the issue.
- Steps to reproduce it.
- A minimal example that does not include private or copyrighted files.
- The affected files or scripts.
- Any suggested mitigation.

## Out of scope

The following are usually out of scope for this repository:

- Model hallucinations that are not caused by repository instructions.
- Scientific disagreements that require domain-expert judgement.
- Problems caused by external PDF extraction tools.
- Issues introduced by third-party agent platforms.
- User-local configuration problems unrelated to this repository.

## Disclaimer

This skill produces candidate errata for expert human review. It should not be used as an authoritative scientific, legal, security, medical, or financial decision-making system.
