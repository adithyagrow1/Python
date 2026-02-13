print("Welcome to Customer Support!")
query = input("Describe your issue: ").lower()

if "refund" in query or "money" in query:
    print("→ Refund Team: We will initiate your refund within 2–3 days.")


elif "delay" in query or "late" in query or "not delivered" in query:
    print("→ Delivery Team: Your order is delayed. We are checking the status.")

elif "broken" in query or "damaged" in query:
    print("→ Replacement Team: We will arrange a replacement soon.")

elif "cancel" in query:
    print("→ Cancellation Team: Your order will be cancelled.")


elif "help" in query or "support" in query:
    print("→ Support Team: How else can we assist you?")
    
else:
    print("→ Could not identify the issue. Please provide more details.")