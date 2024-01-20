import passutils

PASSWORD_FILE = 'password.txt'

def user_exists(username):
    """
    Check if a user exists in the userbase.

    Args:
    username (str): The username to check.

    Returns:
    bool: True if the user exists, False otherwise.
    """
    with open(PASSWORD_FILE, 'r') as userbase:
        for user in userbase:
            if user.split(':')[0] == username:
                return True
    return False

def add_user():
    """
    Add a new user to the userbase.
    The function prompts for a new username, real name, and password,
    then adds the new user with hashed password to the userbase file.
    """
    while True:
        new_user = input("Enter new username: ")
        # Validate that username is not purely numeric
        if not new_user or new_user.isdigit():
            print("Username cannot be empty or only numbers. Please try again.")
            continue

        # Check if the username already exists
        if user_exists(new_user):
            print("Cannot add. Most likely username already exists.")
            continue

        break
    
   
    new_real_name = input("Enter real name: ")
    
    # Display password requirements
    print("*"*55)
    print("Password should follow the following requirements")
    print("At least one lowercase letter.")
    print("At least one uppercase letter.")
    print("At least one digit.")
    print("At least one special character (e.g., @, #, $, etc.)")
    print("Password should be between 8 to 16 characters. ")
    print("*"*55)

    new_password = passutils.get_valid_password()
    if not passutils.confirm_password(new_password):
        print("Operation Failed: Password confirmation failed.")
        return
    
    password_hash = passutils.hashing(new_password)
    
    # Append the new user to the PASSWORD_FILE
    with open(PASSWORD_FILE, "a") as userbase:
        userbase.write(f"{new_user}:{new_real_name}:{password_hash}\n")

    print(f"New user {new_user} added")



if __name__ == "__main__":
    add_user()