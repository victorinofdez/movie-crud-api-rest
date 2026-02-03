
from fastapi import APIRouter, HTTPException       # Se Importa APIRouter para crear rutas y HTTPException para manejar errores HTTP
from repositories.base_reposiry import *

router = APIRouter(prefix="/users", tags=["Users"]) # Crea el router para usuarios prefix="/users" significa que todas las rutas empezarán con /users
                                                    
FAVORITES_KEY = "favoritas"                        

def get_user_or_404(user_id: int) -> dict:          # Función para buscar un usuario por ID Si no existe, devuelve un error 404
    user = get("users", user_id)                    
    if not user:                                     
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user                           

def get_movie_or_404(movie_id: int) -> dict:        # Función para buscar una película por ID Si no existe, devuelve un error 404
    movie = get("movies", movie_id)               
    if not movie:                                                               
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return                                                                     

@router.post("/{user_id}/favorites/{movie_id}")     # Endpoint para agregar una película a favoritas POST porque el usuario esta creando/modificando información
def add_favorite_movie(user_id: int, movie_id: int):
    user = get_user_or_404(user_id)                 # Verifica el usuario o lanzamos error si no existe    
    get_movie_or_404(movie_id)                  
    favorites = user.get(FAVORITES_KEY, [])    
    if movie_id in favorites:                  
        raise HTTPException(
            status_code=400,
            detail="La película ya está en favoritas"
        )

    favorites.append(movie_id)                          # Agrega la película a la lista de favoritas
    user[FAVORITES_KEY] = favorites                    
    update("users", user_id, user)                     
    return {"message": "Película agregada a favoritas"} 

@router.delete("/{user_id}/favorites/{movie_id}")       # Endpoint para eliminar una película de favoritas
def remove_favorite_movie(user_id: int, movie_id: int):
    
    user = get_user_or_404(user_id)                    
    favorites = user.get(FAVORITES_KEY, [])            
    if movie_id not in favorites:                       
        raise HTTPException(
            status_code=404,
            detail="La película no está en favoritas"
        )

    favorites.remove(movie_id)                              # Quita la película de la lista
    user[FAVORITES_KEY] = favorites                         # Actualiza la lista de favoritas del usuario
    update("users", user_id, user)                         
    return {"message": "Película eliminada de favoritas"}  

@router.get("/{user_id}/favorites")
def get_favorite_movies(user_id: int):          # Endpoint para listar todas las películas favoritas del usuario GET porque solo estamos consultando información
    user = get_user_or_404(user_id)            
    favorites_ids = user.get(FAVORITES_KEY, []) 
    favorite_movies = []                        # Lista donde guardaremos las películas completas

    for movie_id in favorites_ids:              # Recorre cada ID de película favorita
        movie = get("movies", movie_id)       
        if movie:                               # Si la película existe, la agrega a la lista
            favorite_movies.append(movie)

    return favorite_movies                      # Devuelve la lista de películas favoritas
