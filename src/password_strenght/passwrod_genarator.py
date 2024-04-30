import random
import string

def generate_password(length=12):
    symbols = "!?@#$%^&*"
    allowed_chars = string.ascii_letters + string.digits + symbols
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    print("Generated Password:", generate_password(password_length))
