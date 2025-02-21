

user_credentials = {}

# function to register user

def register_user():

        username = input("Enter your Username: ")


        # Check to see if the username already exists
        if username in user_credentials:
            print("Username already exists. Please choose a different name")
        else:
            password = input("Enter a Password: ")
            user_credentials[username]= password
            print("Registration successfully")


#function to login the user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter the password: ")

# check to see if the username and password matches
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome back.")
    else:
        print("Invalid username or password. Please Try again.")



#main menu


def authentication_system():
    while True:
        print("Basic Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            register_user()
        elif option == '2':
            login_user()
        elif option =='3':
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please choose from option 1,2 or 3")


# run authentication system
authentication_system()

