Flask Ratings Microservice
  This microservice provides a RESTful API for tracking ratings and basic statistics for images or products. 
  It stores user ratings in a MongoDB database and allows CRUD operations on ratings.

Prerequisites
  Python 3.8+
  MongoDB (local or remote instance)

Setup and Running the Microservice

1. Clone the Repository
    git clone https://github.com/JosephMesser13/CS361_rating_microservice/tree/main
    cd <repository-folder>

2. Create a Virtual Environment (Recommended)
    python -m venv venv
    source venv/bin/activate

3. Install Dependencies
    pip install -r requirements.txt

4. Start MongoDB (If Running Locally)
   Ensure MongoDB is running locally:
     mongod --dbpath /your/db/path

5. Configure Environment Variables
  Create a .env file or set environment variables:
    export MONGO_URI = mongodb://localhost:27017/rating_database # You may need to change the connection string 
    export FLASK_ENV = development
    export PORT=5256

6. Run the Flask App
    python app.py

The service should now be running at http://localhost:5256


Testing the Microservice

Use cURL to test endpoints.
  Add a Rating
    curl -X POST "http://localhost:5256/ratings" -H "Content-Type: application/json" -d '{"user_id": "123", "product_id": "456", "rating": 4.5}'
  
  Get Average Rating for a Product
    curl -X GET "http://localhost:5256/ratings/456"
  
  Get a User’s Rating
    curl -X GET "http://localhost:5256/ratings/456/user/123"
  
  Update a User's Rating
    curl -X PUT "http://localhost:5256/ratings/456/users/123" -H "Content-Type: application/json" -d '{"rating": 5.0}'
  
  Delete a User’s Rating
    curl -X DELETE "http://localhost:5256/ratings/456/users/123"
  
  Delete All Ratings for a Product
    curl -X DELETE "http://localhost:5256/ratings/456"


Connecting to Another Application

  Backend Integration
    import requests
    response = requests.get("http://localhost:5256/ratings/456")
    print(response.json())

  Frontend Integration
    

