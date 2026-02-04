import json

# ---------- Operaciones con fichero ----------
def read_file(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        write_file(DATA_FILE, {})
        return {}


def write_file(DATA_FILE, data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

import os

# ---------- CRUD genérico ----------

def create(DATA_FILE, collection, id, item):
    data = read_file(DATA_FILE)
    collection_data = data.setdefault(collection, {})
    key = str(id)

    if key in collection_data:
        raise ValueError("ID duplicado")

    collection_data[key] = item
    write_file(DATA_FILE, data)
    return True


def get(DATA_FILE, collection, id):
    data = read_file(DATA_FILE)
    return data.get(collection, {}).get(str(id))


def get_all(DATA_FILE, collection):
    data = read_file(DATA_FILE)
    return data.get(collection, {})


def update(DATA_FILE, collection, id, item):
    data = read_file(DATA_FILE)
    key = str(id)

    if collection not in data or key not in data[collection]:
        raise ValueError("Elemento no existe")

    data[collection][key] = item
    write_file(DATA_FILE, data)
    return True


def delete(DATA_FILE, collection, id):
    data = read_file(DATA_FILE)
    key = str(id)

    if collection not in data or key not in data[collection]:
        raise ValueError("Elemento no existe")

    del data[collection][key]
    write_file(DATA_FILE, data)
    return True


# ---------- Búsquedas ----------

def get_by_field(DATA_FILE, collection, field, value):
    data = read_file(DATA_FILE)
    for item in data.get(collection, {}).values():
        if item.get(field) == value:
            return item
    return None


def search_by_field_contains(DATA_FILE, collection, field, text):
    data = read_file(DATA_FILE)
    results = []
    text = text.lower()

    for item in data.get(collection, {}).values():
        value = str(item.get(field, "")).lower()
        if text in value:
            results.append(item)

    return results

