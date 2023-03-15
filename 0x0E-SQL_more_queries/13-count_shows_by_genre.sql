-- lists all genres from hbtn_0d_tvshows and displays the number of shows
-- linked to each
-- display: <TV Show genre> - <Number of shows linked to this genre>
-- in descending order of number_of_shows
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
