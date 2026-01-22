password = input("Enter password: ")

length_ok = len(password) >= 8
upper_ok = any(c.isupper() for c in password)
lower_ok = any(c.islower() for c in password)
digit_ok = any(c.isdigit() for c in password)
special_ok = any(c in "@#$%&!" for c in password)

if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
    print("Strong password")
elif length_ok and digit_ok and (upper_ok or lower_ok):
    print("Medium password")
else:
    print("Weak password")
