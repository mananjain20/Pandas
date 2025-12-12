import pandas as pd

# creating a simple Data Frame 
data = {"Name": ["A","B","C"], "Age":[20,25,30]}
df = pd.DataFrame(data)
print(df)

s = pd.Series([10,20,30,40,50])
print(s)
print(s[2])