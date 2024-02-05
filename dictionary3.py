student = {
    "name": "a",
    "surname": "b",
    "age": 12
}

student["age"] = 13
print(student)

student.update({"age":14})
print(student)

student["id"] = 12345
print(student)

student.update({"gpa":2.3})
print(student)

student.pop("id")
print(student)

student.popitem()
print(student)

del student["age"]
print(student)

del student
#print(student) -> error