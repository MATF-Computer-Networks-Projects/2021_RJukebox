import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query


api_patch = Blueprint('api_patch', __name__)


@api_getter.route('/api/songs/name', methods=['PATCH'])
def change_song_name():
    return make_response("Song name successfully updated", 200)


@api_getter.route('/api/songs/artist', methods=['PATCH'])
def change_artist():
    return make_response("Artist successfully updated", 200)


@api_getter.route('/api/songs/genre', methods=['PATCH'])
def change_genre():
    return make_response("Genre successfully updated", 200)


@api_getter.route('/api/songs/link', methods=['PATCH'])
def change_yt_link():
    return make_response("Youtube link successfully updated", 200)