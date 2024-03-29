PASSWORD_FILE = "password.txt"

def list_user():
    """
    List all users in the userbase.

    Reads the userbase file and prints each user's username and real name.
    """
    print("\nList of Users")
    print("=" * len("List of Users"))
    with open(PASSWORD_FILE, "r") as userbase:
        for user in userbase:
            if user.strip(): #Check if line is not empty
                username, real_name, password_hash = user.strip().split(":")
                print(f"Username: {username}, Real Name: {real_name}")


if __name__ == '__main__':
    list_user()