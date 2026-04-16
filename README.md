# Tech Jobs ETL Pipeline

## Overview

This project is a data pipeline that extracts job vacancies from an external API, processes the data, and loads it into ClickHouse for analytical querying.

Pipeline stages:
- Extract → fetch raw job data from API
- Transform → clean and normalize data using pandas
- Load → store data in ClickHouse
- Analytics → build data marts and export them for analysis

---

## Tech Stack

- Python
- pandas
- ClickHouse
- Docker

---

## Project Structure

📁 tech_jobs_pipeline/  
├── 📁 src/  
│    ├── 📁 extract/  
│    ├── 📁 transform/ 
│    ├── 📁 load/  
│    └── 📁 analytics/   
├── 📁 data/  
│   ├── 📁 raw/  
│   ├── 📁 processed/  
│   └── 📁 marts/  
└── 📁 sql/  
    └── 📄 marts.sql

---

## Data Pipeline

API → 
Extract (Python) →
Raw JSON →
Transform (pandas) → 
Parquet → 
Load (ClickHouse) →
Data marts (SQL) → 
CSV export

---

## Data Marts

### Jobs by Location

Top locations by number of job postings.

### Jobs by Day

Distribution of job postings over time.

### Skills Frequency

Most common skills extracted from job tags.

---

## Example Queries SQL

```sql
SELECT location, count()
FROM jobs
GROUP BY location
ORDER BY count() DESC;
```
```sql
SELECT arrayJoin(tags) AS skill, count()
FROM jobs
GROUP BY skill
ORDER BY count() DESC;
```
---

## Example Output

Jobs by location (top 5):

Germany — 45  
USA — 30  
Netherlands — 20  

Skills frequency (top 5):

Python — 60  
SQL — 55  
AWS — 40  
Docker — 25  

---

## How to Run

- Activate virtual environment
```bash 
source venv/bin/activate 
```
- Start ClickHouse
```bash 
docker start clickhouse-server
```
- Run pipeline
```bash 
python src/extract/fetch_jobs.py
python src/transform/clean_jobs.py
python src/load/load_jobs.py
```
- Export data marts
```bash 
python src/analytics/export_marts.py
```

---

## Output

The project generates CSV files:

data/marts/jobs_by_location.csv
data/marts/jobs_by_day.csv
data/marts/skills_frequency.csv