# Joseph Messer
# CS 361
# 2025 February 2025

# Miroservice for rating system
# This microservice will allow users to rate a product and view the average rating of a product
# The microservice will also allow users to view the ratings of a product
# The microservice will communicate with the user microservice to get the user information via REST API


from flask import Flask, request, jsonify, redirect
import os
import requests
import pymongo
from bson.objectid import ObjectId

PORT = 5256
app = Flask(__name__)

# DataBase connection information (mongoDB)
# can be set as an environment variable or default to localhost (may need to change the port number)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/rating_database")
client = pymongo.MongoClient(MONGO_URI)
mongo = client.rating_database
ratings_collection = mongo["ratings"]


# Routes

@app.route('/ratings', methods=['POST'])
def add_rating():
    """Add a rating to a product"""
    data = request.json
    if not all(key in data for key in ['user_id', 'product_id', 'rating']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        data['rating'] = float(data['rating'])  # Ensure numeric rating
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid rating format'}), 400

    rating_id = ratings_collection.insert_one({
        'user_id': data['user_id'],
        'product_id': data['product_id'],
        'rating': data['rating']
    }).inserted_id

    return jsonify({'rating_id': str(rating_id)}), 201


@app.route('/ratings/<product_id>', methods=['GET'])
def get_rating(product_id):
    """Get the average rating for a product"""
    ratings = ratings_collection.find({'product_id': product_id})
    rating_sum = 0
    count = 0
    for rating in ratings:
        try:
            rating_sum += float(rating['rating'])
            count += 1
        except (TypeError, ValueError):
            return jsonify({'error': 'Invalid rating data'}), 500

    if count == 0:
        return jsonify({'average_rating': 0}), 200
    average_rating = rating_sum / count
    return jsonify({'average_rating': average_rating}), 200


@app.route('/ratings/<product_id>/user/<user_id>', methods=['GET'])
def get_user_rating(product_id, user_id):
    """Get a user's rating for a product"""
    rating = ratings_collection.find_one({'product_id': product_id, 'user_id': user_id})
    if rating is None:
        return jsonify({'rating': None}), 200
    return jsonify({'rating': rating['rating']}), 200


@app.route('/ratings/<product_id>/users', methods=['GET'])
def get_all_ratings(product_id):
    """Get all user ratings for a product"""
    ratings = ratings_collection.find({'product_id': product_id})
    user_ratings = {}
    for rating in ratings:
        user_ratings[rating['user_id']] = rating['rating']

    return jsonify(user_ratings), 200


@app.route('/ratings/<product_id>/users/<user_id>', methods=['DELETE'])
def delete_user_rating(product_id, user_id):
    # Delete a user rating
    result = ratings_collection.delete_one({'product_id': product_id, 'user_id': user_id})
    if result.deleted_count == 0:
        return jsonify({'error': 'Rating not found'}), 404
    return jsonify({'message': 'Rating deleted'}), 200


@app.route('/ratings/<product_id>/users/<user_id>', methods=['PUT'])
def update_user_rating(product_id, user_id):
    # Update a user rating
    data = request.json
    if 'rating' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        data['rating'] = float(data['rating'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid rating format'}), 400

    result = ratings_collection.update_one({'product_id': product_id, 'user_id': user_id}, {'$set': {'rating': data['rating']}})
    if result.modified_count == 0:
        return jsonify({'error': 'Rating not found'}), 404
    return jsonify({'message': 'Rating updated'}), 200


@app.route('/ratings/<product_id>/', methods=['DELETE'])
def delete_all_ratings(product_id):
    # Delete all ratings of a product
    ratings_collection.delete_many({'product_id': product_id})
    return jsonify({'message': 'All ratings deleted'}), 200


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
