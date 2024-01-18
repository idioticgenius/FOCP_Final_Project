import hashlib
import getpass

def hashing(new_password):
    # Create a new SHA256 hash object of the password
    hash_object = hashlib.sha256(new_password.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig

def validate_password(password):
    if len(password) < 8 or len(password) > 16:
        print("Password must be at least 8 characters long.")
        return False

    has_lower = any(char.islower() for char in password)
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
        return False

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        return False

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        print("Password must contain at least one digit.")
        return False

    special_characters = "!@#$%^&*()-+?_=,<>/"
    has_special = any(char in special_characters for char in password)
    if not has_special:
        print("Password must contain at least one special character.")
        return False

    return True

def get_valid_password(prompt = "Enter password: "):
    while True:
        new_password = getpass.getpass(prompt)
        if validate_password(new_password):
            return new_password

def confirm_password(password):
    for i in range(3):
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            return True
        else:
            print("Passwords did not match.")
    return False


def authenticate_user(userbase, username, prompt = "Enter Password: "):
    for i in range(3):
        old_password = getpass.getpass(prompt)
        if hashing(old_password) == userbase[username][1]:
            return True
        else:
            print("Incorrect password.")
    return False