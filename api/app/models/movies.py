class Movie:
    def __init__(self, 
                titulo: str, 
                anio: int, 
                sinopsis: str, 
                director: str
        ):
        
        self.titulo = titulo
        self.anio = anio
        self.sinopsis = sinopsis
        self.director = director
'''

from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    titulo: str
    anio: int
    director: str
    sinopsis: str
'''