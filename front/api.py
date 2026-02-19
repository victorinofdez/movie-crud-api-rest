import requests
from config import BASE_URL


def login(username, password):
    return requests.post(
        f"{BASE_URL}/login",
        data={
            "username": username,
            "password": password
        }
    )


# ---------------- MOVIES ----------------

def get_movies(token):
    return requests.get(
        f"{BASE_URL}/movies/",
        headers={"Authorization": f"Bearer {token}"}
    )


def create_movie(token, movie_data):
    return requests.post(
        f"{BASE_URL}/movies/",
        json=movie_data,
        headers={"Authorization": f"Bearer {token}"}
    )


def delete_movie(token, movie_id):
    return requests.delete(
        f"{BASE_URL}/movies/{movie_id}",
        headers={"Authorization": f"Bearer {token}"}
    )


# ---------------- USERS ----------------

def get_users(token):
    return requests.get(
        f"{BASE_URL}/users/",
        headers={"Authorization": f"Bearer {token}"}
    )
