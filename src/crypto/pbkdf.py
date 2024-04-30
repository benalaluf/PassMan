import hashlib
from base64 import urlsafe_b64encode

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key_from_password(password, salt, iterations=100000, key_length=32):
    # Convert password to bytes
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')

    # Derive key using PBKDF2
    key = hashlib.pbkdf2_hmac('sha256', password, salt, iterations, key_length)

    # Encode key in URL-safe base64 format
    fernet_key = urlsafe_b64encode(key)

    return fernet_key

