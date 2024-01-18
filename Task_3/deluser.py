import getpass
import passutils


PASSWORD_FILE = "password.txt"

def confirm_deletion(username):
    """
    Ask the user to confirm the deletion of a user account.

    Args:
    username (str): The username of the account to be deleted.

    Returns:
    bool: True if the user confirms deletion, False otherwise.
    """
    confirmation = input(f"Are you sure you want to delete {username}? (y/n): ")
    return confirmation.lower() == 'y'

def del_user():
    """
    Delete a user from the userbase.

    This function allows for the deletion of a user from the userbase file.
    It first verifies the existence of the user and then confirms the deletion 
    after successfully verifying the user's password.
    """
    # Load existing user data into a dictionary
    userbase_dictionary = {}
    with open(PASSWORD_FILE, "r") as userbase:
        for user in userbase:
            username, real_name, password_hash = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password_hash]

    username = input("Enter username: ")
    # Check if the username exists in the userbase
    if username not in userbase_dictionary:
        print("Username does not exist.")
        return
    
    # Verify the user's password before deletion
    password = getpass.getpass("Enter password: ")
    pass_hash = passutils.hashing(password)
    if pass_hash != userbase_dictionary[username][1]:
        print("Incorrect password.")
        return
    
    # Confirm deletion with the user and then delete the user from dictionary
    if confirm_deletion(username):
        removed_user = userbase_dictionary.pop(username)
        print(f"User {removed_user[0]} deleted.")
    else:
        print("User deletion cancelled.")
        return
    
    # Write the updated userbase back to the file
    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")


if __name__ == '__main__':
    del_user()
