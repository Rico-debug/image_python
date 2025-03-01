from skimage import data, filters
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

img = data.camera()

#sobel算子
img_sobel_h = filters.sobel_h(img)
img_sobel_v = filters.sobel_v(img)
img_sobel = filters.sobel(img)

#显示图像
#设置格式
font_set = FontProperties(fname = r"C:\Windows\Fonts\msyh.ttc",size=12)
fig = plt.figure(figsize = (10,8))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title("(a)原始图像",fontproperties = font_set)
plt.subplot(232)
plt.imshow(img_sobel_h, cmap='gray')
plt.title("(b)sobel_h",fontproperties = font_set)
plt.subplot(233)
plt.imshow(img_sobel_v, cmap='gray')
plt.title("(c)sobel_V",fontproperties = font_set)
plt.subplot(234)
plt.imshow(img_sobel, cmap='gray')
plt.title("(d)sobel_img",fontproperties = font_set)
plt.subplot(235)
plt.imshow(50*img_sobel+img, cmap='gray')
plt.title("(e)叠加图片",fontproperties = font_set)
plt.show()