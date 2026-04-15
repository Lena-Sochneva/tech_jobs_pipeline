import pandas as pd
import json
from clickhouse_connect import get_client

df = pd.read_parquet("data/processed/jobs_clean.parquet")

print("Rows to load:", len(df))

# нормализация типов
df = df.fillna("")

df["title"] = df["title"].apply(str)
df["company_name"] = df["company_name"].apply(str)
df["location"] = df["location"].apply(str)
df["created_at"] = df["created_at"].astype(int)

df["tags"] = df["tags"].apply(
    lambda x: [str(i) for i in x] if isinstance(x, list) else []
)

client = get_client(
    host="localhost",
    port=8123,
    username="default",
    password="random123"
)

client.command("""
CREATE TABLE IF NOT EXISTS jobs
(
    title String,
    company_name String,
    location String,
    created_at Int64,
    tags Array(String)
)
ENGINE = MergeTree
ORDER BY created_at
""")

# преобразование в JSONEachRow
rows = "\n".join(
    json.dumps(row, ensure_ascii=False)
    for row in df.to_dict("records")
)

client.command(
    "INSERT INTO jobs FORMAT JSONEachRow",
    data=rows
)

print("Load finished")