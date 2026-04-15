import requests
import json
from datetime import datetime
from pathlib import Path

API_URL = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(API_URL)

if response.status_code != 200:
    raise Exception(f"API request failed: {response.status_code}")

data = response.json()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

file_path = output_dir / f"jobs_{timestamp}.json"

with open(file_path, "w") as f:
    json.dump(data, f)

print(f"Saved raw data to {file_path}")