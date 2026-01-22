import json

DATA_FILE = "data/data.json"

def read_file():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def write_file(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def create(movie_id, titulo, anio, sinopsis, director):
    data = read_file()

    if str(movie_id) in data["movies"]:
        print("La pelicula ya existe")
        return

    data["movies"][str(movie_id)] = {
        "id": movie_id,
        "titulo": titulo,
        "anio": anio,
        "sinopsis": sinopsis,
        "director": director
    }

    write_file(data)
    print("Pelicula creada")

def get(movie_id):
    data = read_file()
    return data["movies"].get(str(movie_id), "pelicula no encontrada")

def update(movie_id, titulo=None, anio=None, sinopsis=None, director=None):
    data = read_file()
    movie = data["movies"].get(str(movie_id))

    if not movie:
        print("pelicula no encontrada")
        return

    if titulo:
        movie["titulo"] = titulo
    if anio:
        movie["anio"] = anio
    if sinopsis:
        movie["sinopsis"] = sinopsis
    if director:
        movie[director] = director

    write_file(data)
    print("pelicula actualizado")

def delete(movie_id):
    data = read_file()

    if str(movie_id) not in data["movies"]:
        print("pelicula no encontrado")
        return

    del data["movies"][str(movie_id)]
    write_file(data)
    print("pelicula eliminado")

def get_all_movies():
    data = read_file()
    return data["movies"]


def main():
    pass 

if __name__ == "__main__":
    main()