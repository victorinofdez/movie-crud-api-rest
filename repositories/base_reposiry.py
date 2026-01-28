from persistencia import persistencia as p

DATA_FILE = "data/data.json"

# ---------- CRUD ----------
def create(section, key, value):
    data = p.read_file(DATA_FILE)
    if section not in data:
        data[section] = {}

    if str(key) in data[section]:
        raise ValueError(f"Ya existe el id {key} en '{section}'")

    data[section][str(key)] = value
    p.write_file(DATA_FILE, data)


def get(section, key):
    data = p.read_file(DATA_FILE)
    return data.get(section, {}).get(str(key))


def get_all(section):
    data = p.read_file(DATA_FILE)
    return data.get(section, {})


def update(section, key, value):
    data = p.read_file(DATA_FILE)
    if section not in data or str(key) not in data[section]:
        raise ValueError(f"No existe el id {key} en '{section}'")

    data[section][str(key)] = value
    p.write_file(DATA_FILE, data)


def delete(section, key):
    data = p.read_file(DATA_FILE)
    if section not in data or str(key) not in data[section]:
        raise ValueError(f"No existe el id {key} en '{section}'")

    del data[section][str(key)]
    p.write_file(DATA_FILE, data)


# ---------- Búsquedas ----------
def get_by_field(section, field, value):
    data = p.read_file(DATA_FILE)
    items = data.get(section, {})

    for item in items.values():
        if str(item.get(field, "")).lower() == str(value).lower():
            return item

    return None


def search_by_field_contains(section, field, text):
    data = p.read_file(DATA_FILE)
    items = data.get(section, {})

    text = str(text).lower()
    return [
        item for item in items.values()
        if text in str(item.get(field, "")).lower()
    ]
