import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    print(all_characters)
    print(letters)
    print(digits)
    print(symbols)
    print(lettees + digits)
    

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, '[0123456789]')
        ]        

    return password
    print(constraints)
    # new_password = generate_password(8)
# print(new_password)
