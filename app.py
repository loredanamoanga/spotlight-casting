import logging

from dateutil.parser import parse
from flask import (
    Flask)
from flask import request, abort, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from auth import requires_auth, AuthError
from models import Actor, db, db_drop_and_create_all, Movie, setup_db

app = Flask(__name__)
# app.config["DEBUG"] = True
setup_db(app)
migrate = Migrate(app, db)
CORS(app)

db_drop_and_create_all()


# db.create_all()

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(jwt):
    actors = map(lambda actor: actor.format_actor(), Actor.query.all())
    if actors:
        return jsonify({"success": True, "actors": list(actors)})
    return "Actors not implemented"


@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(jwt):
    movies = map(lambda movie: movie.format_movie(), Movie.query.all())
    if movies:
        return jsonify({"success": True, "movies": list(movies)})
    return "Movies not implemented"


@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actor(jwt):
    body = request.get_json(force=True)
    req_name = body.get('name', None)
    req_age = body.get('age', None)
    req_gender = body.get('gender', None)

    try:
        actor = Actor(name=req_name, age=req_age, gender=req_gender)
        if actor is None:
            abort(404)

        actor.insert()
        actors = map(lambda actor_formatted: actor_formatted.format_actor(), Actor.query.all())
        if actors:
            return jsonify({"success": True, "actors": list(actors)})
        return "Actors not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movie(jwt):
    body = request.get_json(force=True)
    req_title = body.get('title', None)
    req_release_date = body.get('release_date', None)
    try:
        movie = Movie(title=req_title, release_date=parse(req_release_date))

        if movie is None:
            abort(404)

        movie.insert()

        movies = map(lambda movie_formatted: movie_formatted.format_movie(), Movie.query.all())

        if movies:
            return jsonify({"success": True, "movies": list(movies)})
        return "Movies not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actor(jwt, actor_id):
    body = request.get_json(force=True)
    if id is None:
        abort(404)
    req_name = body.get('name', None)
    req_age = body.get('age', None)
    req_gender = body.get('gender', None)
    try:
        specific_actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if specific_actor is None:
            abort(404)

        if req_name:
            specific_actor.name = req_name
        if req_age:
            specific_actor.age = req_age
        if req_gender:
            specific_actor.gender = req_gender
        specific_actor.update()

        actors = map(lambda actor: actor.format_actor(), Actor.query.all())

        if actors:
            return jsonify({"success": True, "actors": list(actors)})
        return "Actors not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movie(jwt, movie_id):
    body = request.get_json(force=True)
    if id is None:
        abort(404)
    req_title = body.get('title', None)
    req_release_date = body.get('release_date', None)
    try:
        specific_movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if specific_movie is None:
            abort(404)

        if req_title:
            specific_movie.title = req_title
        if req_release_date:
            specific_movie.release_date = parse(req_release_date)
        specific_movie.update()

        movies = map(lambda movie: movie.format_movie(), Movie.query.all())

        if movies:
            return jsonify({"success": True, "movies": list(movies)})
        return "Movies not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def remove_actor(jwt, actor_id):
    if actor_id is None:
        abort(404)
    try:
        specific_actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if specific_actor is None:
            abort(404)

        specific_actor.delete()

        actors = map(lambda actor: actor.format_actor(), Actor.query.all())

        if actors:
            return jsonify({"success": True, "actors": list(actors)})
        return "Actors not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def remove_movie(jwt, movie_id):
    if movie_id is None:
        abort(404)
    try:
        specific_movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if specific_movie is None:
            abort(404)

        specific_movie.delete()

        movies = map(lambda movie: movie.format_movie(), Movie.query.all())

        if movies:
            return jsonify({"success": True, "movies": list(movies)})
        return "Movies not implemented"
    except Exception as e:
        abort(422)
        logging.error('Error at %s', 'division', exc_info=e)


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Not allowed"
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
