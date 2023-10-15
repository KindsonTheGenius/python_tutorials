student_file = open("students.txt", "r")

print(student_file.readlines())

for student in student_file.readlines():
    print(student)

student_file.close()
