import base64
import os
from uuid import uuid4
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from server_side.database import create_database, search_account_entries
from cryptography.hazmat.primitives import hashes

def create_account(email: str, username: str, password: str, confirm_password: str):

    status, cur, con = create_database("account")
    
    status, acc = search_account_entries("account", "username = ? AND email = ?", (username, email ))
    if status:
        return True

    salt = os.urandom(16)
    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=2**21
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))
    f = Fernet(key)
    token = f.encrypt()    
    print(f)
    
    
    # add_account_entries(
    #     database_name="account",
    #     uuid= uuid4(),
    #     email=email,
    #     username=username,
    #     password=password,
        
    # )
    
    

# add_account_entries("account", f"{uuid.uuid4()}", "test@test.com", "hello", "yea","","","")

    