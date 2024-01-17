import hashlib
import getpass

PASSWORD_FILE = "password.txt"

def hashing(new_password):
    # Create a new SHA256 hash object of the password
    hash_object = hashlib.sha256(new_password.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig

def deluser():
    userbase_dictionary = {}
    with open(PASSWORD_FILE,"r") as userbase:
        #userbase.seek(0)
        for user in userbase:
            username, real_name, password_hash = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password_hash]
    user = input("Enter username: ")    
    if user not in userbase_dictionary:
        print("Username doesnot exist")
        return
    password = input("Enter password: ")    
    pass_hash = hashing(password)
    if pass_hash == userbase_dictionary[username][1]:
        removed_user = userbase_dictionary.pop(username)
    print(f"User {removed_user[0]} deleted")

    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")


if __name__ == '__main__':
    deluser()