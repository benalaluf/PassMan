import hashlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key_from_password(password, salt, iterations=100000, key_length=32):
    # Convert password to bytes
    password = password.encode('utf-8')

    key = hashlib.pbkdf2_hmac('sha256', password, salt, iterations, key_length)

    return key