review = input("Enter your movie review: ").lower()

positive_words = ["good", "great", "excellent", "amazing", "superb"]
negative_words = ["bad", "boring", "worst", "poor", "terrible"]

pos = any(word in review for word in positive_words)

neg = any(word in review for word in negative_words)

if pos and not neg:
    print("Sentiment: 👍 Positive Review")

elif neg and not pos:
    print("Sentiment: 👎 Negative Review")

elif pos and neg:
    print("Sentiment: 😐 Mixed Review")

else:
    print("Sentiment: 🤔 Neutral / Not Clear")