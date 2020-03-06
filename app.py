import os
from flask import Flask, request, abort, jsonify, json, logging
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
db.create_all()

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
    req_name = body.get('name', None)
    req_age = body.get('age', None)
    req_gender = body.get('gender', None)
    print(body)

    try:
        actor = Actor(id=req_id, name=req_name, age=req_age, gender=req_gender)
        if actor is None:
            abort(404)

        actor.insert()
        actors = map(lambda actor: actor.format(), Actor.query.all())

        if actors:
            return jsonify({"success": True, "actors": list(actors)})
        return "Actors not implemented"
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
