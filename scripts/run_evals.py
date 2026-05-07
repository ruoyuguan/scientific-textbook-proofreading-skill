from pathlib import Path
import json

cases_path = Path("evals/cases.jsonl")

if not cases_path.exists():
    raise FileNotFoundError("Missing evals/cases.jsonl")

count = 0
with cases_path.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        item = json.loads(line)
        for key in ["id", "field", "input", "expected"]:
            if key not in item:
                raise SystemExit(f"Missing key {key} in eval case: {item}")
        count += 1

print(f"Loaded {count} eval cases.")
