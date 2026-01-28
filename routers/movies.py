from fastapi import APIRouter, HTTPException
from repositories.base_reposiry import *

router = APIRouter(prefix="/movies", tags=["Movies"])


# Obtener detalles de una película por ID
@router.get("/{movie_id}")
def get_movie(movie_id: int):
    movie = get("movies", movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return movie

# Listar todas las películas
@router.get("/")
def list_movies():
    return list(get_all("movies").values())





