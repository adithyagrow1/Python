password = "secret123"
attempts = 3


while attempts > 0:
    user_pass = input("Enter password: ")

    if user_pass == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)


if attempts == 0:
    print("Account locked. Too many failed attempts.")
