from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from model import db, User, MovieStatus

movies = Blueprint('movies', __name__)

@movies.route('/api/movies/to-watch', methods=['POST'])
@jwt_required()
def add_to_watch():
    # Get the current user's identity
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    # Validate user existence
    if user is None:
        return jsonify({'msg': 'User not found.'}), 404

    # Get the movie ID from the request
    data = request.get_json()
    movie_id = data.get('movieId')

    # Validate movie ID existence (you can implement a Movie model query if needed)
    if movie_id is None:
        return jsonify({'msg': 'Movie ID is required.'}), 400

    # Add movie to the user's To Watch list
    status_entry = MovieStatus(user_id=user.id, movie_id=movie_id, status='To Watch')
    db.session.add(status_entry)
    db.session.commit()

    return jsonify({'msg': 'Movie added to To Watch list.'}), 201


@movies.route('/api/movies/watched', methods=['POST'])
@jwt_required()
def add_watched():
    # Get the current user's identity
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    # Validate user existence
    if user is None:
        return jsonify({'msg': 'User not found.'}), 404

    # Get the movie ID from the request
    data = request.get_json()
    movie_id = data.get('movieId')

    # Validate movie ID existence (you can implement a Movie model query if needed)
    if movie_id is None:
        return jsonify({'msg': 'Movie ID is required.'}), 400

    # Add movie to the user's Watched list
    status_entry = MovieStatus(user_id=user.id, movie_id=movie_id, status='Watched')
    db.session.add(status_entry)
    db.session.commit()

    return jsonify({'msg': 'Movie added to Watched list.'}), 201
