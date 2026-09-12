
import sqlite3
from pathlib import Path
from time import sleep
import uuid
def create_database(database_name: str):
    
    allowed_database = ["temp", "account"]
    if database_name in allowed_database:
        con = sqlite3.connect(f".venv/database/{database_name}.db")
        cur = con.cursor()
        return True, cur, con
    return False, None, None

def delete_database(database_name: str):
    file_path = Path(f".venv/database/{database_name}.db")
    file_path.unlink(missing_ok=True)

def create_account_db(database_name:str):
    status, cur, con = create_database(database_name)
    if status: 
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uuid TEXT PRIMARY KEY,
                email TEXT UNIQUE NOT NULL, 
                username TEXT UNIQUE NOT NULL,
                password BLOB NOT NULL,
                salt BLOB NOT NULL,
                account_lock INTEGER NOT NULL DEFAULT 0,
                security_question TEXT
            )
        """) 
        con.commit()
        con.close()
        return True     
    return False

def fresh_start(database_name:str):
    
    ""

def add_account_entries(database_name, uuid, email, username, password, salt, account_lock, security_question):
    status, cur, con = create_database(database_name)
    if status: 
        cur.execute("""INSERT INTO users (
        uuid, 
        email, 
        username,
        password,
        salt,
        account_lock,
        security_question) VALUES (?, ?, ?, ?, ?, ?, ?)""", 
        (uuid, email, username, password, salt, account_lock, security_question))

        con.commit()
        con.close()
        return True
    return False

def search_account_entries(database_name, search_field, search_data):
    status, cur, con = create_database(database_name)

    if status:
        cur.execute(f"SELECT * FROM users WHERE ({search_field})", search_data)
        user = cur.fetchone()
        con.close()
        if user:
            return True, user

    return False, None


def print_all_database_enteries(database:str, table_name:str):
    status, cur, con = create_database(database)
    if status and cur and con:
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        for row in rows:
            print(row) 
        con.close()
    return 
    
# create_account_db("account")

# add_account_entries("account", f"{uuid.uuid4()}", "test@test.com", "hello", "yea","","","")
# search_account_entries("account", "username", "hello" )

# sleep(2)

# delete_database("account")

# b'r\x92\xce@\xe3\x9f\xf1\xcd_|c!\xc8Hc3'
# {b'gAAAAABqpBQbnJVh2aGlKRpkhOdAfRDd6jMViQz65wKumXQ0fvyivgc06Uturl6PI4Th7geJ977r_UOSzTRz2j6Np5jpv3aq_8cFY0fV-y6SvVI2f--idleYMh6ybno0d_y-8pJZaLcC'}