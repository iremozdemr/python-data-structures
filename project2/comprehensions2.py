#list comprehensions

salaries = [1000,2000,3000,4000,5000]
new_list = [salary * 2 for salary in salaries]

print(salaries)
print(new_list)

salaries = [1000,2000,3000,4000,5000]
new_list = [salary * 2 if salary < 4000 else salary * 3 for salary in salaries]

print(salaries)
print(new_list)
#eğer if-else kullanılacaksa:
#if ve else ortaya yazılır

salaries = [1000,2000,3000,4000,5000]
new_list = [salary * 2 for salary in salaries if salary < 4000]

print(salaries)
print(new_list)
#eğer sadece if kullanılacaksa:
#if en sona yazılır