import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
import json

SECRET_KEY = os.urandom(32)
project_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


# db_id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
db_string = Column(String(180), unique=True)
db_integer = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Actor(db.Model):
    name = db_string
    age = db_integer
    gender = Column(String(180), unique=True)

    def format(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()



class Movie(db.Model):
    title = db_string
    release_date = Column(DateTime, nullable=False)

    def format(self):
        return {
            'title': self.title,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()




class Masterpieces(db.Model):
    actor_id = Column('id', ForeignKey('actor.id'),
                      primary_key=True, autoincrement='ignore_fk')
    movie_id = Column('id', ForeignKey('movie.id'),
                      primary_key=True, autoincrement='ignore_fk')
    title = db_string

    def format(self):
        return {
            'actor_id': self.actor_id,
            'movie_id': self.movie_id,
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''delete()
      deletes a new model into a database
      the model must exist in the database
      '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
        update()
            updates a new model into a database
            the model must exist in the database
        '''

    def update(self):
        db.session.commit()


