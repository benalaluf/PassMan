import pyotp
import qrcode
from PIL import Image

# Function to generate a random secret key
def generate_secret_token():
    return pyotp.random_base32()

# Function to generate a QR code for the secret key
def generate_qr_code(secret_key, filename):
    totp = pyotp.totp.TOTP(secret_key)
    uri = totp.provisioning_uri(name='iBen & co', issuer_name='PassMan')
    img = qrcode.make(uri)
    img.save(filename)

# Function to verify the OTP entered by the user
def verify_otp(secret_key, user_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_otp)

if __name__ == "__main__":
    # Generate a secret key
    secret_key = generate_secret_token()

    # Generate a QR code for the secret key
    qr_code_filename = "qr_code.png"
    generate_qr_code(secret_key, qr_code_filename)
    print("QR code generated. Scan the QR code with Google Authenticator app.")

    # Prompt user to enter OTP
    user_otp = input("Enter OTP: ")

    # Verify OTP
    if verify_otp(secret_key, user_otp):
        print("OTP is valid")
    else:
        print("OTP is invalid")
