import json
import unittest
from flask_sqlalchemy import SQLAlchemy
import app
from headers import executive_producer, casting_assistant
from models import Actor, Movie, db_drop_and_create_all


class SpotlightTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app.app
        self.app.testing = True
        self.client = self.app.test_client()

        self.initial_actor = {
            "age": 25,
            "gender": "female",
            "name": "Jane"
        }

        self.new_actor = {
            "age": 24,
            "gender": "male",
            "name": "John"
        }

        self.detail_actor = {
            "name": "Julia"
        }
        self.initial_movie = {
            "title": "The tornado",
            "release_date": "2018-03-29"
        }

        self.new_movie = {
            "title": "The Cottage",
            "release_date": "2016-03-19"
        }

        self.detail_movie = {
            "title": "The Cottage"
        }

        self.client.post("/actors",
                         headers=executive_producer,
                         content_type="application/json",
                         data=json.dumps(self.initial_actor))

        self.client.post("/movies",
                         headers=executive_producer,
                         content_type="application/json",
                         data=json.dumps(self.initial_movie))

    def tearDown(self):
        """Executed after reach test"""
        db_drop_and_create_all()
        pass
    def test_post_without_proper_credentials(self):
        res = self.client.post("/actors",
                               headers=casting_assistant,
                               content_type="application/json",
                               data=json.dumps(self.new_actor))
        self.assertEqual(res.status_code, 401)


    def test_get_actors(self):
        res = self.client.get('/actors', headers=executive_producer)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data.get('success'), True)
        self.assertTrue(len(data.get('actors')))

    def test_get_actors_inexistent_endpoint(self):
        res = self.client.get('/aactors', headers=executive_producer)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data.get('success'), False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], 'Not found')

    def test_post_actor(self):
        res = self.client.post("/actors",
                               headers=executive_producer,
                               content_type="application/json",
                               data=json.dumps(self.new_actor))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_actor_inexistent_endpoint(self):
        res = self.client.post("/actors/1",
                               headers=executive_producer,
                               content_type="application/json",
                               data=json.dumps(self.new_actor))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Not allowed')

    def test_patch_actor(self):
        res = self.client.patch("/actors/1",
                                headers=executive_producer,
                                content_type="application/json",
                                data=json.dumps(self.detail_actor))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor_inexistent_id(self):
        res = self.client.patch("/actors/123",
                                headers=executive_producer,
                                content_type="application/json",
                                data=json.dumps(self.detail_actor))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Unprocessable')

    def test_delete_actor(self):
        res = self.client.delete("/actors/1",
                                 headers=executive_producer,
                                 content_type="application/json",
                                 data=json.dumps(self.detail_actor))
        data = res.get_json()
        actor = Actor.query.filter(Actor.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(bool(len(data['actors']) == 0))
        self.assertEqual(actor, None)

    def test_delete_actor_inexistent_id(self):
        res = self.client.delete("/actors/123",
                                 headers=executive_producer,
                                 content_type="application/json",
                                 data=json.dumps(self.detail_actor))
        data = res.get_json()
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'Unprocessable')

    def test_get_movies(self):
        res = self.client.get('/movies', headers=executive_producer)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data.get('success'), True)
        self.assertTrue(len(data.get('movies')))


    def test_get_movies_inexistent_endpoint(self):
        res = self.client.get('/mmovies', headers=executive_producer)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data.get('success'), False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], 'Not found')


    def test_post_movie(self):
        res = self.client.post("/movies",
                               headers=executive_producer,
                               content_type="application/json",
                               data=json.dumps(self.new_movie))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_post_movie_inexistent_endpoint(self):
        res = self.client.post("/movies/1",
                               headers=executive_producer,
                               content_type="application/json",
                               data=json.dumps(self.new_movie))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Not allowed')


    def test_patch_movie(self):
        res = self.client.patch("/movies/1",
                                headers=executive_producer,
                                content_type="application/json",
                                data=json.dumps(self.detail_movie))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_patch_movie_inexistent_id(self):
        res = self.client.patch("/movies/123",
                                headers=executive_producer,
                                content_type="application/json",
                                data=json.dumps(self.detail_movie))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'Unprocessable')


    def test_delete_movie(self):
        res = self.client.delete("/movies/1",
                                 headers=executive_producer,
                                 content_type="application/json",
                                 data=json.dumps(self.detail_movie))
        data = res.get_json()
        movie = Movie.query.filter(Movie.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(bool(len(data['movies']) == 0))
        self.assertEqual(movie, None)


    def test_delete_movie_inexistent_id(self):
        res = self.client.delete("/movies/123",
                                 headers=executive_producer,
                                 content_type="application/json",
                                 data=json.dumps(self.detail_movie))
        data = res.get_json()
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'Unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
