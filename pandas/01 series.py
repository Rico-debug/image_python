import pandas as pd
import numpy as np
import string

#创建Series
t1 = pd.Series([1,2,3,4,45])
t2 = pd.Series(np.arange(10),index=list(string.ascii_uppercase[:10])) #指定索引
print(t1)
print(t2)

#通过字典创建
temp_dict = {"name":"yang","age":"11","Tel":"17823446754"}
t3 = pd.Series(temp_dict)
print(t3)


#索引和值
print(t3[1])
print(t3["name"])
print(t3.index)
print(t3.values)
