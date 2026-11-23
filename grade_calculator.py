
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

try:
    maths = float(input("Enter Mathematics marks: "))
    english = float(input("Enter English marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    marks = [maths, english, physics, chemistry]

    if not all(0 <= mark <= 100 for mark in marks):
        print("Error: Marks must be between 0 and 100!")

    else:
        total = sum(marks)
        average = total / 4

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        if grade == "A":
            remark = "Excellent performance!"
        elif grade == "B":
            remark = "Very good performance!"
        elif grade == "C":
            remark = "Good performance!"
        elif grade == "D":
            remark = "Fair performance!"
        else:
            remark = "Poor performance. Keep practicing!"

        print("\n===== STUDENT RESULTS =====")
        print("Student Name:", name)
        print("Total Marks:", total)
        print("Average Marks:", average)
        print("Final Grade:", grade)
        print("Remarks:", remark)

except ValueError:
    print("Error: Please enter numbers only!")
