import pandas as pd
import json
from pathlib import Path

raw_files = list(Path("data/raw").glob("*.json"))

if not raw_files:
    raise Exception("No raw files found")

latest_file = max(raw_files)

print("Reading file:", latest_file)

with open(latest_file) as f:
    data = json.load(f)

jobs = pd.DataFrame(data["data"])

print("Rows in raw dataset:", len(jobs))

jobs_clean = jobs[[
    "title",
    "company_name",
    "location",
    "created_at",
    "tags"
]]

jobs_clean = jobs_clean.dropna(subset=["title"])

print("Rows after cleaning:", len(jobs_clean))

output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "jobs_clean.parquet"

jobs_clean.to_parquet(output_file)

print("Saved cleaned data to:", output_file)