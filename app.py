import os
from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask import (
    Flask)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import Actor

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
print('hello there')
CORS(app)


@app.route('/actors', methods=['GET'])
def get_actors():
    actors = map(lambda drink: drink.short(), Actor.query.all())
    if actors:
        return jsonify({"success": True, "actors": list(actors)})
    return "Actors not implemented"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
