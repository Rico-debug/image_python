import pandas as pd
import numpy as np

# t1 = pd.DataFrame(np.arange(12).reshape(3,4))
# print(t1)

t2 = pd.DataFrame(np.arange(12).reshape(3,4),index = list("abc"),columns=list("wxyz"))
print(t2)
print(t2.shape)
print(t2.shape[0])
print(t2.shape[1])

# #字典转换为DataFrame
# temp_dict = {"name":["ming","gang"],"age":[20,23],"Tel":[10086,10010]}
# t3 = pd.DataFrame(temp_dict)
# print(t3)