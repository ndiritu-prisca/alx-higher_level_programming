-- lists all shows contained in the database hbtn_0d_tvshows
-- displays: tv_shows.title - tv_show_genres.genre_id in ascedning order
-- If a show doesn’t have a genre, displays NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
