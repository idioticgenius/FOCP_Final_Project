import hashlib

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