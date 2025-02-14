username = input("Enter username: ")

if(len(username) < 10):
    print("Username must be at least 10 characters long")
else:
    print("your username is: ", username)