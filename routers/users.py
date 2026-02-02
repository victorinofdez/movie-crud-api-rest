
from fastapi import APIRouter, HTTPException       # Se Importa APIRouter para crear rutas y HTTPException para manejar errores HTTP
from repositories.base_reposiry import *

router = APIRouter(prefix="/users", tags=["Users"]) # Crea el router para usuarios prefix="/users" significa que todas las rutas empezarán con /users
                                                    # tags=["Users"] sirve para agruparlas en la documentación (Swagger)
FAVORITES_KEY = "favoritas"                         # Constante que guarda la clave donde se guardan las películas favoritas

def get_user_or_404(user_id: int) -> dict:          # Función para buscar un usuario por ID Si no existe, devuelve un error 404
    user = get("users", user_id)                    # Busca el usuario en la colección "users"
    if not user:                                     # Si no existe el usuario, lanzamos un error HTTP 404
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user                            # Si existe, lo devolvemos

def get_movie_or_404(movie_id: int) -> dict:        # Función para buscar una película por ID Si no existe, devuelve un error 404
    movie = get("movies", movie_id)                 # Busca la película en la colección "movies"
    if not movie:                                                               # Si no existe la película, lanzamos un error HTTP 404
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return                                                                      # Si existe, la devolvemos

@router.post("/{user_id}/favorites/{movie_id}")     # Endpoint para agregar una película a favoritas POST porque el usuario esta creando/modificando información
def add_favorite_movie(user_id: int, movie_id: int):
    user = get_user_or_404(user_id)             # Verifica el usuario o lanzamos error si no existe    
    get_movie_or_404(movie_id)                  # Verifica que la película exista
    favorites = user.get(FAVORITES_KEY, [])     # Obtiene la lista de favoritas del usuarios Si no existe, usamos una lista vacía
    if movie_id in favorites:                   # Verifica si la película ya está en favoritas
        raise HTTPException(
            status_code=400,
            detail="La película ya está en favoritas"
        )

    favorites.append(movie_id)                          # Agrega la película a la lista de favoritas
    user[FAVORITES_KEY] = favorites                     # Actualiza la lista de favoritas en el usuario
    update("users", user_id, user)                      # Guarda los cambios del usuario
    return {"message": "Película agregada a favoritas"} # Devuelve un mensaje de confirmacíon

@router.delete("/{user_id}/favorites/{movie_id}")       # Endpoint para eliminar una película de favoritas
def remove_favorite_movie(user_id: int, movie_id: int): # DELETE porque estamos eliminando información
    
    user = get_user_or_404(user_id)                     # Obtiene el usuario o lanzamos error si no existe
    favorites = user.get(FAVORITES_KEY, [])             # Obtiene la lista de favoritas del usuario
    if movie_id not in favorites:                       # Verifica si la película NO está en favoritas
        raise HTTPException(
            status_code=404,
            detail="La película no está en favoritas"
        )

    favorites.remove(movie_id)                              # Quita la película de la lista
    user[FAVORITES_KEY] = favorites                         # Actualiza la lista de favoritas del usuario
    update("users", user_id, user)                          # Guarda los cambios en el usuario
    return {"message": "Película eliminada de favoritas"}   # Devuelves un mensaje de confirmacíon

@router.get("/{user_id}/favorites")
def get_favorite_movies(user_id: int):          # Endpoint para listar todas las películas favoritas del usuario GET porque solo estamos consultando información
    user = get_user_or_404(user_id)             # Obtiene el usuario o lanzamos error si no existe
    favorites_ids = user.get(FAVORITES_KEY, []) # Obtiene los IDs de las películas favoritas
    favorite_movies = []                        # Lista donde guardaremos las películas completas

    for movie_id in favorites_ids:              # Recorre cada ID de película favorita
        movie = get("movies", movie_id)         # Busca la película por ID
        if movie:                               # Si la película existe, la agrega a la lista
            favorite_movies.append(movie)

    return favorite_movies                      # Devuelve la lista de películas favoritas
