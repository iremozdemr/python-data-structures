list = ["word1","word2","word3"]

for x in list:
    print(x)

length = len(list)

for x in range(length):
    print(list[x])

for x in range(0,length):
    print(list[x])

i = 0
while i<length:
    print(list[i])
    i = i+1

[print(x) for x in list]