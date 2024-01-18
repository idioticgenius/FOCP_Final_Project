import getpass
import passutils


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

    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")


if __name__ == '__main__':
    del_user()
