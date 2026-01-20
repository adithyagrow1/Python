#exercise
# validate user input exercise
#username is no more than 12 characters
#username must not contain spaces
#username must not contain digits

username = input("enter your username:")
username.find(" ")
if len(username) > 12:
    print("your user name cant have more than 12 characters!")
else:
    print(f"welcome {username}")