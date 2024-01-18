import getpass
import passutils

PASSWORD_FILE = 'password.txt'

def user_exists(username):
    with open(PASSWORD_FILE, 'r') as userbase:
        for user in userbase:
            if user.split(':')[0] == username:
                return True
    return False

def add_user():
    new_user = input("Enter new username: ")
    if user_exists(new_user):
        print("Cannot add. Most likely username already exists.")
        return
    
    new_real_name = input("Enter real name: ")
    print("Password should follow the following requirements")
    print("At least one lowercase letter.")
    print("At least one uppercase letter.")
    print("At least one digit.")
    print("At least one special character (e.g., @, #, $, etc.)")
    print("Password should be between 8 to 16 characters. ")

    new_password = passutils.get_valid_password()
    if not passutils.confirm_password(new_password):
        print("Operation Failed: Password confirmation failed.")
        return
    
    password_hash = passutils.hashing(new_password)

    with open(PASSWORD_FILE, "a") as userbase:
        userbase.write(f"{new_user}:{new_real_name}:{password_hash}\n")

    print(f"New user {new_user} added")



if __name__ == "__main__":
    add_user()