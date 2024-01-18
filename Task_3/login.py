import getpass
import passutils

PASSWORD_FILE = 'password.txt'


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
        password = passutils.hashing(password)
        if password == userbase_dictionary[username][1]:
            print("Access granted.")
        else:
            print("Access denied")
    else:
        print("User not found")

if __name__ == "__main__":
    main()