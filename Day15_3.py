email = input("Enter email message: ").lower()

if "job" in email or "interview" in email:
    print("Response: Thank you for your interest, we will get back to you.")
elif "complaint" in email:
    print("Response: We apologize for the inconvenience. We will resolve this soon.")
elif "meeting" in email:
    print("Response: Meeting confirmed. Looking forward!")
else:
    print("Response: Thank you for your message.")
