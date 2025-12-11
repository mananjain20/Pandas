import pandas as pd
df=pd.DataFrame({
    'Name':['A','B','C'],
    'Marks':[80,75,90]
})
print(df.sort_values('Marks'))

print(df.sort_values('Marks',ascending=False))