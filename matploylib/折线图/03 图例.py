import random
from matplotlib import font_manager
import matplotlib.pyplot as plt
import matplotlib
#字体设置
my_font_axis = font_manager.FontProperties(fname = 'C:\Windows\Fonts/msyhbd.ttc', size= '10')
my_font_title = font_manager.FontProperties(fname = 'C:\Windows\Fonts/msyhbd.ttc', size= '16')
#传入数据
x = range(18, 26)
a = [1,0,1,3,4,2,4,5]
b = [3,0,1,1,4,6,1,1]
fig = plt.figure(figsize = (16,8))
#生成并且设置曲线格式
plt.plot(x, a, label = "自己", color = "red", linestyle = '--', linewidth = 6)
plt.plot(x, b, label = "同桌", color = "green", linestyle = '-', linewidth = 6)
#刻度
plt.xticks(fontproperties=my_font_axis)
plt.yticks(fontproperties=my_font_axis)
#标题
plt.xlabel("岁数", fontproperties = my_font_title)
plt.ylabel("得分数", fontproperties = my_font_title)
plt.title("成绩", fontproperties = my_font_title)
#设置图例
plt.legend(prop = my_font_axis, loc = "upper left")

plt.show()
