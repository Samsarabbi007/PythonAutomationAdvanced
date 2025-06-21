import pandas as pd
import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())
dist= {
    "Name": ["John", "Suborno", "Tanvir", "Sam", "Sazzad"],
    "ID" : [11,21,31,41,51]
}

df = pd.DataFrame(data=dist)
print(df)


file_name = "sample.xlsx"
df.to_excel(file_name, index=False)
df.to_excel("data.xlsx", index=False)

print("File saved as:", file_name)
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())