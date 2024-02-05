car = {
    "brand": "ford",
    "model": "mustang",
    "age": 12
}

print(car["brand"])
print(car.get("brand"))

keys = car.keys()
values = car.values()
items = car.items()

print(keys)
print(values)
print(items)

car["age"] = 13

print(keys)
print(values)
print(items)