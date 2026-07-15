import json

def read_metadata(path):
    with open(path, "r") as file:
        return json.load(file)