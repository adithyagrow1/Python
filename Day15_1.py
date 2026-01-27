caption = input("Enter your caption: ")

if len(caption) < 10:
    print("Caption is too short.")
elif len(caption) > 100:
    print("Caption is too long.")
elif "#" not in caption:
    print("Add at least one hashtag for better reach.")
else:
    print("Caption looks good!")
