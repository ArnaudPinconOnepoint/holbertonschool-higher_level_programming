-- This script lists all shows in the hbtn_0d_tvshows database that do not have a genre linked.
-- Each record displays the show title and genre ID.
-- Results are sorted in ascending order by show title and genre ID.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
