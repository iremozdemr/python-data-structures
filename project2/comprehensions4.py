#dict comprehensions

dictionary = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

dictionary = {k:v * 2 for (k,v) in dictionary.items()}

print(dictionary.items())

dictionary = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

dictionary = {k.upper():v for (k,v) in dictionary.items()}

print(dictionary.items())

dictionary = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

dictionary = {k.upper():v*2 for (k,v) in dictionary.items()}

print(dictionary.items())