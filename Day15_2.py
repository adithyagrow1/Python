phone = input("Enter phone number: ")

if len(phone) != 10:
    print("Phone number must be 10 digits.")
elif not phone.isdigit():
    print("Phone number should contain only numbers.")
elif phone[0] not in "6789":
    print("Phone number should start with 6, 7, 8, or 9.")
else:
    print("Valid Indian phone number.")
