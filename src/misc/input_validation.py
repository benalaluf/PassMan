import re

def validate_mail(mail: str) -> bool:
    if not mail:
        return False

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, mail))


