mytuple = (1,2,3,4,5)
#you cannot change tuples items
#you cannot add an item
#you cannot remove an item

mylist = list(mytuple)
mylist.append(6)
mylist.remove(2)
mylist[0] = 12

mytuple = tuple(mylist)
print(mylist)
print(mytuple)

del mytuple
#print(mytuple) -> error