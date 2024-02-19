import os
import json
from filelock import FileLock
base_path = "Data_Employees/"  # this refers to the database path


def validate_file(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError("User Not exist")

    if not filepath.endswith(".json"):
        raise FileNotFoundError("Invalid input!!")


def read_data(employee_id: str) -> dict:
    """it returns the data as dictionary"""
    filepath = f"{base_path}{employee_id}.json"
    validate_file(filepath)
    data = None
    with open(filepath, "r") as file:
        data = json.load(file)

    return data


def write_data(employee_id: str, data: dict):
    """Clean Current file and overwrite new data"""
    filepath = f"{base_path}{employee_id}.json"
    validate_file(filepath)
    with open(filepath, "w") as file:
        json.dump(data, file)


def create_file(filepath: str):
    with open(filepath, "w") as file:
        print("file is creating")


def delete_file(employee_id: str):
    filepath = f"{base_path}{employee_id}.json"
    validate_file(filepath)
    os.remove(filepath)



