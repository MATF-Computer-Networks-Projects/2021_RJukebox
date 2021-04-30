import json
import names
import random
import string
import logging
from utilities.hash_utilities import generate_hash


def create_users():
    try:
        data = {}
        data['users'] = []

        for i in range(10):
            data['users'].append({
            'user':names.get_full_name(),
            'password':generate_hash('12345')
            })

        with open("users.json", 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        logging.exception(f"Exception raised while creating users: {e}")
        raise e


def create_songs() -> list:
    try:
        logging.info("Creating test songs.")

        data = []
        yt_base = "https://www.youtube.com/watch?v="
        letters = string.ascii_letters
        genres = [ 'Rock', 'HipHop', 'Metal', 'Pop', 'RnB' ]

        for i in range(10):
            yt_link = yt_base + ''.join(random.choice(letters) for i in range(10))
            artist = names.get_first_name()
            song_name = names.get_last_name()
            genre = random.choice(genres)

            data.append({ 'song_name': song_name, 'artist': artist, 'genre': genre, 'yt_link': yt_link })

        return data
    except Exception as e:
        logging.exception(f"Error happened while creating test songs: {e}")
        return []
