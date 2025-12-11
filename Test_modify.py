import pandas as pd

df=pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})
#add new column
df['D']=df['A']+df['B']
print(df)
df["E"] =df["A"]+df["B"] +df["C"]
print(df)


#DROP DOWN 
df =df.drop("C",axis=1)
print(df)

#Rename of Column

df =df.rename(columns = {"A":"ALPHA"})
print(df)

