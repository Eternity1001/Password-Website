import base64
import os
from uuid import uuid4
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from server_side.database import *

def create_account(email: str, username: str, password: str, confirm_password: str) -> bool:
    status = search_account_entries("account", "username = ? AND email = ?", (username, email ))
    if status[0] :
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
    token = f.encrypt(key)    
    
    status =  add_account_entries(database_name="account",
                        uuid=str(uuid4()),
                        email=email, 
                        username=username, 
                        password=token,
                        salt=salt,
                        account_lock="0",
                        security_question="")
    
    if status:
        return True
    return False
        
def login(email: str, password: str):
    status, user = search_account_entries("account", "email = ?", (email, ))
    
    if status:
        print(user[4])
        
        
        kdf = Argon2id(
        salt=user[4],
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=2**21
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))
        f = Fernet(key)
        token = f.decrypt(key)   
        # print(token) 
# add_account_entries("account", f"{uuid.uuid4()}", "test@test.com", "hello", "yea","","","")

    