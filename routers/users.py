from fastapi import APIRouter, HTTPException
from repositories.base_reposiry import *

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

FAVORITES_KEY = "favoritas"



def get_user_or_404(user_id: int) -> dict:
    user = get("users", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


def get_movie_or_404(movie_id: int) -> dict:
    movie = get("movies", movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return movie


# CRUD USUARIOS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


@router.post("/")
def create_user(user: dict):
    user[FAVORITES_KEY] = []
    return insert("users", user)


@router.get("/")
def get_all_users():
    return get_all("users")


@router.get("/{user_id}")
def get_user(user_id: int):
    return get_user_or_404(user_id)


@router.put("/{user_id}")
def update_user(user_id: int, updated_user: dict):
    user = get_user_or_404(user_id)
    updated_user[FAVORITES_KEY] = user.get(FAVORITES_KEY, [])
    update("users", user_id, updated_user)
    return {"message": "Usuario actualizado"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    get_user_or_404(user_id)
    delete("users", user_id)
    return {"message": "Usuario eliminado"}


# FAVORITAS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


@router.post("/{user_id}/favorites/{movie_id}")
def add_favorite_movie(user_id: int, movie_id: int):
    user = get_user_or_404(user_id)
    get_movie_or_404(movie_id)

    favorites = user.get(FAVORITES_KEY, [])
    if movie_id in favorites:
        raise HTTPException(
            status_code=400,
            detail="La película ya está en favoritas"
        )

    favorites.append(movie_id)
    user[FAVORITES_KEY] = favorites
    update("users", user_id, user)

    return {"message": "Película agregada a favoritas"}


@router.delete("/{user_id}/favorites/{movie_id}")
def remove_favorite_movie(user_id: int, movie_id: int):
    user = get_user_or_404(user_id)

    favorites = user.get(FAVORITES_KEY, [])
    if movie_id not in favorites:
        raise HTTPException(
            status_code=404,
            detail="La película no está en favoritas"
        )

    favorites.remove(movie_id)
    user[FAVORITES_KEY] = favorites
    update("users", user_id, user)

    return {"message": "Película eliminada de favoritas"}


@router.get("/{user_id}/favorites")
def get_favorite_movies(user_id: int):
    user = get_user_or_404(user_id)
    favorites_ids = user.get(FAVORITES_KEY, [])

    favorite_movies = []
    for movie_id in favorites_ids:
        movie = get("movies", movie_id)
        if movie:
            favorite_movies.append(movie)

    return favorite_movies
