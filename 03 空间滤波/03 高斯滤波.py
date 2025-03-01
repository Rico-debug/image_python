from skimage import data
import numpy as np
from scipy import signal
import math
from matplotlib import pyplot as plt

'''
使用滤波器实现图像的空间相关，
mode = same  #输出尺寸=输入尺寸
boundary = fill #表示滤波前，用常数填充图像边缘，默认为0
'''
def correl2d (img, window):
    s = signal.correlate(img, window, mode = "same", method = 'auto')
    return s.astype(np.uint8)

#定义二维高斯函数
def guass(i,j,sigma):
    return 1/(2*math.pi*sigma**2) * math.exp(-(i**2+j**2)/2*sigma**2)

#定义radius x radius 的高斯平滑模板
def guass_window(radius, sigma):
    window = np.zeros((radius, radius))
    r = int((radius - 1) / 2)
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            window[i + r][j + r] = guass(i, j, sigma)
    return window / np.sum(window)

#原始图像和高斯模板
img = data.camera()
window1 = guass_window(3, 1)
window2 = guass_window(5, 1)
window3 = guass_window(9, 1)
img1 = correl2d(img, window1)
img2 = correl2d(img, window2)
img3 = correl2d(img, window3)

#生成图像
plt.figure(figsize=(10,8))
plt.subplot(221)
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("(a)orignal_img")

plt.subplot(222)
plt.imshow(img1,cmap="gray")
plt.axis("off")
plt.title("(b)3*3_guass_img")

plt.subplot(223)
plt.imshow(img2,cmap="gray")
plt.axis("off")
plt.title("(c)5*5_guass_img")

plt.subplot(224)
plt.imshow(img3,cmap="gray")
plt.axis("off")
plt.title("(d)9*9_guass_img")

plt.show()