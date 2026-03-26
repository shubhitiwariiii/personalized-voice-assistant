import json

MEMORY_FILE = "utils/memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file)


def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)


def recall(key):
    data = load_memory()
    return data.get(key, None)