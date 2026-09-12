import base64
import os
from uuid import uuid4
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidKey

from server_side.database import *
def create_account(email: str, username: str, password: str, confirm_password: str) -> tuple[bool, any]:
    status = search_account_entries("account", "username = ? OR email = ?", (username, email))
    if status[0] :
        return True, status
    salt = os.urandom(16)

    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=2**21
    )

    password_hash = kdf.derive(password.encode("utf-8"))


    status =  add_account_entries(database_name="account",
                        uuid=str(uuid4()),
                        email=email, 
                        username=username, 
                        password=password_hash,
                        salt=salt,
                        account_lock="0",
                        security_question="")
    
    if status:
        return True, None
    return False, None
        
def login(email: str, password: str):
    status, user = search_account_entries("account", "email = ?", (email, ))
    
    if status:
        kdf = Argon2id(
        salt=user[4],
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=2**21
        )
        try:
            kdf.verify(password.encode("utf-8"), user[3])
            return True
        except InvalidKey:
            return False 



# b'\x0f\xfeN#\xc7\xdf\xbf\xc5C\x00\x86\xcf\xe0\x85\xd7\xfc'
# b'gAAAAABqpCsuZfwvLqhwNFwlFCgGNw3f1LdgpALth6cFm_kbUOM0tF5O_W9bcrm_8Gsyjr1sVJPqVnoMCZWYPsAwdZdaf8HEbsY2t8Nz5XFu6SZyGIJMmFHayfHJMC4Gd8eaOH6iKy6a'