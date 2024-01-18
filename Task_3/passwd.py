import getpass
import passutils

PASSWORD_FILE = "password.txt"


def change_pass():
    userbase_dictionary = {}
    with open(PASSWORD_FILE,"r") as userbase:
        #userbase.seek(0)
        for user in userbase:
            username, real_name, password_hash = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password_hash]
    user = input("Enter new username: ")    
    if user not in userbase_dictionary:
        print("Username doesnot exist")
        return
    while True:
        new_password = getpass.getpass("Enter password: ")
        if passutils.validate_password(new_password):
            break    
    new_pass_hash = passutils.hashing(new_password)

    userbase_dictionary[user][1] = new_pass_hash

    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")
    print("Password change successful")


if __name__ == '__main__':
    change_pass()