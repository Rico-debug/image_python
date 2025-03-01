import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from skimage import data
from matplotlib.font_manager import FontProperties

def correl2d (img, window):
    s = signal.correlate(img, window, mode = "same", method = 'auto')
    return s.astype(np.uint8)

img = data.camera()
window = np.ones((3,3))/(3**2)
img_blur = correl2d(img, window)
img_edge = img - img_blur
img_enhanced = img + img_edge

font_set = FontProperties(fname = r"C:\Windows\Fonts\msyh.ttc",size=12)
fig = plt.figure(figsize = (10,8))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title("(a)原始图像",fontproperties = font_set)
plt.subplot(222)
plt.imshow(img_blur, cmap='gray')
plt.title("(b)模糊图像",fontproperties = font_set)
plt.subplot(223)
plt.imshow(img_edge, cmap='gray')
plt.title("(c)边缘图像",fontproperties = font_set)
plt.subplot(224)
plt.imshow(img_enhanced, cmap='gray')
plt.title("(d)锐化图像",fontproperties = font_set)
plt.show()