from fastapi import APIRouter, HTTPException       
from repositories.base_reposiry import get, update, get_all, create, delete

router = APIRouter(prefix="/users", tags=["Users"]) 
                                                    
FAVORITES_KEY = "favoritas"                        

# ─────────────── Helpers ─────────────── #

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


# ─────────────── Favoritos ─────────────── #

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
    if movie_id not in favorites:  # ← cambio importante
        raise HTTPException(status_code=404, detail="Película no encontrada")
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


# ─────────────── CRUD Usuarios ─────────────── #

@router.get("/")                          
def get_users():
    users = get_all("users")          
    return list(users.values())  

@router.post("/")                         
def create_user(users: dict):  # ← cambié el nombre a create_user para claridad
    create("users", users)               
    return {"message": "Usuario creado"}  # ← cambio de "mensaje" a "message"

@router.put("/{user_id}")                
def update_user(user_id: int, new_data: dict): 
    user = get("users", user_id)
    if user is None:
        raise HTTPException(404, "Usuario no encontrado")
    user.update(new_data)
    update("users", user_id, user)
    return user

@router.delete("/{user_id}")                   
def delete_user(user_id: int):
    delete("users", user_id)                  
    return {"message": "Usuario eliminado"}  # ← cambio de "mensaje" a "message"
