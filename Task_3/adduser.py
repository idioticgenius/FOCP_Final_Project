PASSWORD_FILE = '/home/abhidan/Documents/British_college/FOCP/FOCP_Final_Project/Task_3/password.txt'
userbase_dictionary = {}
def add_user():
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
        new_password = input("Enter password: ")

        userbase_dictionary[new_user] = [new_real_name, new_password]
        userbase.write(f"{new_user}:{new_real_name}:{new_password}\n")


if __name__ == "__main__":
    add_user()