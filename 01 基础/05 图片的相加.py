from skimage import data, io
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

#设置格式
font_set = FontProperties(fname = r"C:\Windows\Fonts\simsun.ttc",size=16)
fig = plt.figure(figsize = (10,8))
#图像运算
moon = data.moon()
camera = data.camera()
image_minus = moon - camera
image_plus = moon + camera

#设置图像
plt.set_cmap(cmap="gray")
plt.subplot(2,2,1)
plt.title("(a)moon",fontproperties = font_set)
plt.imshow(moon)

plt.subplot(2,2,2)
plt.title("(b)camera",fontproperties = font_set)
plt.imshow(camera)

plt.subplot(2,2,3)
plt.title("(c)plus",fontproperties = font_set)
plt.imshow(image_plus)

plt.subplot(2,2,4)
plt.title("(d)minus",fontproperties = font_set)
plt.imshow(image_minus)

plt.show()