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


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as err:
        print(err)

def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_lines(f):
            add_student(student)
        f.close()
    except Exception as err:
        print(err)


def read_lines(f):
    for line in f:
        yield line



read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
save_file(student_name)