import hashlib
import getpass

PASSWORD_FILE = 'password.txt'

 
def hashing(new_password):
    # Create a new SHA256 hash objectnew
    hash_object = hashlib.sha256()

    # Add data to it (bytes, not strings)
    hash_object.update(new_password.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig


def add_user():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, 'a+') as userbase:
        userbase.seek(0)
        for user in userbase:
            username, real_name, password = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password]
        new_user = input("Enter new username: ")
        if new_user in userbase_dictionary:
            print("Cannot add. Most likely username already exists.")
            return
        new_real_name = input("Enter real name: ")
        new_password = getpass.getpass("Enter password: ")
        password_hash = hashing(new_password)

        userbase_dictionary[new_user] = [new_real_name, password_hash]
        userbase.write(f"{new_user}:{new_real_name}:{password_hash}\n")


if __name__ == "__main__":
    add_user()