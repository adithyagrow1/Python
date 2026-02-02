feedback = input("Enter your feedback: ").lower()

if any(w in feedback for w in ["love", "great", "awesome", "nice", "excellent"]):
    print("Feedback Type: 👍 Positive")

elif any(w in feedback for w in ["improve", "should add", "suggest", "recommend"]):
    print("Feedback Type: 💡 Suggestion")

elif any(w in feedback for w in ["angry", "frustrated", "hate", "worst"]):
    print("Feedback Type: 😠 Angry")

elif any(w in feedback for w in ["problem", "issue", "not working", "bad"]):
    print("Feedback Type: ⚠ Complaint")

else:
    print("Feedback Type: 🤔 Neutral / Not clear")