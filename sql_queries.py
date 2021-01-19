# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS artists"
song_table_drop = "DROP TABLE IF EXISTS users"
artist_table_drop = "DROP TABLE IF EXISTS songs"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays(\
                songplay_id serial PRIMARY KEY,\
                start_time bigint,\
                user_id varchar,\
                level varchar,\
                song_id varchar,\
                artist_id varchar,\
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
                hour integer,\
                day integer,\
                week integer,\
                month integer,\
                year integer,\
                weekday integer);")
                
# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays\
                         (start_time,\
                          user_id,\
                          level,\
                          song_id,\
                          artist_id,\
                          session_id,\
                          location,\
                          user_agent)\
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\
                              ON CONFLICT DO NOTHING;")
                        

user_table_insert = ("INSERT INTO users\
                        (user_id,\
                        first_name,\
                        last_name,\
                        gender,\
                        level)\
                        VALUES (%s, %s, %s, %s, %s);")

song_table_insert =  ("INSERT INTO songs\
                        (song_id,\
                        title,\
                        artist_id,\
                        year,\
                        duration)\
                        VALUES (%s, %s, %s, %s, %s)\
                            ON CONFLICT DO NOTHING;")
                        

artist_table_insert = ("INSERT INTO artists\
                        (artist_id,\
                        name,\
                        location,\
                        latitude,\
                        longitude)\
                        VALUES (%s, %s, %s, %s, %s)\
                            ON CONFLICT DO NOTHING;;")


time_table_insert = ("INSERT INTO time\
                        (start_time,\
                        hour,\
                        day,\
                        week,\
                        month,\
                        year,\
                        weekday)\
                        VALUES (%s, %s, %s, %s, %s, %s, %s);")

# FIND SONGS

song_select = ("SELECT s.song_id, a.artist_id FROM songs AS s\
                JOIN artists AS a\
                   ON a.artist_id = s.artist_id\
                WHERE s.title = %s\
                    AND\
                    a.name = %s\
                    AND\
                    s.duration = %s;")
                    


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]