#############################################
list1 = [5,6,2,9,0,1]
print(list)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
#############################################
list2 = [5,1,2,8,3]
print(list2)

list2.reverse()
print(list2)
#############################################
mylist = ["a","b","c"]
copylist1 = mylist.copy()
copylist2 = list(mylist)

print(mylist)
print(copylist1)
print(copylist2)

mylist[0] = "w"

print(mylist)
print(copylist1)
print(copylist2)
#############################################