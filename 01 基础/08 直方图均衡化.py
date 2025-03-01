from skimage import data, io, exposure
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

img = data.moon()
arr = img.flatten()  #将二维ndarray降至一维
#设置图像
plt.figure(figsize=(10,6))
#原始图像
plt.subplot(221)
plt.imshow(img,plt.cm.gray)
#原始图像直方图
plt.subplot(222)
plt.hist(arr,bins=256,density=True,edgecolor="None",facecolor="black")

#图像均衡
img1 =exposure.equalize_hist(img)
arr1 = img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)
#图像均衡的直方图
plt.subplot(224)
plt.hist(arr1,bins=256,density=True,edgecolor="None",facecolor="black")

plt.show()