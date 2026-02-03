from fastapi import APIRouter, HTTPException          # Se importa APIRouter para crear rutas HTTPException para manejar errores HTTP
from repositories.base_reposiry import *              # Se importa  todas las funciones del repositorio base (get, get_all, create, delete, etc.)

                                                     
router = APIRouter(prefix="/movies", tags=["Movies"]) # Creamos el router para películas prefix="/movies" significa que todas las rutas empiezan con /movies



@router.get("/{movie_id}")                             # GET /movies/{movie_id} para obtener una sola película
def get_movie(movie_id: int):
    movie = get("movies", movie_id)                   
    if not movie:                                     

        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )
    return movie                         

# 
@router.get("/")                          # GET /movies/Sirve para obtener todas las películas
def get_movies():
    movies = get_all("movies")          
    return list(movies.values())         

@router.post("/")                         # POST /movies/Sirve para crear una nueva película
def create_movie(movie: dict):
    create("movies", movie)               
    return {"mensaje": "Película creada"} 

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _

@router.put("/{movie_id}")                # Este endpoint busca una película por ID, verifica que exista, actualiza sus datos y guarda los cambios.
def update_movie(movie_id: int, new_data: dict): 
    movie = get("movies", movie_id)
    if movie is None:
        raise HTTPException(404, "Película no encontrada")
      
    movie.update(new_data)
    update("movies", movie_id, movie)
    return movie

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _


@router.delete("/{movie_id}")                   # DELETE /movies/{movie_id} Sirve para eliminar una película
def delete_movie(movie_id: int):
    delete("movies", movie_id)                  # Eliminamos la película por ID
    return {"mensaje": "Película eliminada"}    # Devolvemos un mensaje de confirmación

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
