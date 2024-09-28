names = ("a","b","c")
(name1,name2,name3) = names
#unpacking
#number of variables = number of items

ages = (12,13,14,15,16)
(age1,age2,*age3) = ages
#unpacking
#number of variables < number of items

usernames = ("q","w","e","r","t")
(*username1,username2,username3) = usernames
#unpacking
#number of variables < number of items

print(name1)
print(name2)
print(name3)

print(age1)
print(age2)
print(age3)#list

print(username1)#list
print(username2)
print(username3)