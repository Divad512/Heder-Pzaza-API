import json

def read_data(DB_NAME):
    try:
        with open(DB_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"message": "File not found"}


def write_data(DB_NAME, data):
    try:
        with open(DB_NAME, "w") as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        return {"message": "File not found"}
    