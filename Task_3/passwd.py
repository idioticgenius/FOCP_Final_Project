import passutils


PASSWORD_FILE = "password.txt"


def change_pass():
    """
    This function changes the password for an existing user in the userbase.
    """
    # Load existing user data into a dictionary
    userbase_dictionary = {}
    with open(PASSWORD_FILE, "r") as userbase:
        for user in userbase:
            if user.strip():
                username, real_name, password_hash = user.strip().split(":")
                userbase_dictionary[username] = [real_name, password_hash]

    username = input("Enter username: ")
    
    # Check if the username exists in the userbase
    if username not in userbase_dictionary:
        print("Username does not exist")
        return
    
    # Authenticate the user with the current password
    if not passutils.authenticate_user(userbase_dictionary, username, "Enter Old Password: "):
        print("Password verification failed.")
        return

    # Get a new valid password from the user
    new_password = passutils.get_valid_password("Enter New Password: ")
    # Confirm the new password
    if not passutils.confirm_password(new_password):
        print("Operation Failed: Password confirmation failed.")
        return

    # Hash the new password and update the user's entry
    new_pass_hash = passutils.hashing(new_password)
    userbase_dictionary[username][1] = new_pass_hash

    # Write the updated userbase back to the file
    with open(PASSWORD_FILE, 'w') as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")
    
    print("Password change successful")

if __name__ == '__main__':
    change_pass()
