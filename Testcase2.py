import pandas as pd
data = {
    "Name": ["Tom","Nick","Krish","Jack"],
    "Marks": [99,98,95,100]
}

df = pd.DataFrame(data)
print(df)
# print(df["Name"])
print(df["Marks"])
