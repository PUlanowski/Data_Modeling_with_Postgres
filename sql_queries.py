# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS artists"
song_table_drop = "DROP TABLE IF EXISTS users"
artist_table_drop = "DROP TABLE IF EXISTS songs"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays(\
                songplay_id integer,\
                start_time timestamp UNIQUE,\
                user_id integer UNIQUE,\
                level varchar,\
                song_id varchar UNIQUE,\
                artist_id varchar UNIQUE,\
                session_id integer,\
                location varchar,\
                user_agent varchar);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(\
                artist_id varchar,\
                name varchar,\
                location varchar,\
                latitude float,\
                longitude float);")

user_table_create = ("CREATE TABLE IF NOT EXISTS users(\
                user_id varchar,\
                first_name varchar,\
                last_name varchar,\
                gender varchar,\
                level varchar);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs(\
                song_id varchar,\
                title varchar,\
                artist_id varchar,\
                year integer,\
                duration float);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time(\
                start_time timestamp,\
                hour time,\
                day integer,\
                week integer,\
                month integer,\
                year integer,\
                weekday integer);")
                
# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("INSERT INTO users (user_id,\
                        first_name,\
                        last_name,\
                        gender,\
                        level)\
                        VALUES (%s, %s, %s, %s, %s);")

song_table_insert =  ("INSERT INTO songs (song_id,\
                        title,\
                        artist_id,\
                        year,\
                        duration)\
                        VALUES (%s, %s, %s, %s, %s);")

artist_table_insert = ("INSERT INTO artists (artist_id,\
                        name,\
                        location,\
                        latitude,\
                        longitude)\
                        VALUES (%s, %s, %s, %s, %s);")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]