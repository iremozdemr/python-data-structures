import seaborn as sns

#yöntem1:

df = sns.load_dataset("car_crashes")

list = ["mean","min","max","sum"]

dictionary = {}

for column in df.columns:
    dictionary[column] = list

print(dictionary)

#yöntem2:

df = sns.load_dataset("car_crashes")

dictionary = {column:list for column in df.columns}

print(dictionary)