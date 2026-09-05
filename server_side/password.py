import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from server_side.database import create_database, search_account_entries
def create_account(email, username, password, confirm_password):

    status, cur, con = create_database("account")
    status, acc = search_account_entries("account", "username = ? or email = ?", "")

    # sea
    ""


    