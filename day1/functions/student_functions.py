"""Day 1 - Python Fundamentals."""


def get_student_info():
    student_name = input("Enter student name:")
    marks_python = float(input("Enter marks for Python:"))
    marks_math = float(input("Enter marks for Mathematics:"))
    marks_comm = float(input("Enter marks for Communication:"))

    return {
        "name": student_name,
        "python_marks": marks_python,
        "math_marks": marks_math,
        "comm_marks": marks_comm,
    }


dict_student_info = get_student_info()
student_name = dict_student_info["name"]
marks_python = dict_student_info["python_marks"]
marks_math = dict_student_info["math_marks"]
marks_comm = dict_student_info["comm_marks"]

#TODO:
total=(marks_python+marks_math+marks_comm)
percentage =(total/300)*100
#percentage = 0

print("\n -- Result --")
print("Student:", student_name)
print("Percentage",percentage)
