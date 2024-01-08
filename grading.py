def grade_student(mark):
    if mark < 0 or mark > 100:
        return "Invalid"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "E"

# Get student mark as input
try:
    student_mark = float(input("Enter the student's mark: "))
    # Call the grade_student function and print the result
    result = grade_student(student_mark)
    print(f"The student's grade is: {result}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")