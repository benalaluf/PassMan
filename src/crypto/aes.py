from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet


def aes_encrypt(key, plaintext):
    try:
        f = Fernet(key)
        padded_plaintext = pad(plaintext.encode(), 16)  # Pad plaintext
        return f.encrypt(padded_plaintext).decode()
    except Exception as e:
        print("Encryption failed:", e)
        return None

def aes_decrypt(key, ciphertext):
    try:
        f = Fernet(key)
        decrypted_data = f.decrypt(ciphertext.encode())
        unpadded_plaintext = unpad(decrypted_data, 16)  # Unpad decrypted data
        return unpadded_plaintext.decode()
    except Exception as e:
        print("Decryption failed:", e)
        return None


if __name__ == "__main__":
    key = Fernet.generate_key()
    print(key)
    plaintext = "Hello, World!"
    ciphertext = aes_encrypt(key, plaintext)
    print(ciphertext)
    decrypted = aes_decrypt(key, ciphertext)
    print(decrypted)
    assert decrypted == plaintext