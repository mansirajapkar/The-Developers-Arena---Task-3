# import numpy as np 
# import pandas as pd 
# # # #Broadcasting
# # # a = np.array([1,2,3])
# # # b = 2
# # # print(a + b)   # [3 4 5]

# #Pandas
# import pandas as pd
# # s = pd.Series([10, 20, 30], index=["a","b","c"])

# data = {"Name":["Mansi","Raj"], "Age":[21,22]}
# df = pd.DataFrame(data)
# print(df["Name"])         # column
# print(df.loc[0])          # row by label
# print(df.iloc[1])         # row by index

# df.groupby("Age").mean()


# # data=np.array([1,2,3,4,5])
# # mean=np.mean(data)
# # print(mean)
# # print("Max : ", np.median(data))
# # print("Total",np.sum(data))
# # print("Square : ",np.sqrt(data))
# # print("Multiply by 2 ",data * 2)
# # print("Multiply by 5 ", data* 5)

# data={"Name" : ["Mansi","Gaurav","Seema","Radha","Kishna"],
#       "Age" : [19, 19, 22, 22,23],
#       "Marks" : [89,89,76,90,54],
#       "City" : ["Indore","Mumbai","Jaipur","Indore","Mumbai"]}

# df=pd.DataFrame(data)
# print("Original Dataset : ")
# print(df)
# print("-------")
# print("Name Column:")
# print(df['Name'])
# print("--------")
# print("First Row ")
# print(df.loc[0])
# print("-------")
# print("Average Marks by Age-")
# print(df.groupby('City')["Marks"].mean())

import pandas as pd
import numpy as np
#Client Project = Data Cleaning + Aggregation 
data = {"Student": ["Mansi","Gaurav","Mansi","Gaurav","Reema"],
        "Subject": ["Math","Math","Sci","Sci","Math"],
        "Marks": [90,80,None,90,80]}

df=pd.DataFrame(data)
print("Original Data")
print(df)
cln_dt=df.dropna()
print(cln_dt)
print("Unduplicated---")
print(cln_dt.drop_duplicates())
print("_______")
print("Grouping ")
print(cln_dt.groupby('Student')['Marks'].mean())

