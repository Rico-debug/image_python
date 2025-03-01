import random
from matplotlib import font_manager
import matplotlib.pyplot as plt
import matplotlib


#设置中文字体
# font = {'family' : 'MicroSoft YaHei',
#               'weight' : 'bold',
#               'size'   : '10'}
# matplotlib.rc("font", **font)
my_font_axis = font_manager.FontProperties(fname = 'C:\Windows\Fonts/msyhbd.ttc', size= '10')
my_font_title = font_manager.FontProperties(fname = 'C:\Windows\Fonts/msyhbd.ttc', size= '16')

fig = plt.figure(figsize = (16,8))
a = [random.randint(20,35) for i in range(120)]
x = range(0, 120)
y = a
plt.plot(x, y)

#调整x\y的刻度
_xticks_label = [f"10点{i}分" for i in range(60)]
_xticks_label += [f"11点{i}分" for i in range(60)]
#使得步长，数字的标签一一对应，数据的长度一致
plt.xticks(list(x)[::5], _xticks_label[::5], rotation=45, fontproperties=my_font_axis)
plt.yticks(fontproperties=my_font_axis)

#添加轴标题和总标题
plt.xlabel("时间", fontproperties = my_font_title)
plt.ylabel("温度℃", fontproperties = my_font_title)
plt.title("10点到12点每分钟的气温变化情况", fontproperties = my_font_title)
plt.savefig("./fig_setting.png")
#绘制网格
plt.grid(alpha = 0.2)

plt.show()