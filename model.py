import json

def load_data():
    with open("products.json") as f:
        return json.load(f)
db = load_data()

def save_data():
    with open("products.json",'w') as f:
        return json.dump(db,f)

