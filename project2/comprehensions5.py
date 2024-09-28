#dict comprehensions

#yöntem 1:

dictionary = {}

for i in range(10):
    if i % 2 == 0:
        dictionary[i] = i ** 2

print(dictionary)

#yöntem 2:

dictionary = {}

dictionary = {i:i ** 2 for i in range(10) if i%2 == 0}

print(dictionary)