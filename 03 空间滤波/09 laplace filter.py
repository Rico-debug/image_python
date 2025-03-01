from skimage import data, filters
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

img = data.camera()

#拉普拉斯算子
img_laplace = filters.laplace(img, ksize=3, mask=None)

#显示图像
#设置格式
font_set = FontProperties(fname = r"C:\Windows\Fonts\msyh.ttc",size=12)
fig = plt.figure(figsize = (10,8))

plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title("(a)原始图像",fontproperties = font_set)
plt.subplot(132)
plt.imshow(img_laplace, cmap='gray')
plt.title("(b)拉普拉斯图像",fontproperties = font_set)
plt.subplot(133)
plt.imshow(img + img_laplace, cmap='gray')
plt.title("(c)锐化增强图像",fontproperties = font_set)
plt.show()