students = []

def print_students_titlecase():
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            student["name"] = student["name"].title()
            students_titlecase.append(student)
        return students_titlecase
    print(get_students_titlecase())


def add_student(name, student_id = 123):
    student = {"name": name, "student_id": student_id}
    students.append(student)

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
print_students_titlecase()