import requests
from app import PORT, BASE_URL

# BASE_URL = f"http://localhost:{PORT}"

# Test adding a rating
def test_add_rating():
    print("Testing add rating")
    data = {"user_id": "123", "product_id": "456", "rating": 4.5}
    response = requests.post(f"{BASE_URL}/ratings", json=data)
    print("Add Rating Response:", response.json())
    return response.json().get("rating_id")


# Test getting average rating
def test_get_average_rating(product_id):
    print("Testing get average rating")
    response = requests.get(f"{BASE_URL}/ratings/{product_id}")
    print("Get Average Rating Response:", response.json())


# Test getting user rating
def test_get_user_rating(product_id, user_id):
    print("Testing get user rating")
    response = requests.get(f"{BASE_URL}/ratings/{product_id}/user/{user_id}")
    print("Get User Rating Response:", response.json())


# Test updating user rating
def test_update_rating(product_id, user_id):
    print("Testing update user rating")
    data = {"rating": 5.0}
    response = requests.put(f"{BASE_URL}/ratings/{product_id}/users/{user_id}", json=data)
    print("Update Rating Response:", response.json())


# Test deleting user rating\
def test_delete_rating(product_id, user_id):
    print("Testing delete user rating")
    response = requests.delete(f"{BASE_URL}/ratings/{product_id}/users/{user_id}")
    print("Delete Rating Response:", response.json())


#  Test delete all user ratings
def test_delete_all_ratings(product_id):
    print("Testing delete all user ratings")
    response = requests.delete(f"{BASE_URL}/ratings/{product_id}/users")
    print("Delete All Ratings Response:", response.json())

# Test getting error for invalid rating data
def test_invalid_get_rating_data(product_id, user_id):
    print("Testing invalid rating data")
    response = requests.get(f"{BASE_URL}/ratings/{product_id}/user/{user_id}")
    print("Error Response:", response.json())


# Test getting error for adding invalid rating data
def test_invalid_add_rating_data(product_id, user_id):
    print("Testing invalid rating data")
    response = requests.get(f"{BASE_URL}/ratings/{product_id}/user/{user_id}")
    print("Error Response:", response, response.json())


if __name__ == "__main__":
    rating_id = test_add_rating()
    test_get_average_rating("456")
    test_get_user_rating("456", "123")
    test_update_rating("456", "123")
    test_delete_rating("456", "123")
    test_invalid_get_rating_data("467", "178")
    test_invalid_add_rating_data("234", "567")
    test_invalid_add_rating_data("234", "asdf")
