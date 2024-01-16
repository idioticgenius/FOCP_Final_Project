PASSWORD_FILE = '/home/abhidan/Documents/British_college/FOCP/FOCP_Final_Project/Task_3/password.txt'

def main():
    userbase_dictionary = {}
    with open(PASSWORD_FILE, 'a+') as userbase:
        userbase.seek(0)
        for user in userbase:
            username, real_name, password = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password]
    print(userbase_dictionary)
    username = input("User: ")
    if username in userbase_dictionary:
        password = input("Password: ")
        if password == userbase_dictionary[username][1]:
            print("Access granted.")
    else:
        print("User not found")

if __name__ == "__main__":
    main()