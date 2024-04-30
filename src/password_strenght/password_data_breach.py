import hashlib

import requests


def check_pwned_password(password):
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Send a GET request to the Pwned Passwords API
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    if response.status_code == 200:
        # Split the response by lines and check if our suffix is present
        for line in response.text.splitlines():
            if line.startswith(suffix):
                count = int(line.split(':')[1])
                return count
        return 0
    else:
        return None


if __name__ == "__main__":
    password = "asdkl;"
    print(check_pwned_password(password))