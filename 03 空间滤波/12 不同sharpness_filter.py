from skimage import data
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

'''
使用滤波器实现图像的空间相关，
mode = same  #输出尺寸=输入尺寸
boundary = fill #表示滤波前，用常数填充图像边缘，默认为0
'''
def correl2d (img, window):
    s = signal.correlate(img, window, mode = "same", method = 'auto')
    return s.astype(np.uint8)

#img为原始图像,图像滤波操作
img = data.coffee()
window1 = np.array(((1, 1, 1), (1, -7, 1), (1, 1, 1)))
window2 = np.array(((1, 1, 1), (1, -8, 1), (1, 1, 1)))
window3 = np.array(((1, 1, 1), (1, -9, 1), (1, 1, 1)))

img1 = correl2d(img, window1)
img2 = correl2d(img, window2)
img3 = correl2d(img, window3)

#生成图像
plt.figure(figsize=(10,8))
plt.subplot(221)
plt.imshow(img)
plt.axis("off")
plt.title("(a)orignal_img")

plt.subplot(222)
plt.imshow(img1)
plt.axis("off")
plt.title("(b)core=-7")


plt.subplot(223)
plt.imshow(img2)
plt.axis("off")
plt.title("(c)core=-8")

plt.subplot(224)
plt.imshow(img3)
plt.axis("off")
plt.title("(d)core=-9")

plt.show()

