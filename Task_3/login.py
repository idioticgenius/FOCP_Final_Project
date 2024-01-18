import passutils
import deluser
import adduser
import passwd

PASSWORD_FILE = 'password.txt'


def login():
    """
    Authenticate a user based on username and password.

    Reads the password.txt file to load existing users and their passwords.
    Then prompts for a username and password, authenticating the user if the credentials match.
    
    Returns:
        bool: True if the user is authenticated, False otherwise.
    """
    # Load existing user data into a dictionary
    userbase_dictionary = {}
    with open(PASSWORD_FILE, 'a+') as userbase:
        userbase.seek(0)
        for user in userbase:
            username, real_name, password = user.strip().split(":")
            userbase_dictionary[username] = [real_name, password]
    
    # Prompt for user credentials and authenticate
    username = input("User: ")
    if username in userbase_dictionary:
        if passutils.authenticate_user(userbase_dictionary, username):
            print("Access granted.")
            return True
        else:
            print("Access denied")
            return False
    else:
        print("User not found")
        return False

def main():
    """
    Main function to run the User Management System.

    Provides a menu for user management operations like adding, deleting,
    and changing passwords. Calls respective functions based on user choice.
    """
    if login():
        while True:
            # Display the menu
            print("="*30)
            print(f"| {'User Management System':<27}|")
            print("="*30)
            print(f"| {'1. Add User':<27}|")
            print(f"| {'2. Delete User':<27}|")
            print(f"| {'3. Change Password':<27}|")
            print(f"| {'4. Exit':<27}|")
            print("="*30)

            option = input("Enter your choice: ")

            if option == '1':
                adduser.add_user()
            elif option == '2':
                deluser.del_user()
            elif option == '3':
                passwd.change_pass()
            elif option == '4':
                break
            else:
                print("Invalid option")
            
            input("\nPress Enter to continue....\n")

        

if __name__ == "__main__":
    main()