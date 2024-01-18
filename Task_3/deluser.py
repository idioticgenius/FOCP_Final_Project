import getpass
import passutils
import tempfile
import os

PASSWORD_FILE = "password.txt"

def confirm_deletion(username):
    confirmation = input(f"Are you sure you want to delete {username}? (y/n): ")
    return confirmation.lower() == 'y'

def del_user():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, "r") as userbase:
        for user in userbase:
            username, real_name, password_hash = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password_hash]

    username = input("Enter username: ")
    if username not in userbase_dictionary:
        print("Username does not exist.")
        return

    password = getpass.getpass("Enter password: ")
    pass_hash = passutils.hashing(password)

    if pass_hash != userbase_dictionary[username][1]:
        print("Incorrect password.")
        return

    if confirm_deletion(username):
        removed_user = userbase_dictionary.pop(username)
        print(f"User {removed_user[0]} deleted.")
    else:
        print("User deletion cancelled.")
        return

    # Write to a temporary file and then replace the original file
    temp_file_descriptor, temp_file_path = tempfile.mkstemp()
    with os.fdopen(temp_file_descriptor, 'w') as temp_file:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            temp_file.write(f"{username}:{real_name}:{password_hash}\n")
    
    os.replace(temp_file_path, PASSWORD_FILE)

if __name__ == '__main__':
    del_user()
