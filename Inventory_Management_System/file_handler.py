import json
import os

from data import inventory

FILE_NAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            inventory.clear()
            inventory.extend(data)

def save_inventory():
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)