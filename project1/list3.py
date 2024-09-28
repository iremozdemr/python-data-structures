list = ["a","b","c","d","e"]
print(list)

list[3] = "f"
print(list)
#change item value

list[0:2] = ["q","w"]
print(list)
#change a range of item values

list[0:2] = ["e","i","s"]
print(list)
#if you insert more items than you replaced
#the new items will be inserted where you specified
#the remaining items will move accordingly

list[1:3] = ["n"]
print(list)
#if you insert less items than you replaced
#the new items will be inserted where you specified
#the remaining items will move accordingly