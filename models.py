import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import json

SECRET_KEY = os.urandom(32)
project_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.environ.get('DATABASE_URL')
db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                            'sqlite:///' + os.path.join(basedir, 'test/spotlight.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    age = Column(Integer())
    gender = Column(String)

    def format_actor(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime())

    def format_movie(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": str(self.release_date)
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())

# class Masterpieces(db.Model):
#     __tablename__ = 'masterpieces'
#     id = Column(Integer(), autoincrement=True, primary_key=True),
#     actor_id = Column("id", ForeignKey('actor.id'),
#                       primary_key=True, autoincrement='ignore_fk')
#     movie_id = Column("id", ForeignKey('movie.id'),
#                       primary_key=True, autoincrement='ignore_fk')
#     title = Column(String)
#
#     def format(self):
#         return {
#             "id": self.id,
#             'actor_id': self.actor_id,
#             'movie_id': self.movie_id,

#         }
#
#     '''
#     insert()
#         inserts a new model into a database
#         the model must have a unique name
#         the model must have a unique id or null id
#     '''
#
#     def insert(self):
#         db.session.add(self)
#         db.session.commit()
#
#     '''delete()
#       deletes a new model into a database
#       the model must exist in the database
#       '''
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#
#     '''
#         update()
#             updates a new model into a database
#             the model must exist in the database
#         '''
#
#     def update(self):
#         db.session.commit()
