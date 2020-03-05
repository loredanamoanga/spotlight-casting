import os
from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import dateutil.parser
import babel
from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from sqlalchemy.exc import SQLAlchemyError
# from forms import *
from config import Config
from flask_migrate import Migrate

from models import Actor

app = Flask(__name__)
app.config.from_object(Config)
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
