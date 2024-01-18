import getpass
import passutils

PASSWORD_FILE = 'password.txt'


def add_user():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, 'r') as userbase:
        userbase.seek(0)
        for user in userbase:
            username, real_name, password = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password]
    new_user = input("Enter new username: ")
    if new_user in userbase_dictionary:
        print("Cannot add. Most likely username already exists.")
        return
    new_real_name = input("Enter real name: ")
    print("Password should follow the following requirements")
    print("At least one lowercase letter.")
    print("At least one uppercase letter.")
    print("At least one digit.")
    print("At least one special character (e.g., @, #, $, etc.)")
    print("Minimum length of 8 characters.")
    while True:
        new_password = getpass.getpass("Enter password: ")
        if passutils.validate_password(new_password):
            break
    attempts = 0
    while attempts < 3:
        confirm_password = getpass.getpass("Confirm Password: ") 
        if new_password == confirm_password:
            password_hash = passutils.hashing(new_password)
            userbase_dictionary[new_user] = [new_real_name, password_hash]
            break
        else:
            attempts += 1
            print("Password didnot match")
    else:
        print("Operation Failed")
        return

    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")

    print(f"New user {new_user} added")



if __name__ == "__main__":
    add_user()