# Stage 3: Student Grade Calculator
def grade_calculator():
    name = input("Enter student name: ")
    marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
    total = sum(marks)
    percentage = (total / 300) * 100
    if percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'
    print(f"{name}\nTotal: {total}/300\nPercentage: {percentage:.1f}%\nGrade: {grade}")

grade_calculator()
