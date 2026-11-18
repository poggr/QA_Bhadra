

def student_grade():
    stu_name = input("Enter student name: ")
    marks1 = int(input("Enter marks for subject 1: "))
    marks2 = int(input("Enter marks for subject 2: "))
    marks3 = int(input("Enter marks for subject 3: "))

    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    if average_marks >= 80:
        grade = "Grade A"
    elif average_marks >= 60:
        grade = "Grade B"
    elif average_marks >= 40:
        grade = "Grade C"
    else:
        grade = "Fail"

    print("Student Name:", stu_name)
    print("Total Marks:", total_marks)
    print("Average Marks:", average_marks)
    print("Grade:", grade)

student_grade()