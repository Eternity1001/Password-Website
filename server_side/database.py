
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
        cur.execute("CREATE TABLE users(uuid, email, username, password, salt, account_lock, security_question)")   
        con.commit()
        con.close()
        return True     
    return False

def fresh_start(database_name:str):
    
    ""

def add_account_entries(database_name, uuid, email, username, password, salt, account_lock, security_question):
    status, cur, con = create_database(database_name)
    if status: 
        cur.execute("""INSERT INTO users (uuid, email, username, password, salt, account_lock, security_question) VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ((uuid, email, username, password, salt, account_lock, security_question)))
        con.commit()
        con.close()
        return True
    return False

def search_account_entries(database_name, search_field, search_data):
    status, cur, con = create_database(database_name)

    if status:
        cur.execute(f"SELECT * FROM users WHERE {search_field} = ?", (search_data,))
        user = cur.fetchone()
        print(user)
        con.close()
        
    
# create_account_db("account")

add_account_entries("account", f"{uuid.uuid4()}", "test@test.com", "hello", "yea","","","")
search_account_entries("account", "username", "hello" )

# sleep(2)

# delete_database("account")