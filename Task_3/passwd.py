import hashlib
import getpass

PASSWORD_FILE = "password.txt"

def hashing(new_password):
    # Create a new SHA256 hash object
    hash_object = hashlib.sha256()

    # Add data to it (bytes, not strings)
    hash_object.update(new_password.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig

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
        
    new_password = input("Enter new password: ")
    new_pass_hash = hashing(new_password)

    userbase_dictionary[user][1] = new_pass_hash

    with open(PASSWORD_FILE, "w") as userbase:
        for username, (real_name, password_hash) in userbase_dictionary.items():
            userbase.write(f"{username}:{real_name}:{password_hash}\n")
    print("Password change successful")


if __name__ == '__main__':
    change_pass()