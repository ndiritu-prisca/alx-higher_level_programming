-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- displays: tv_shows.title - rating sum in descending order of rating
-- 1 SELECT statement
SELECT title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
