import hashlib
import getpass

PASSWORD_FILE = 'password.txt'

def hashing(new_password):
    # Create a new SHA256 hash object
    hash_object = hashlib.sha256()

    # Add data to it (bytes, not strings)
    hash_object.update(new_password.encode())

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, 'a+') as userbase:
        userbase.seek(0)
        for user in userbase:
            username, real_name, password = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password]
    #print(userbase_dictionary)
    username = input("User: ")
    if username in userbase_dictionary:
        password = getpass.getpass(prompt = "Password: ")
        password = hashing(password)
        if password == userbase_dictionary[username][1]:
            print("Access granted.")
        else:
            print("Access denied")
    else:
        print("User not found")

if __name__ == "__main__":
    main()