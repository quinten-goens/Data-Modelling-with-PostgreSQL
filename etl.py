import os
import glob
import psycopg2
import datetime
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Processes the song file located at filepath and inserts song and artist data 
    in appropriate tables.
    
    Params 
    ------
    cur : psycopg2.extensions.cursor
    filepath : str
    
    returns
    -------
    None
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data =list(df[['song_id','title', 'artist_id','year','duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df[[
        'artist_id',
        'artist_name',
        'artist_location',
        'artist_latitude',
        'artist_longitude']
    ].values[0]) 
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Processes the log file located at filepath and inserts time, user and songplay data 
    in appropriate tables.
    
    Params 
    ------
    cur : psycopg2.extensions.cursor
    filepath : str
    
    returns
    -------
    None
    """
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    df['timestamp_full'] = pd.DataFrame(df['ts'].apply(lambda l: datetime.datetime.fromtimestamp(l/1000.0)))
    t = df[['timestamp_full']].rename({'timestamp_full':'ts'},axis=1)
    
    # insert time data records
    time_df = pd.DataFrame()
    (
    time_df['timestamp'],
    time_df['hour'],
    time_df['day'],
    time_df['week_of_year'],
    time_df['month'],
    time_df['year'],
    time_df['weekday'],
    ) = zip(*t['ts'].apply(lambda l: (
        l,
        l.hour,
        l.day,
        l.isocalendar()[1],
        l.month,
        l.year,
        l.weekday(),
        )))
    time_df = time_df.drop_duplicates()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']].drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.timestamp_full,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Reads in all files in a filepath, processes them and inserts data in tables.
    
    Params 
    ------
    cur : psycopg2.extensions.cursor
    conn : psycopg2.extensions.connection
    filepath : str
    func : function
    
    returns
    -------
    None
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Main function to start processes.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()