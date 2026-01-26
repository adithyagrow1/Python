text = input("Enter a sentence: ").lower()

bad_words = ["idiot", "stupid", "dumb"]

if any(bad in text for bad in bad_words):
    print("Warning: Your message contains inappropriate words.")
else:
    print("Message is clean.")
