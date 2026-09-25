# TODO
# Create a function called calculate_percentage()

# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage

#TODO
def calculate_percentage(marks_sub1, marks_sub2, marks_sub3):
    total = marks_sub1 + marks_sub2 + marks_sub3
    percentage = (total / 300) * 100
    return percentage
 
def calculte_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
if __name__ == "__main__":
    student_name = input("Enter student name: ")
    marks_python = float(input("Enter Python marks: "))
    marks_math = float(input("Enter Mathematics marks: "))
    marks_comm = float(input("Enter Communication marks: "))
    dict_student_info = {
        "name": student_name,
        "python_marks": marks_python,
        "math_marks": marks_math,
        "comm_marks": marks_comm,
    }

    percentage = calculate_percentage(
        dict_student_info["python_marks"],
        dict_student_info["math_marks"],
        dict_student_info["comm_marks"],
    )
    grade = calculte_grade(percentage)
    print("\n--- Result ---")
    print(f"Student: {student_name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    if __name__ == "__main__":
        print("\n--- Result ---")
        print(student_info)
        print("student:",student_info["name"])
        percentage = calculate_percentage(
            student_info["python_marks"],
            student_info["math_marks"],
            student_info["comm_marks"],
        )
        print("percentage",calculate_percentage(
            student_info["python_marks"],
            student_info["math_marks"],
            student_info["comm_marks"]
        )
    print(f"Grade: {calculte_grade(percentage)}")

    def save_student(students,file_name):
        """"