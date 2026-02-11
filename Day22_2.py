

goal = input("What is your fitness goal? ").lower()

if "weight loss" in goal or "lose weight" in goal:
    print("Plan: Cardio + calorie deficit + daily steps target.")


elif "muscle" in goal or "gain" in goal or "bulk" in goal:
    print("Plan: Strength training + high protein diet.")

elif "abs" in goal or "core" in goal:
    print("Plan: Core workout + calorie control + HIIT.")

elif "fit" in goal or "healthy" in goal:
    print("Plan: Balanced routine with cardio + strength + stretching.")


else:
    print("Goal unclear. Please specify weight loss, muscle gain, or general fitness.")