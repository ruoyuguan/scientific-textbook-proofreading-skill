from pathlib import Path

skill_path = Path("skill/SKILL.md")
text = skill_path.read_text(encoding="utf-8")

required = ["---", "name:", "description:", "## Purpose", "## Required Output Format"]

missing = [item for item in required if item not in text]

if missing:
    raise SystemExit(f"Missing required markers in SKILL.md: {missing}")

print("SKILL.md passed basic lint checks.")
