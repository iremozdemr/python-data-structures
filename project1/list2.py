list = [1,"a",2,"b",3]
print(list)
print(list[0])
print(list[-1]) #the last item
print(list[-2]) #the second last item
print(list[1:4]) #1. 2. 3. indexes

#[start index(included) : end index(not included)]

list1 = list[1:4]
print(list1)
#when specifying a range
#the return value will be a new list with the specified items
#a 2 b

list2 = list[:4]
print(list2)
#the new list will start at the first item
#1 a 2 b

list3 = list[2:]
print(list3)
#the new list will go on to the end of the list
#2 b 3

mylist = [1,2,3,4,5]
if 8 in mylist:
    print("true")
else:
    print("false")