import os
import json
import pytest
from persistencia import persistencia as p

# ------------------------
# Fixtures
# ------------------------

@pytest.fixture
def tmp_json_file(tmp_path):
    """Archivo temporal para pruebas."""
    file_path = tmp_path / "data_tmp.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({}, f)
    return str(file_path)


@pytest.fixture
def sample_data(tmp_json_file):
    """Datos iniciales para probar CRUD y búsquedas."""
    data = {
        "movies": {
            "1": {"id": 1, "titulo": "Matrix", "anio": 1999, "director": "Lana Wachowski", "sinopsis": "La realidad no es lo que parece."},
            "2": {"id": 2, "titulo": "Inception", "anio": 2010, "director": "Christopher Nolan", "sinopsis": "Robar secretos dentro de los sueños."}
        }
    }
    p.write_file(tmp_json_file, data)
    return tmp_json_file


# ------------------------
# Tests CRUD
# ------------------------

def test_create_ok(sample_data):
    movie = {"id": 3, "titulo": "El Padrino", "anio": 1972}
    assert p.create(sample_data, "movies", 3, movie) is True
    assert p.get(sample_data, "movies", 3)["titulo"] == "El Padrino"


def test_create_id_duplicado_lanza(sample_data):
    movie = {"id": 1, "titulo": "Duplicado"}
    with pytest.raises(ValueError):
        p.create(sample_data, "movies", 1, movie)


def test_get_devuelve_none_si_no_existe(sample_data):
    assert p.get(sample_data, "movies", 999) is None


def test_get_all_devuelve_diccionario(sample_data):
    movies = p.get_all(sample_data, "movies")
    assert isinstance(movies, dict)
    assert len(movies) == 2


def test_update_ok(sample_data):
    updated = {"id": 2, "titulo": "Inception Editada"}
    assert p.update(sample_data, "movies", 2, updated) is True
    assert p.get(sample_data, "movies", 2)["titulo"] == "Inception Editada"


def test_update_no_existe_lanza(sample_data):
    with pytest.raises(ValueError):
        p.update(sample_data, "movies", 999, {"id": 999})


def test_delete_ok(sample_data):
    assert p.delete(sample_data, "movies", 1) is True
    assert p.get(sample_data, "movies", 1) is None


def test_delete_no_existe_lanza(sample_data):
    with pytest.raises(ValueError):
        p.delete(sample_data, "movies", 999)


# ------------------------
# Tests búsquedas
# ------------------------

def test_get_by_field_encuentra(sample_data):
    movie = p.get_by_field(sample_data, "movies", "titulo", "Matrix")
    assert movie["id"] == 1


def test_get_by_field_no_encuentra(sample_data):
    assert p.get_by_field(sample_data, "movies", "titulo", "No Existe") is None


def test_search_by_field_contains_devuelve_lista(sample_data):
    results = p.search_by_field_contains(sample_data, "movies", "titulo", "in")
    assert isinstance(results, list)
    assert len(results) >= 1


def test_search_by_field_contains_vacio(sample_data):
    results = p.search_by_field_contains(sample_data, "movies", "titulo", "zzzzz")
    assert results == []


# ------------------------
# Test creación automática de archivo si no existe
# ------------------------

def test_read_file_crea_si_no_existe(tmp_path):
    path = tmp_path / "noexiste.json"
    data = p.read_file(str(path))
    assert data == {}
    assert os.path.exists(path)
#----------------------------------------


