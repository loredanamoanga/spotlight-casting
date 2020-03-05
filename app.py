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

from models import Actor, db, db_drop_and_create_all

app = Flask(__name__)
# app.config.from_object('config.Development')
# app.config.from_object('config.Config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
print(os.environ.get('DATABASE_URL'))
db.init_app(app)
db_drop_and_create_all()

migrate = Migrate(app, db)
CORS(app)


@app.route('/actors', methods=['GET'])
def get_actors():
    actors = map(lambda drink: drink.short(), Actor.query.all())
    if actors:
        return jsonify({"success": True, "actors": list(actors)})
    return "Actors not implemented"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
