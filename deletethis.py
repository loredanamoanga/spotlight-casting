def test_get_movies(self):
    res = self.client.get('/movies', headers=executive_producer)
    data = res.get_json()
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data.get('success'), True)
    self.assertTrue(len(data.get('movies')))


def test_get_wrong_endpoint(self):
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


def test_post_wrong_endpoint(self):
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