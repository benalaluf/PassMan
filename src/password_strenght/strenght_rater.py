import re

def password_strength(password):
    # Calculate length score
    length_score = min(len(password) / 8.0, 1)

    # Check for presence of uppercase letters
    has_uppercase = bool(re.search(r'[A-Z]', password))
    uppercase_score = 0.5 if has_uppercase else 0

    # Check for presence of lowercase letters
    has_lowercase = bool(re.search(r'[a-z]', password))
    lowercase_score = 0.5 if has_lowercase else 0

    # Check for presence of digits
    has_digit = bool(re.search(r'\d', password))
    digit_score = 0.5 if has_digit else 0

    # Check for presence of special characters
    has_special = bool(re.search(r'[!@#$%^&*()-_+=]', password))
    special_score = 0.5 if has_special else 0

    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_score

    # Determine strength rating based on total score
    if total_score >= 3:
        rating = "Strong"
    elif total_score >= 2:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, total_score

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength_rating, score = password_strength(password)
    print("Strength rating:", strength_rating)
    print("Total score:", score)