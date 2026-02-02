from fastapi import APIRouter, HTTPException          # Se importa APIRouter para crear rutas HTTPException para manejar errores HTTP
from repositories.base_reposiry import *              # Se importa  todas las funciones del repositorio base (get, get_all, create, delete, etc.)

                                                      # tags=["Movies"] sirve para agruparlas en Swagger
router = APIRouter(prefix="/movies", tags=["Movies"]) # Creamos el router para películas prefix="/movies" significa que todas las rutas empiezan con /movies



@router.get("/{movie_id}")                             # GET /movies/{movie_id} para obtener una sola película
def get_movie(movie_id: int):
    movie = get("movies", movie_id)                    # Busca la película por ID en la lista "movies"
    if not movie:                                      # Si no existe la película, devolvemos error 404

        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )
    return movie                          # Si existe, devolvemos la película

# 
@router.get("/")                          # GET /movies/Sirve para obtener todas las películas
def get_movies():
    movies = get_all("movies")            # get_all devuelve un diccionario con todas las películas
    return list(movies.values())          # Convertimos los valores del diccionario en una lista

@router.post("/")                         # POST /movies/Sirve para crear una nueva película
def create_movie(movie: dict):
    create("movies", movie)               # Guardamos la película en la colección "movies"
    return {"mensaje": "Película creada"} # Devolvemos un mensaje de éxito

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _

# PUT /movies/{movie_id}
# Este endpoint está comentado porque aún no está implementado
# @router.put("/{movie_id}")
# def update_movie(movie_id: int, movie: dict):
#     pass

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _


@router.delete("/{movie_id}")                   # DELETE /movies/{movie_id} Sirve para eliminar una película
def delete_movie(movie_id: int):
    delete("movies", movie_id)                  # Eliminamos la película por ID
    return {"mensaje": "Película eliminada"}    # Devolvemos un mensaje de confirmación

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _