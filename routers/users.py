from fastapi import APIRouter, HTTPException
from repositories.base_reposiry import *

router = APIRouter(prefix="/users", tags=["Users"])

# Agregar película a favoritas
@router.post("/{user_id}/favorites/{movie_id}")
def add_favorite_movie(user_id: int, movie_id: int):
    user = get("users", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    movie = get("movies", movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    favorites = user.get("favoritas", [])
    if movie_id in favorites:
        raise HTTPException(status_code=400, detail="La película ya está en favoritas")

    favorites.append(movie_id)
    user["favoritas"] = favorites
    update("users", user_id, user)
    return {"message": "Película agregada a favoritas"}

# Quitar película de favoritas
@router.delete("/{user_id}/favorites/{movie_id}")
def remove_favorite_movie(user_id: int, movie_id: int):
    user = get("users", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    favorites = user.get("favoritas", [])
    if movie_id not in favorites:
        raise HTTPException(status_code=404, detail="La película no está en favoritas")

    favorites.remove(movie_id)
    user["favoritas"] = favorites
    update("users", user_id, user)
    return {"message": "Película eliminada de favoritas"}

# Listar favoritas completas
@router.get("/{user_id}/favorites")
def get_favorite_movies(user_id: int):
    user = get("users", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    favorites_ids = user.get("favoritas", [])
    return [get("movies", movie_id) for movie_id in favorites_ids if get("movies", movie_id)]
