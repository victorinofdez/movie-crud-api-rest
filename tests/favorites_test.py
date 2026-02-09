import json
import pytest

# ------------------- FIXTURES -------------------

@pytest.fixture
def tmp_json_file(tmp_path):
    """Archivo temporal para pruebas."""
    file_path = tmp_path / "data_tmp.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({}, f)
    return str(file_path)


@pytest.fixture
def sample_favorites(tmp_json_file):
    data = {
        "favorites": {
            "1": [1, 2], 
            "2": [2],     
            "3": []       
        }
    }
    with open(tmp_json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return tmp_json_file


# ------------------- HELPERS -------------------

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ------------------- TESTS FAVORITOS -------------------

def test_agregar_favorito(sample_favorites):
    file = sample_favorites
    data = read_json(file)
    data["favorites"].setdefault("3", []).append(1)
    write_json(file, data)

    data_after = read_json(file)
    assert 1 in data_after["favorites"]["3"]


def test_eliminar_favorito(sample_favorites):
    file = sample_favorites
    data = read_json(file)

    data["favorites"]["1"].remove(2)
    write_json(file, data)

    data_after = read_json(file)
    assert 2 not in data_after["favorites"]["1"]


def test_listar_favoritos(sample_favorites):
    file = sample_favorites
    data = read_json(file)
    favs_noemi = data["favorites"].get("1", [])
    favs_vito = data["favorites"].get("2", [])
    favs_david = data["favorites"].get("3", [])
    assert favs_noemi == [1, 2]
    assert favs_vito == [2]
    assert favs_david == []


def test_favorito_no_duplicado(sample_favorites):
    file = sample_favorites
    data = read_json(file)
    user_id = "1"  
    movie_id = 2
    if movie_id not in data["favorites"][user_id]:
        data["favorites"][user_id].append(movie_id)
    write_json(file, data)

    data_after = read_json(file)
    assert data_after["favorites"][user_id].count(2) == 1


def test_agregar_varios_favoritos(sample_favorites):
    file = sample_favorites
    data = read_json(file)
    data["favorites"].setdefault("3", []).extend([3, 4])
    write_json(file, data)

    data_after = read_json(file)
    assert data_after["favorites"]["3"] == [3, 4] or data_after["favorites"]["3"] == [1,3,4]


def test_eliminar_favorito_inexistente(sample_favorites):
    file = sample_favorites
    data = read_json(file)
    if 99 in data["favorites"]["3"]:
        data["favorites"]["3"].remove(99)
    write_json(file, data)

    data_after = read_json(file)
    assert data_after["favorites"]["3"] == []

"-------------------------------------"