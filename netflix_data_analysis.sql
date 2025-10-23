CREATE DATABASE netflix_db;
USE netflix_db;
SELECT * FROM netflix_db.netflix_titles;


# 1. Directors who created both Movies and TV Shows
SELECT director
FROM netflix_titles
WHERE director != ''
GROUP BY director
HAVING COUNT(DISTINCT type) > 1;

# 2.Country with the highest number of Comedy Movies
SELECT country, COUNT(*) AS comedy_count
FROM netflix_titles
WHERE listed_in LIKE '%Comedy%' AND type = 'Movie'
GROUP BY country
ORDER BY comedy_count DESC
LIMIT 1;

# 3.Top Director Each Year 
SELECT release_year, director, COUNT(*) AS total
FROM netflix_titles
WHERE director != ''
GROUP BY release_year, director
ORDER BY release_year ASC, total DESC;

# 4.Average Movie Duration by Genre
SELECT listed_in, 
       AVG(CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED)) AS avg_duration
FROM netflix_titles
WHERE type = 'Movie' AND duration LIKE '%min%'
GROUP BY listed_in;


# 5.Directors who made both Comedy & Horror Movies
SELECT director
FROM netflix_titles
WHERE director != '' AND (listed_in LIKE '%Comedy%' OR listed_in LIKE '%Horror%')
GROUP BY director
HAVING SUM(listed_in LIKE '%Comedy%') > 0 
   AND SUM(listed_in LIKE '%Horror%') > 0;
