#list comprehensions

students = ["john","mark","venessa","mariam"]
students_make_upper = ["john","venessa"]

new_list = [student.upper() for student in students if student == "john" or student == "venessa"]

print(students)
print(new_list)

students = ["john","mark","venessa","mariam"]
students_make_upper = ["john","venessa"]

new_list = [student.upper() if student == "john" or student == "venessa" else student.lower() for student in students]

print(students)
print(new_list)

students = ["john","mark","venessa","mariam"]
students_make_upper = ["john","venessa"]

new_list = [student.upper() for student in students if student in students_make_upper]

print(students)
print(new_list)

students = ["john","mark","venessa","mariam"]
students_make_upper = ["john","venessa"]

new_list = [student.upper() if student in students_make_upper else student.lower() for student in students]

print(students)
print(new_list)