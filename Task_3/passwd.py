import getpass
import passutils
import tempfile
import os

PASSWORD_FILE = "password.txt"


def change_pass():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, "r") as userbase:
        for user in userbase:
            username, real_name, password_hash = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password_hash]

    username = input("Enter username: ")
    if username not in userbase_dictionary:
        print("Username does not exist")
        return

    if not passutils.authenticate_user(userbase_dictionary, username, "Enter Old Password: "):
        print("Password verification failed.")
        return

    new_password = passutils.get_valid_password("Enter New Password: ")
    if not passutils.confirm_password(new_password):
        print("Operation Failed: Password confirmation failed.")
        return

    new_pass_hash = passutils.hashing(new_password)
    userbase_dictionary[username][1] = new_pass_hash

    with open(PASSWORD_FILE, 'w') as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")
    
    print("Password change successful")

if __name__ == '__main__':
    change_pass()
