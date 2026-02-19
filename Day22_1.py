email = input("Enter the email message: ").lower()


if any(word in email for word in ["meeting", "project", "deadline", "team"]):
    print("Category: 🧑‍💼 Work Email")
elif any(word in email for word in ["mom", "dad", "friend", "family"]):
    print("Category: ❤️ Personal Email")
elif any(word in email for word in ["offer", "sale", "discount", "deal"]):
    print("Category: 🛍 Promotion Email")

elif any(word in email for word in ["lottery", "free money", "click link", "urgent"]):
    print("Category: 🚨 Spam Email")

else:
    print("Category: 📩 General Email (No clear category)")