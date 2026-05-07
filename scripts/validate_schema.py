from pathlib import Path
import json

schema_path = Path("schemas/errata_report.schema.json")

if not schema_path.exists():
    raise FileNotFoundError("Missing schemas/errata_report.schema.json")

with schema_path.open("r", encoding="utf-8") as f:
    json.load(f)

print("Schema file is valid JSON.")
