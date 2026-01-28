name = input("Enter your name: ")
attendance = int(input("Enter attendance percentage: "))
assignment = input("Have you submitted assignments? (yes/no): ").lower()

if attendance < 75:
    print(name, ", you are NOT eligible due to low attendance.")
elif assignment != "yes":
    print(name, ", you are NOT eligible because assignments are pending.")
else:
    print(name, ", you ARE eligible for the exam!")
