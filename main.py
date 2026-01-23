import json

DATA_FILE = "persistencia/persistencia.py"

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


# ---------- CRUD ----------
def create(path, section, key, value):
    data = read_file(path)

    if section not in data:
        data[section] = {}

    if str(key) in data[section]:
        raise ValueError(f"Ya existe el id {key} en '{section}'")

    data[section][str(key)] = value
    write_file(path, data)
    return True


def get(path, section, key):
    data = read_file(path)
    return data.get(section, {}).get(str(key))


def get_all(path, section):
    data = read_file(path)
    return data.get(section, {})


def update(path, section, key, value):
    data = read_file(path)

    if section not in data or str(key) not in data[section]:
        raise ValueError(f"No existe el id {key} en '{section}'")

    data[section][str(key)] = value
    write_file(path, data)
    return True


def delete(path, section, key):
    data = read_file(path)

    if section not in data or str(key) not in data[section]:
        raise ValueError(f"No existe el id {key} en '{section}'")

    del data[section][str(key)]
    write_file(path, data)
    return True


# ---------- Búsqueda simple por campo ----------
def get_by_field(path, section, field, value):
    data = read_file(path)
    items = data.get(section, {})

    for item in items.values():
        if str(item.get(field, "")).lower() == str(value).lower():
            return item

    return None


def search_by_field_contains(path, section, field, text):
    data = read_file(path)
    items = data.get(section, {})

    text = str(text).lower()
    result = []

    for item in items.values():
        value = str(item.get(field, "")).lower()
        if text in value:
            result.append(item)

    return result


# ---------- Pruebas rápidas ----------

def main():


 if __name__ == "__main__":  
    main()
