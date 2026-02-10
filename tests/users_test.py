import pytest                                           # Importa pytest para poder ejecutar los tests
from fastapi import FastAPI                             # Importa FastAPI 
from fastapi.testclient import TestClient               # Importa TestClient
from routers.users import router                        # Importa el router


# Se crea FastAPI Test _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


app = FastAPI()                                         # Crea una app FastAPI
app.include_router(router)                              # Incluye el router de usuarios
client = TestClient(app)                                # Crea el cliente de prueba


users_test = {                                          # Diccionario que simula usuarios
    1: {
        "id": 1,
        "name": "Juan",
        "favoritas": []
    }
}

test_movie = {                                         # Diccionario que simula películas
    10: {
        "id": 10,
        "title": "Matrix"
    }
}

# 🔹 CAMBIO: renombradas para que pytest NO las considere tests
def _test_get(lista, item_id=None):                      # función get del repositorio
    if lista == "users":                                # Si se pide la lista users
        return users_test.get(item_id)                  # Devuelve el usuario si existe
    if lista == "movies":                               # Si se pide la lista movies
        return test_movie.get(item_id)                 # Devuelve la película si existe
    return None                                         # Si no existe, devolvemos None


def _test_update(lista, item_id, data):                  # Simula la función update del repositorio
    if lista == "users":                                # Si se actualiza un usuario
        users_test[item_id] = data                      # Guardamos los cambios en el diccionario


# TEST: Agregar película a favoritas correctamente _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_add_favorite_movie(monkeypatch):                     # Test para agregar película a favoritas
    monkeypatch.setattr("routers.users.get", _test_get)        # Reemplaza get por _test_get
    monkeypatch.setattr("routers.users.update", _test_update)  # Reemplaza update por _test_update

    response = client.post("/users/1/favorites/10")           # Hace la petición POST

    assert response.status_code == 200                        # Verifica que el status sea 200
    assert response.json()["message"] == "Película agregada a favoritas"  # Verifica el mensaje
    assert 10 in users_test[1]["favoritas"]                   # Verifica que la película esté en favoritas

# TEST: Usuario no existe _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_add_favorite_user_not_found(monkeypatch):      # Test cuando el usuario no existe
    monkeypatch.setattr("routers.users.get", _test_get)  # Reemplaza get por _test_get

    response = client.post("/users/999/favorites/10")   # Usuario inexistente

    assert response.status_code == 404                  # Verifica el status 404
    assert response.json()["detail"] == "Usuario no encontrado"  # Verifica el mensaje


# TEST: Película no existe _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_add_favorite_movie_not_found(monkeypatch):     # Test cuando la película no existe
    monkeypatch.setattr("routers.users.get", _test_get)  # Reemplaza get por _test_get

    response = client.post("/users/1/favorites/999")    # Película inexistente

    assert response.status_code == 404                  # Verificamos el status 404
    assert response.json()["detail"] == "Película no encontrada"  # Verificamos el mensaje


# TEST: Película ya está en favoritas _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_add_favorite_already_exists(monkeypatch):      # Test cuando la película ya está en favoritas
    users_test[1]["favoritas"] = [10]                   # Agregamos la película previamente

    monkeypatch.setattr("routers.users.get", _test_get)  # Reemplazamos get por _test_get

    response = client.post("/users/1/favorites/10")     # Intentamos agregarla de nuevo

    assert response.status_code == 400                  # Verificamos el status 400
    assert response.json()["detail"] == "La película ya está en favoritas"  # Verificamos el mensaje

# TEST: Eliminar película de favoritas _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_remove_favorite_movie(monkeypatch):            # Test para eliminar película de favoritas
    users_test[1]["favoritas"] = [10]                   # Dejamos la película en favoritas

    monkeypatch.setattr("routers.users.get", _test_get)        # Reemplaza get por _test_get
    monkeypatch.setattr("routers.users.update", _test_update)  # Reemplaza update por _test_update

    response = client.delete("/users/1/favorites/10")   # Hacemos la petición DELETE

    assert response.status_code == 200                  # Verifica el status 200
    assert response.json()["message"] == "Película eliminada de favoritas"  # Verificamos el mensaje
    assert 10 not in users_test[1]["favoritas"]         # Verifica que se eliminó


# TEST: Listar películas favoritas _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_get_favorite_movies(monkeypatch):              # Test para listar películas favoritas
    users_test[1]["favoritas"] = [10]                   # Dejamos una película en favoritas

    monkeypatch.setattr("routers.users.get", _test_get)  # Reemplaza get por _test_get

    response = client.get("/users/1/favorites")         # Hace la petición GET

    assert response.status_code == 200                  # Verificamos el status 200
    assert response.json() == [test_movie[10]]         # Verificamos la lista de películas
