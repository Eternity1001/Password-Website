
import sqlite3
from pathlib import Path

def create_database(database_name: str):

    allowed_database = ["temp"]
    if database_name in allowed_database:
        con = sqlite3.connect(f".venv/database/{database_name}.db")
        cur = con.cursor()
        return True, cur
    return False, None

def delete_database(database_name: str):
    file_path = Path(f".venv/database/{database_name}.db")
    file_path.unlink(missing_ok=True)

def fresh_start(database_name:str):
    ""


# create_database("temp")
