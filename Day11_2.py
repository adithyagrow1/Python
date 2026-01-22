name = input("Enter the student's name: ")
marks = int(input("Enter marks out of 100: "))

if marks >= 90:
    grade = "A"
    remark = "Excellent performance"

elif marks >= 75:
    grade = "B"
    remark = "Good job"

elif marks >= 60:
    grade = "C"
    remark = "Satisfactory"

elif marks >= 40:
    grade = "D"
    remark = "Needs improvement"
        
else:
    grade = "F"
    remark = "Failed"

print(name + " scored Grade " + grade + " - " + remark)
