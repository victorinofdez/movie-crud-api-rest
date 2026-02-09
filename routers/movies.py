from fastapi import APIRouter, HTTPException          
from repositories.base_reposiry import *              
                                                     
router = APIRouter(prefix="/movies", tags=["Movies"]) 

@router.get("/{movie_id}")                             
def get_movie(movie_id: int):
    movie = get("movies", movie_id)                   
    if not movie:                                     

        raise HTTPException(
            status_code=404,
            detail="Película no encontrada"
        )
    return movie                         

@router.get("/")                        
def get_movies():
    movies = get_all("movies")          
    return list(movies.values())         

@router.post("/")                       
def create_movie(movie: dict):
    create("movies", movie)               
    return {"mensaje": "Película creada"} 

@router.put("/{movie_id}")               
def update_movie(movie_id: int, new_data: dict): 
    movie = get("movies", movie_id)
    if movie is None:
        raise HTTPException(404, "Película no encontrada")
      
    movie.update(new_data)
    update("movies", movie_id, movie)
    return movie

@router.delete("/{movie_id}") 
def delete_movie(movie_id: int):
    delete("movies", movie_id) 
    return {"mensaje": "Película eliminada"}
