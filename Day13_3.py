msg = input("Enter message: ").lower()


if "win money" in msg or "free offer" in msg or "click link" in msg:
    print("Warning: This looks like spam!")

else:
    print("Message looks safe")
