import requests
from app import PORT, BASE_URL

# BASE_URL = f"http://localhost:{PORT}"

# Test adding a rating
def test_add_rating():
    data = {"user_id": "123", "product_id": "456", "rating": 4.5}
    response = requests.post(f"{BASE_URL}/ratings", json=data)
    print("Add Rating Response:", response.json())
    return response.json().get("rating_id")

# Test getting average rating
def test_get_average_rating(product_id):
    response = requests.get(f"{BASE_URL}/ratings/{product_id}")
    print("Get Average Rating Response:", response.json())

# Test getting user rating
def test_get_user_rating(product_id, user_id):
    response = requests.get(f"{BASE_URL}/ratings/{product_id}/user/{user_id}")
    print("Get User Rating Response:", response.json())

# Test updating user rating
def test_update_rating(product_id, user_id):
    data = {"rating": 5.0}
    response = requests.put(f"{BASE_URL}/ratings/{product_id}/users/{user_id}", json=data)
    print("Update Rating Response:", response.json())

# Test deleting user rating
def test_delete_rating(product_id, user_id):
    response = requests.delete(f"{BASE_URL}/ratings/{product_id}/users/{user_id}")
    print("Delete Rating Response:", response.json())

if __name__ == "__main__":
    rating_id = test_add_rating()
    test_get_average_rating("456")
    test_get_user_rating("456", "123")
    test_update_rating("456", "123")
    test_delete_rating("456", "123")
