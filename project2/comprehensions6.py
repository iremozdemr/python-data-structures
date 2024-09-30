import seaborn as sns

#yöntem 1:

df = sns.load_dataset("car_crashes")

a = []

for column in df.columns:
    a.append(column.upper())

df.columns = a

print(df.columns)

#yöntem2:

df = sns.load_dataset("car_crashes")

df.columns = [column.upper() for column in df.columns]

print(df.columns)