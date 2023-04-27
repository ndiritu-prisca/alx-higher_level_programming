-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- displays: tv_genres.name - rating sum in descending order of rating
-- 1 SELECT statement
SELECT name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;