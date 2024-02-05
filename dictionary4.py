car = {
    "brand": "ford",
    "model": "mustang",
    "age": 12
}

copy1 = car.copy()
copy2 = dict(car)

print(car)
print(copy1)
print(copy2)

car["age"] = 25

print(car)
print(copy1)
print(copy2)