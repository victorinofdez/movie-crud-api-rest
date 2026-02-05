from fastapi import APIRouter, HTTPException       # Se Importa APIRouter para crear rutas y HTTPException para manejar errores HTTP
from repositories.base_reposiry import get, update, get_all, create, delete

router = APIRouter(prefix="/users", tags=["Users"]) # Crea el router para usuarios prefix="/users" significa que todas las rutas empezarán con /users
                                                    
FAVORITES_KEY = "favoritas"                        

def get_user_or_404(user_id: int) -> dict:          # Función para buscar un usuario por ID Si no existe, devuelve un error 404
    user = get("users", user_id)                    
    if not user:                                     
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user                           

def get_movie_or_404(movie_id: int) -> dict:        # Función para buscar una usuario por ID Si no existe, devuelve un error 404
    movie = get("movies", movie_id)               
    if not movie:                                                               
        raise HTTPException(status_code=404, detail="usuario no encontrada")
    return movie                                                                     


@router.post("/{user_id}/favorites/{movie_id}")     # Endpoint para agregar una usuario a favoritas POST porque el usuario esta creando/modificando información
def add_favorite_movie(user_id: int, movie_id: int):
    user = get_user_or_404(user_id)                 # Verifica el usuario o lanzamos error si no existe    
    get_movie_or_404(movie_id)                  
    favorites = user.get(FAVORITES_KEY, [])    
    if movie_id in favorites:                  
        raise HTTPException(
            status_code=400,
            detail="La usuario ya está en favoritas"
        )

    favorites.append(movie_id)                          # Agrega la usuario a la lista de favoritas
    user[FAVORITES_KEY] = favorites                    
    update("users", user_id, user)                     
    return {"message": "usuario agregada a favoritas"} 

@router.delete("/{user_id}/favorites/{movie_id}")       # Endpoint para eliminar una usuario de favoritas
def remove_favorite_movie(user_id: int, movie_id: int):
    
    user = get_user_or_404(user_id)                    
    favorites = user.get(FAVORITES_KEY, [])            

    if movie_id in favorites:                       
        favorites.remove(movie_id)                              # Quita la usuario de la lista
        user[FAVORITES_KEY] = favorites                         # Actualiza la lista de favoritas del usuario
        update("users", user_id, user)                         

    return {"message": "usuario eliminada de favoritas"}  

@router.get("/{user_id}/favorites")
def get_favorite_movies(user_id: int):          # Endpoint para listar todas las usuarios favoritas del usuario GET porque solo estamos consultando información
    user = get_user_or_404(user_id)            
    favorites_ids = user.get(FAVORITES_KEY, []) 

    favorite_movies = []                        # Lista donde guardaremos las usuarios completas

    for movie_id in favorites_ids:              # Recorre cada ID de usuario favorita
        movie = get("movies", movie_id)       
        if movie:                               # Si la usuario existe, la agrega a la lista                            

            favorite_movies.append(movie)

    return favorite_movies                      

#crear la funcion de crear obtener actualizar eliminar (post, get, put, delete)

@router.get("/")                          # GET /movies/Sirve para obtener todas las usuarios
def get_users():
    users = get_all("users")          
    return list(users.values())  

@router.post("/")                         # POST /movies/Sirve para crear una nueva usuario
def create_movie(users: dict):
    create("users", users)               
    return {"mensaje": "Usuario creado"} 

@router.put("/{user_id}")                # Este endpoint busca una usuario por ID, verifica que exista, actualiza sus datos y guarda los cambios.
def update_user(user_id: int, new_data: dict): 
    user = get("users", user_id)
    if user is None:
        raise HTTPException(404, "Usuario no encontrado")
      
    user.update(new_data)
    update("users", user_id, user)

    return user

@router.delete("/{user_id}")                   # DELETE /movies/{movie_id} Sirve para eliminar una usuario
def delete_user(user_id: int):
    delete("users", user_id)                  # Eliminamos la usuario por ID
    return {"mensaje": "Usuario eliminado"}    # Devolvemos un mensaje de confirmación
