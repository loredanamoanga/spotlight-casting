import psycopg2
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from app import db
from datetime import datetime
db_id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
db_name = Column(String(180), unique=True)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Actor(db.Model):
    id = db_id
    name = db_name
    age = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    gender = Column(String(180), unique=True)

    def format(self):
        return {
            'id': self.id,
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

    def __repr__(self):
        return json.dumps(self.format())


class Movie(db.Model):
    id = db_id
    name = db_name
    release_date = Column(db.DateTime, nullable=False)

    def format(self):
        return {
            'id': self.id,
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

    def __repr__(self):
        return json.dumps(self.format())


class Masterpieces(db.Model):
    id = db_id,
    actor_id = Column('id', ForeignKey('actor.id'),
                      primary_key=True, autoincrement='ignore_fk')
    movie_id = Column('id', ForeignKey('movie.id'),
                      primary_key=True, autoincrement='ignore_fk')
    title = Column(String(80), unique=True)

    def format(self):
        return {
            'id': self.id,
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

    def __repr__(self):
        return json.dumps(self.format())
