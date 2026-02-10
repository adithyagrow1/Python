dictionary = {
    "python": "A powerful programming language.",
    "algorithm": "A step-by-step procedure to solve a problem.",
    "ai": "Artificial Intelligence – machines that think like humans.",
    "data": "Facts and statistics collected together.",
    "debug": "Finding and fixing errors in code."
}


word = input("Enter a word to find meaning: ").lower()

if word in dictionary:
    print("Meaning:", dictionary[word])

elif word.endswith("s") and word[:-1] in dictionary:
    print("Meaning:", dictionary[word[:-1]], "(singular form)")

elif len(word) < 3:
    print("Word too short to search.")
else:
    print("Meaning not found in dictionary.")