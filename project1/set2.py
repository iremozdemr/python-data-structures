#you cannot change tuples items
#you can add an item
#you can remove an item

myset = {1,2,3,4,5}
print(myset)

myset.add(6)
print(myset)

myset.remove(2)
print(myset)

#myset.remove(15)
#print(myset)
#this is an error

myset.discard(15)
print(myset)
#this is not an error

myset.pop()
print(myset)

myset.clear()
print(myset)

del myset
#print(myset) -> error