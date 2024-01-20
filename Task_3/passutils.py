import hashlib
import getpass

def hashing(new_password):
    """
    Create a SHA256 hash of the given password.

    Args:
    new_password (str): The password to be hashed.

    Returns:
    str: The hexadecimal hash of the password.
    """
    hash_object = hashlib.sha256(new_password.encode())

    return hash_object.hexdigest()

def validate_password(password):
    """
    Validate the given password based on defined criteria.

    Args:
    password (str): The password to be validated.

    Returns:
    bool: True if the password meets the criteria, False otherwise.
    """
    if len(password) < 8:
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
    """
    Prompt the user to enter a password and validate it.

    Args:
    prompt (str, optional): The prompt to display to the user.

    Returns:
    str: The validated password.
    """
    while True:
        new_password = getpass.getpass(prompt)
        if validate_password(new_password):
            return new_password

def confirm_password(password):
    """
    Confirm the given password by asking the user to re-enter it.

    Args:
    password (str): The original password to match.

    Returns:
    bool: True if the user correctly re-enters the password, False otherwise.
    """
    for i in range(3):
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            return True
        else:
            print("Passwords did not match.")
    return False


def authenticate_user(userbase, username, prompt = "Enter Password: "):
    """
    Authenticate a user by verifying their password.

    Args:
    userbase (dict): A dictionary containing username-password pairs.
    username (str): The username of the user to authenticate.
    prompt (str, optional): The prompt to display for password input.

    Returns:
    bool: True if authentication is successful, False otherwise.
    """

    for i in range(3):
        old_password = getpass.getpass(prompt)
        if hashing(old_password) == userbase[username][1]:
            return True
        else:
            print("Incorrect password.")
    return False