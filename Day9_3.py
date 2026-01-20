#exercise
# validate user input exercise
#username is no more than 12 characters
#username must not contain spaces
#username must not contain digits

username = input("enter your username:")
username.find(" ")
if len(username) > 12:
    print("your user name cant have more than 12 characters!")
elif not username.find(" ") == -1:
    print("your user name can't contain space!")
elif not username.isalpha() == True:
    print("your user name cant contain digits!")
else:
    print(f"welcome {username}")