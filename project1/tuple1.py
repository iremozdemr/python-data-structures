#tuple items are
#ordered
#unchangeable
#allow duplicate values

#tuples are created using round brackets

mytuple = ("a",1,"a",2,"b",False)

print(mytuple)
print(len(mytuple))
print(type(mytuple))
print(mytuple[0])

tuple1 = ("x")
print(type(tuple1))
#this is not a tuple

tuple2 = ("x",)
print(type(tuple2))
#this is a tuple

tuple_with_constructor = tuple((1,2,3))
print(tuple_with_constructor)