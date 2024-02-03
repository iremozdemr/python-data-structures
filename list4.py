list = ["a","b","c","a","s","e","r","t"]
print(list)

list.remove("b")
print(list)

list.remove("a")
print(list)
#if there are more than one item with the specified value
#removes the first occurance

list.pop(1)
print(list)
#removes the specified index

list.pop()
print(list)
#if you do not specify the index
#removes the last item

del list[0]
print(list)
#removes the specified index

#del list
#print(list)
#removes the entire list completely

#list.clear()
#print(list)
#removes the items

list.append("y")
print(list)

list.insert(0,"d")
print(list)

list.insert(15,"q")
print(list)
#adds the new item to the end of the list