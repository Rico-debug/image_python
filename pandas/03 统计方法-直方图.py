import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:/软件/软件学习/Python/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#用来获取打印的所有结果，使其不被省略
pd.set_option("display.max_column",None)

# print(df.info())
# print(df.head())

#runtime的分布
runtime_datd = df["Runtime (Minutes)"].values
max_runtime = runtime_datd.max()
min_runtime = runtime_datd.min()
#计算组距
num_bin = (max_runtime - min_runtime)//5
print(num_bin)

#设置图形参数
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_datd, num_bin)
plt.xticks(range(65, 200,5))
plt.show()


