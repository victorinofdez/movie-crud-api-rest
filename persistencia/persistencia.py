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
