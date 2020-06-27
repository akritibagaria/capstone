import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth, AuthError
from models import Actors, Movies, setup_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    print("--------created app------------")
    CORS(app)
    database_path = os.environ['DATABASE_URL']
    setup_db(app, database_path)


    @app.route('/')
    def hello():
        return jsonify('Hello! Welcome to Casting Agency')

    @app.route('/actors', methods=['GET'])
    @requires_auth(permission='get:actors')
    def get_actors(jwt):
        try:
            actors = Actors.query.all()
            if not actors:
                abort(404)
            act_format = [act.format() for act in actors]
            result = {
                "success": True,
                "Actors": act_format
            }
            return jsonify(result)
        except Exception as error:
            raise error

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth(permission='delete:actors')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

            if not actor:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'delete': actor_id
            }), 200

        except Exception as error:
            raise error  

    @app.route('/actors', methods=['POST'])
    @requires_auth(permission='post:actors')
    def insert_actor(jwt):
        try:
            new_actor = request.get_json()
            name = new_actor.get('name')
            if name == '':
                abort(400)
            actor = Actors(name=new_actor['name'],age=new_actor['age'],email=new_actor['email'],salary=new_actor['salary'])
            actor.insert()

            return jsonify({
                'success': True,
            }), 201

        except Exception as error:
            raise error

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth(permission='patch:actors')
    def edit_actor(jwt, actor_id):
        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
            body = request.get_json()

            if not actor:
                abort(404)

            if 'name' in body:
                actor.name = body['name']
            if 'age' in body:
                actor.age = body['age']
            if 'email' in body:
                actor.email = body['email']
            if 'salary' in body:
                actor.salary = body['salary']

            actor.update()

            return jsonify({
                'success': True,
            }), 200
        except Exception as error:
            raise error

    @app.route('/movies', methods=['GET'])
    @requires_auth(permission='get:movies')
    def get_movies(jwt):
        try:
            movies = Movies.query.all()
            if not movies:
                abort(404)
            mov_format = [mov.format() for mov in movies]
            result = {
                "success": True,
                "Movies": mov_format
            }
            return jsonify(result)
        except Exception as error:
            raise error

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth(permission='delete:movies')
    def delete_movie(jwt, movie_id):
        try:
            movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
            if not movie:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200

        except Exception as error:
            raise error 


    @app.route('/movies', methods=['POST'])
    @requires_auth(permission='post:movies')
    def insert_movie(jwt):
        try:
            new_movie = request.get_json()
            name = new_movie.get('name')
            if name == '':
                abort(400)
            movie = Movies(name=new_movie['name'],length=new_movie['length'],genre=new_movie['genre'])
            movie.insert()

            return jsonify({
                'success': True,
            }), 201

        except Exception as error:
            raise error


    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth(permission='patch:movies')
    def update_Movies(jwt, movie_id):
        try:
            movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
            body = request.get_json()

            if not movie:
                abort(404)

            if 'name' in body:
                movie.name = body['name']
            if 'age' in body:
                movie.age = body['age']
            if 'email' in body:
                movie.email = body['email']
            if 'salary' in body:
                movie.salary = body['salary']

            movie.update()

            return jsonify({
                'success': True,
            }), 200
        except Exception as error:
            raise error

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
            return jsonify({
            'success': False,
            'error': 422,
            'message': error.description
        }), 422

    @app.errorhandler(400)
    def Bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad request"
        }), 400

    @app.errorhandler(401)
    def Bad_request(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "Unnauthorized"
        }), 401


    @app.errorhandler(500)
    def InternelError(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
        }), 500

    @app.errorhandler(AuthError)
    def unauthorized(error):
        print(error.status_code)
        print(error.error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)