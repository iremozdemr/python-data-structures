#list:
#-değiştirilebilir
#-sıralıdır
#-index işlemleri yapılabilir
#-farklı veri tipleri aynı list'e eklenebilir
#-list içine list eklenebilir
#-aynı element tekrar eklenebilir

#if you add new items to a list
#the new items will be placed at the end of the list

#lists are created using square brackets

list1 = ["a","b","c","a",1,"d",False]
#list items can be of any data type

length = len(list1)
print(length) 

type = type(list1)
print(type)
#lists are defined as objects in python
#list's data type is "list"

list2 = list((1,2,3))
#list constructor
#list() is wrong
#list(()) is true