# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id integer, start_time timestamp,
user_id integer, level varchar, song_id integer, artist_id integer, session_id integer, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id integer, first_name varchar, lastname varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id integer, title varchar, artist_id integer, year integer, duration decimal)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id integer, name varchar, location varchar, latitude decimal)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour integer, day integer, week integer, month integer, year integer, weekday varchar) 
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, lastname, gender, level) VALUES (%s, %s, %s, %s, %s)""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude) VALUES (%s, %s, %s, %s)""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]