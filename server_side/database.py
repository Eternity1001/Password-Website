import sqlite3
import uuid
from pathlib import Path
from sqlite3 import Connection, Cursor

def create_database(database_name: str) -> tuple[bool, Cursor, Connection] | tuple[bool, None, None]:
    allowed_database = ["temp", "account"]
    if database_name in allowed_database:
        try:
            con = sqlite3.connect(f".venv/database/{database_name}.db")
            cur = con.cursor()
            return True, cur, con

        except sqlite3.Error as _e:
            
            return False, None, None
    return False, None, None


def delete_database(database_name: str) -> None:
    file_path = Path(f".venv/database/{database_name}.db")
    file_path.unlink(missing_ok=True)


def create_account_db(database_name: str) -> bool:
    status, cur, con = create_database(database_name)
    if status and cur and con:
        cur.execute("CREATE TABLE users(uuid, email, username, password, salt, account_lock, security_question)")
        con.commit()
        con.close()
        return True
    return False


def fresh_start(database_name: str):
    ""


def add_account_entries(database_name: str, uuid: uuid.UUID, email: str, username: str, password: str, salt: str, account_lock: str, security_question: str) -> bool:
    status, cur, con = create_database(database_name)
    if status and cur and con:
        cur.execute(
            """INSERT INTO users (uuid, email, username, password, salt, account_lock, security_question) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (uuid, email, username, password, salt, account_lock, security_question))
        con.commit()
        con.close()
        return True
    return False


def search_account_entries(database_name:str, search_field:str, search_data: tuple[str, ...]):
    status, cur, con = create_database(database_name)

    if status and cur and con:
        cur.execute(f"SELECT * FROM users WHERE ({search_field})", search_data)
        user = cur.fetchone()
        con.close()
        if user is None:
            return False, None
        return True, user

    return False, None

# # add_account_entries("account", f"{uuid.uuid4()}", "test@test.com", "hello", "yea","","","")
# # search_account_entries("account", "username", "hello" )

# # sleep(2)

# # delete_database("account")
