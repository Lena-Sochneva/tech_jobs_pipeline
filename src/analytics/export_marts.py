from clickhouse_connect import get_client
import pandas as pd
from pathlib import Path

# подключение
client = get_client(
    host="localhost",
    port=8123,
    username="default",
    password="random123"
)

output_dir = Path("data/marts")
output_dir.mkdir(parents=True, exist_ok=True)

# -------------------------
# jobs_by_location
# -------------------------
query_location = """
SELECT
    location,
    count() AS jobs_count
FROM jobs
GROUP BY location
ORDER BY jobs_count DESC
"""

df_location = client.query_df(query_location)
df_location.to_csv("data/marts/jobs_by_location.csv", index=False)

print("jobs_by_location exported")


# -------------------------
# jobs_by_day
# -------------------------
query_day = """
SELECT
    toDate(toDateTime(created_at)) AS day,
    count() AS jobs_count
FROM jobs
GROUP BY day
ORDER BY day
"""

df_day = client.query_df(query_day)
df_day.to_csv("data/marts/jobs_by_day.csv", index=False)

print("jobs_by_day exported")


# -------------------------
# skills_frequency
# -------------------------
query_skills = """
SELECT
    arrayJoin(tags) AS skill,
    count() AS skill_count
FROM jobs
GROUP BY skill
ORDER BY skill_count DESC
LIMIT 20
"""

df_skills = client.query_df(query_skills)
df_skills.to_csv("data/marts/skills_frequency.csv", index=False)

print("skills_frequency exported")