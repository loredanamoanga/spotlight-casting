# Spotlight casting agency

## Live application
The application is hosted on heroku under the url:

[https://spotlight-casting.herokuapp.com/](https://spotlight-casting.herokuapp.com/)

## Learning purposes

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 
No current frontend available

## Models:

Movies with attributes title and release date
Actors with attributes name, age and gender

##  Roles:
* Casting Assistant
    * Can view actors and movies
* Casting Director
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies
* Executive Producer
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database
    
## Testing
Test the following endpoints with [Postman](https://getpostman.com) by importing and running [spotlight-casting.postman_collection.json](spotlight-casting.postman_collection.json)
The collection has added the proper authorizations tokens.


There is also a local backend testing which can be run in the following stps:
* implement and activate the virtual environment,
* install the [requirements.txt ](requirements.txt)
* run python test_app.py;     

## Endpoints:

For all the endpoints you need to use a valid access token in the request headers as well as Content-Type to use the endpoints.
These can be found in the [headers.py](headers.py) document

### Actors
```GET /actors ```

Fetches a list of all actors

Response:
~~~
{
    "actors": [
        {
           "age": 24,
           "gender": "male",
           "id": 1,
           "name": "John Smith"
        }
    ],
    "success": true
}

~~~

```POST /actors ```
Adds a new actor and returns an updated list of all actors and the success value

Body:

~~~
{
    "age": 25,
    "gender": "Female",
    "name": "Jane Doe"
}
~~~

Response:

~~~
{
  "actors": [
    {
      "age": 24,
      "gender": "male",
      "id": 1,
      "name": "John Smith"
    },
    {
      "age": 25,
      "gender": "female",
      "id": 2,
      "name": "Jane Doe"
    }
  ],
  "success": true
}

~~~


```PATCH /actors/1 ```
Edits a specific id actor and returns an updated list of all actors and the success value

Body:

~~~
{
    "name": "John Doe"
}
~~~

Response:

~~~
{
  "actors": [
    {
      "age": 24,
      "gender": "male",
      "id": 1,
      "name": "John Doe"
    },
    {
      "age": 25,
      "gender": "female",
      "id": 2,
      "name": "Jane Doe"
    }
  ],
  "success": true
}

~~~

```DELETE /actors/1 ```
Removes a specific id actor and returns an updated list of all remaining actors and the success value

Response:

~~~
{
  "actors": [
    {
      "age": 25,
      "gender": "female",
      "id": 2,
      "name": "Jane Doe"
    }
  ],
  "success": true
}

~~~
### Movies
```GET /movies ```
Fetches a list of all movies

Response:
~~~
{
  "movies": [
    {
      "id": 1,
      "release_date": "2018-03-29 00:00:00",
      "title": "The tornado"
    }
  ],
  "success": true
}
~~~


```POST /movies ```
Adds a new movie and returns an updated list of all movies and the success value

Body:

~~~
{
    "title": "The tornado",
    "release_date": "2018-03-29"
}
~~~

Response:

~~~
{
  "movies": [
    {
      "id": 1,
      "release_date": "2016-03-02 00:00:00",
      "title": "The cottage"
    },
    {
      "id": 2,
      "release_date": "2018-03-29 00:00:00",
      "title": "The tornado"
    }
  ],
  "success": true
}
~~~


```PATCH /movies/1 ```
Edits a specific id movie and returns an updated list of all movies and the success value

Body:

~~~
{
    "title": "The cottage 2",
}
~~~

Response:

~~~
{
  "movies": [
    {
      "id": 1,
      "release_date": "2016-03-02 00:00:00",
      "title": "The cottage 2"
    },
    {
      "id": 2,
      "release_date": "2018-03-29 00:00:00",
      "title": "The tornado"
    }
  ],
  "success": true
}
~~~

```DELETE /movies/1 ```
Removes a specific id movie and returns an updated list of all remaining movies and the success value

Response:

~~~
{
  "movies": [
    {
      "id": 2,
      "release_date": "2018-03-29 00:00:00",
      "title": "The tornado"
    }
  ],
  "success": true
}
~~~
