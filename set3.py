set1 = {1,2,3}
set2 = {"a","b","c"}
set1.update(set2)
print(set1)

x = {1,2,3}
y = {4,2,6}
x.intersection_update(y)
print(x)

myset1 = {62,15,75}
myset2 = {38,15,56}
myset3 = myset1.intersection(myset2)
print(myset3)

i = {"a","b","c"}
j = {"a","x","c"}
i.symmetric_difference_update(j)
print(i)

q = {"f","z","n"}
w = {"f","z","m"}
t = q.symmetric_difference(w)
print(t)

a = {14,15,16}
b = {"a","b","c"}
c = a.union(b)
print(c)

set = {1,2,3}
list = ["x","y","z"]
tuple = ("q","w","e")

set.update(list)
print(set)
set.update(tuple)
print(set)