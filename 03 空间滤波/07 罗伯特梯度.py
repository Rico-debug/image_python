from skimage import data, filters
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

img = data.camera()

#罗伯特交叉梯度算子
img_robert_pos = filters.roberts_pos_diag(img)
img_robert_neg = filters.roberts_neg_diag(img)
img_robert = filters.roberts(img)

#显示图像
#设置格式
font_set = FontProperties(fname = r"C:\Windows\Fonts\msyh.ttc",size=12)
fig = plt.figure(figsize = (10,8))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title("(a)原始图像",fontproperties = font_set)
plt.subplot(232)
plt.imshow(img_robert_pos, cmap='gray')
plt.title("(b)正对角线边缘图像",fontproperties = font_set)
plt.subplot(233)
plt.imshow(img_robert_neg, cmap='gray')
plt.title("(c)负对角线边缘图像",fontproperties = font_set)
plt.subplot(234)
plt.imshow(img_robert, cmap='gray')
plt.title("(d)罗伯特梯度图",fontproperties = font_set)
plt.subplot(235)
plt.imshow(5*img_robert+img, cmap='gray')
plt.title("(e)叠加图片",fontproperties = font_set)
plt.show()