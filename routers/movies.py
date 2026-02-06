from fastapi import APIRouter, HTTPException
from repositories.base_reposiry import *

# El router para películas. prefix="/movies" significa que todas las rutas empiezan con /movies
router = APIRouter(prefix="/movies", tags=["Movies"])


# GET /movies/{movie_id} Obtiene detalles de una película por ID
@router.get("/{movie_id}")
def get_movie(movie_id: int):
    movie = get("movies", movie_id)
    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )
    return movie

# GET /movies Sirve para obtener todas las películas 
@router.get("/")
def get_movies():
    movies = get_all("movies")
    return list(movies.values())


# POST /movies Sirve para crear una nueva película
@router.post("/")
def create_movie(movie: dict):
    insert("movies", movie)
    return {"mensaje": "Película creada"}


# PUT /movies/{movie_id} Este endpoint busca una película por ID, verifica que exista.
# actualiza sus datos y guarda los cambios
@router.put("/{movie_id}")
def update_movie(movie_id: int, new_data: dict):
    movie = get("movies", movie_id)
    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )

    movie.update(new_data)
    update("movies", movie_id, movie)
    return movie


# DELETE /movies/{movie_id} Sirve para eliminar una película
@router.delete("/{movie_id}")
def delete_movie(movie_id: int):
    movie = get("movies", movie_id)
    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )

    delete("movies", movie_id)
    return {"mensaje": "Película eliminada"}
