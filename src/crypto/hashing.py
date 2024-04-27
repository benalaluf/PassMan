import binascii
import hashlib
import os


def hashpass( password, salt):
    to_hash = salt + password
    hash = hashlib.sha256(to_hash.encode()).hexdigest()
    return hash


def generate_salt( length=16):
    # Generate raw bytes using a CSPRNG
    salt = os.urandom(length)
    # Encode the salt to a readable string (hexadecimal)
    encoded_salt = binascii.hexlify(salt).decode('utf-8')
    return encoded_salt