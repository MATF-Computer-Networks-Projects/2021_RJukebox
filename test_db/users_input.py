import json
import logging
import mysql.connector
from dotenv import dotenv_values

import defaults
from create_test_data import create_users, create_songs
from db_templates.load_template import load_db_template
from utilities.db_util import check_if_table_exists

def input_user(mydb, cursor):
    if check_if_table_exists(cursor,"users"):
        create_users()

        with open("users.json") as json_file:
            data = json.load(json_file)

        for d in data['users']:
            cursor.execute("INSERT INTO users (user,password) VALUES (%s,%s)",(d['user'], d['password']))

        mydb.commit()
        logging.info(f"Users added.")
        return True
    else:
        logging.error(f"Users table doesn't exist.")
        return False


def input_songs(my_db, cursor) -> bool:
    if not check_if_table_exists(cursor, 'songs'):
        logging.warning("Table [songs] doesn't exist. Can't input users.")
        return False
    
    template = load_db_template(defaults.song_insert)
    
    songs = create_songs()
    for song in songs:
        insert_query = template.render(song_name=song['song_name'], artist=song['artist'], genre=song['genre'], yt_link=song['yt_link'])
        cursor.execute(insert_query)
    
    my_db.commit()
    logging.info("Songs successfully added to DB.")

    return True
