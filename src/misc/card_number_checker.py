import re


def card_type(card_number):
    card_number = ''.join(c for c in card_number if c.isdigit())

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

    return 'unknown'

