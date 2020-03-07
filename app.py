import logging
import os
from flask import Flask, request, abort, jsonify, json
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask import (
    Flask)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import Actor, db, db_drop_and_create_all, Movie

app = Flask(__name__)
# app.config.from_object('config.Development')
# app.config.from_object('config.Config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
print(os.environ.get('DATABASE_URL'))
db.init_app(app)
# db_drop_and_create_all()
# db.create_all()

migrate = Migrate(app, db)
CORS(app)


@app.route('/actors', methods=['GET'])
def get_actors():
    actors = map(lambda actor: actor.format(), Actor.query.all())
    if actors:
        return jsonify({"success": True, "actors": list(actors)})
    return "Actors not implemented"


@app.route('/movies', methods=['GET'])
def get_movies():
    movies = map(lambda actor: actor.format(), Movie.query.all())
    if movies:
        return jsonify({"success": True, "movies": list(movies)})
    return "Actors not implemented"


@app.route('/actors', methods=['POST'])
# @requires_auth('post:actors')
def create_actor():
    body = request.get_json(force=True)
    req_id = body["id"]
    req_name = body["name"]
    req_age = body["age"]
    req_gender = body["gender"]

    try:
        actor = Actor(id=req_id, name=req_name, age=req_age, gender=req_gender)
        if actor is None:
            abort(404)

        actor.insert()
        actors = map(lambda actor_formatted: actor.format(), Actor.query.all())
        if actors:
            return jsonify({"success": True, "actors": list(actors)})
        return "Actors not implemented"
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/movies', methods=['POST'])
# @requires_auth('post:movies')
def create_movie():
    body = request.get_json(force=True)
    req_id = body["id"]
    req_title = body["title"]
    req_release_date = body["release_date"]
    print(body, "body")
    try:
        movie = Movie(id=req_id, title=req_title, release_date=req_release_date)
        if movie is None:
            abort(404)

        movie.insert()
        movies = map(lambda movie_formatted: movie.format(), Movie.query.all())
        if movies:
            return jsonify({"success": True, "movies": list(movies)})
        return "Actors not implemented"
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)


# @app.route('/actors/<int:actor_id>', methods=['PATCH'])
# # @requires_auth('patch:actors')
# def edit_actor(actor_id):
#     body = request.get_json(force=True)
#     if id is None:
#         abort(404)
#     req_id = body["id"]
#     req_name = body["name"]
#     req_age = body["age"]
#     req_gender = body["gender"]
#     try:
#         specific_actor = Actor.query.filter(Actor.id == actor_id, Actor.id != '').one_or_none()
#
#         if specific_actor is None:
#             abort(404)
#         specific_actor.id = req_id
#         specific_actor.name = req_name
#         specific_actor.age = req_age
#         specific_actor.gender = req_gender
#         specific_actor.update()
#
#         actors = map(lambda actor: actor.long(), Actor.query.all())
#
#         if actors:
#             return jsonify({"success": True, "actors": list(actors)})
#         return "Actors not implemented"
#     except Exception as e:
#         logging.error('Error at %s', 'division', exc_info=e)
