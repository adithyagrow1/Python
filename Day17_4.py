msg = input("Enter message: ").lower()

if "angry" in msg or "hate" in msg or "fight" in msg:
    print("Mood detected: Negative 😠")
elif "happy" in msg or "love" in msg or "great" in msg:
    print("Mood detected: Positive 😊")
elif "sad" in msg or "upset" in msg:
    print("Mood detected: Sad 😢")
else:
    print("Tone unclear")
