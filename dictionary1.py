#dictionary items are
#ordered
#changeable
#not allow duplicate values

#dictionaries are created using curly brackets

#key:value

mydictionary = {
    "name": "a",
    "surname":"b",
    "age":2,
    "name":"x"
}

print(mydictionary)
print(type(mydictionary))
print(len(mydictionary))

print(mydictionary["name"])
print(mydictionary["surname"])
print(mydictionary["age"])

dictionary = dict(name="john",age=36,country="norway")
print(dictionary)