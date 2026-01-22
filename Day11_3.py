msg = input("Say something: ").lower()

if "hello" in msg or "hi" in msg:
    print("Hello! How can I help you?")
elif "weather" in msg:
    print("I think it might be sunny today!")


elif "name" in msg:
    print("I am a simple Python bot.")


elif "bye" in msg:
    print("Goodbye! Have a great day!")


else:
    print("Sorry, I didn't understand that.")
