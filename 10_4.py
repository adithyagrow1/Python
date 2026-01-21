sentence = input("Enter a sentence: ").strip()

if sentence.endswith(".") or sentence.endswith("!") or sentence.endswith("?"):
    print("Proper punctuation")
else:
    print("No punctuation at the end")
