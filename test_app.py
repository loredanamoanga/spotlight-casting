import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class SpotlightTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.database_name = "d4asref0qvp6aj"
        self.database_path = "postgresql://{}/{}".format(
            'postgres://zcetjyxewfhfoy:0ca05a93dc498d2dc27021a028ef122b7a416eade3e6a29dbb1d1b066d4b7caa@ec2-3-211-48-92.compute-1.amazonaws.com:5432/',
            self.database_name)

        self.new_actor = {
            "age": 24,
            "gender": "male",
            "name": "john"
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        res = self.client.get('/actors')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data.get('success'), True)
        self.assertTrue(len(data.get('categories')))




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
