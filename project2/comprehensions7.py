#isminde ins olan değişkenlerin başına FLAG ekle
#isminde ins olmayan değişkenlerin başına NO_FLAG ekle

import seaborn as sns

#yöntem1:

df = sns.load_dataset("car_crashes")

new_columns = []

for column in df.columns:
    if column.startswith("ins"):
        new_columns.append("FLAG" + column) 
    else:
        new_columns.append("NO_FLAG" + column)

df.columns = new_columns

print(df.columns)

#yöntem2:

df = sns.load_dataset("car_crashes")

df.columns = ["FLAG" + column if column.startswith("ins") else "NO_FLAG" + column for column in df.columns]

print(df.columns)