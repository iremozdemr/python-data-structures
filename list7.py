#############################################
list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1+list2

print(list1)
print(list2)
print(list3)
#############################################
list4 = ["a","b","c"]
list5 = [1,2,3]

list4.extend(list5)

print(list4)
print(list5)
#############################################
list6 = ["a","b","c"]
list7 = [1,2,3]

for x in list7:
    list6.append(x)

print(list6)
print(list7)
#############################################