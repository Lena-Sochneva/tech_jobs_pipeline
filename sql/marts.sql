-- =========================
-- jobs by location
-- =========================
SELECT
    location,
    count() AS jobs_count
FROM jobs
GROUP BY location
ORDER BY jobs_count DESC;


-- =========================
-- jobs by day
-- =========================
SELECT
    toDate(toDateTime(created_at)) AS day,
    count() AS jobs_count
FROM jobs
GROUP BY day
ORDER BY day;


-- =========================
-- skills frequency
-- =========================
SELECT
    arrayJoin(tags) AS skill,
    count() AS skill_count
FROM jobs
GROUP BY skill
ORDER BY skill_count DESC
LIMIT 20;