import matplotlib.pyplot as plt
#设置图片大小
fig = plt.figure(figsize = (12,8), dpi = 80)
#绘图
x = range(2, 18, 2)
y = [4, 6, 7, 5, 5, 9, 14, 12]
plt.plot(x, y)
#一些设置
plt.xticks(range(10, 18),)
plt.yticks(range(min(y), max(y)+1))
#保存
plt.savefig("./sig_size.png")
#展示
plt.show()