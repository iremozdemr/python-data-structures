#list comprehensions

#yöntem 1:

salaries = [1000,2000,3000,4000,5000]
null_list = []

def new_salary(x):
    return x + 100

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

print(salaries)
print(null_list)

#yöntem 2:

salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x + 100

null_list = [new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

print(salaries)
print(null_list)