import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

file_path = "D:/软件/软件学习/Python/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts/msyhbd.ttc', size= '10')

#用来获取打印的所有结果，使其不被省略
pd.set_option("display.max_column",None)

print(df.info())
print(df.head())

#创建列表
temp_list = df["Genre"].str.split(',').tolist() #[[],[],[]]
genre_list = list(set([i for j in temp_list for i in j])) #将列表中的列表展开
# print(temp_list)
#构造全部为0的数组
zeros_df = t1 = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list) #将二维数组转换为DataFrame
print(zeros_df)

#给每个类别下赋值
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1 #将i行对应的电影 其列类型中符合的赋值为1
    #例如zeros_df.loc[0, ['sci','action']] = 1

#统计每个类别的个数
genre_count = zeros_df.sum(axis=0)
genre_count = genre_count.sort_values()
print(genre_count)
print(genre_count.shape)
#作图
genre = list(genre_count.index)
num = list(genre_count.values)
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
#绘制条形图
plt.barh(range(len(genre)),num,height=0.3,color="orange")
#设置字符串到x轴
plt.yticks(range(len(genre)),genre,fontproperties=my_font)
plt.grid(alpha=0.3)
# plt.savefig("./movie.png")
plt.show()



