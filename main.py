from classes import HighSchoolStudent

student_name = input("What is the student's name?\n")
james = HighSchoolStudent(student_name)

print(james.get_name_capitalize())