import re


def card_type(card_number):
    """
    Determine the type of credit card based on the card number.

    Parameters:
        card_number (str): The credit card number.

    Returns:
        str: The type of credit card ('MasterCard', 'Visa', 'American Express', or 'Unknown').
    """
    # Remove any non-digit characters from the card number
    card_number = ''.join(c for c in card_number if c.isdigit())

    # Define the card type based on the starting digits
    if len(card_number) == 16:
        if card_number.startswith('5'):
            return 'mastercard'
        elif card_number.startswith('4'):
            return 'visa'
        elif card_number.startswith(('34', '37')):
            return 'amex'
    elif len(card_number) == 15:
        if card_number.startswith(('34', '37')):
            return 'amex'

    # If no matches found, return 'Unknown'
    return 'unknown'

