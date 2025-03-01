import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:/软件/软件学习/Python/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#用来获取打印的所有结果，使其不被省略
pd.set_option("display.max_column",None)

# print(df.info())
print(df.head())

#获取平均评分
rating = df["Rating"].mean()
print(rating)

#导演人数
print(len(set(df["Director"].tolist()))) #用集合去重，tolist变为列表
print(len(df["Director"].unique())) #df.unique 生成不重复的列表

#演员人数
temp_actors_list = df["Actors"].str.split(",").tolist()
# print(temp_actors_list)
actors_list = [i for j in temp_actors_list for i in j] #用于解开列表中的嵌套
# print(actors_list)
# actors_list = np.array(temp_actors_list).flatten()
actors_num = len(set(actors_list))
print(actors_num)