dept = input("Choose branch (CSE/AI/EEE/MECH): ").upper()
rank = int(input("Enter your CET rank: "))

if dept == "CSE":
    cutoff = 5000
elif dept == "AI":
    cutoff = 7000
elif dept == "EEE":
    cutoff = 12000
elif dept == "MECH":
    cutoff = 20000
else:
    cutoff = -1

if cutoff == -1:
    print("Branch not found")
elif rank <= cutoff:
    print("You will most likely get", dept)
else:
    print("Chances are low for", dept)
