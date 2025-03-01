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
img = data.camera()
window1 = np.ones((3,3))/(3**2)
window2 = np.ones((5,5))/(5**2)
window3 = np.ones((9,9))/(9**2)

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
plt.title("(b)3*3_img")

plt.subplot(223)
plt.imshow(img2,cmap="gray")
plt.axis("off")
plt.title("(c)5*5_img")

plt.subplot(224)
plt.imshow(img3,cmap="gray")
plt.axis("off")
plt.title("(d)9*9_img")

plt.show()

