import numpy as np
from skimage import data, util
from scipy import ndimage
import math
from matplotlib import pyplot as plt

img = data.astronaut()[:,:,0]
#加入pepper噪声
pepper_img = util.random_noise(img, mode = 'pepper',seed = None, clip = True)
#加入salt噪声
salt_img = util.random_noise(img, mode = 'salt',seed = None, clip = True)

n = 3
#最大值滤波
max_img = ndimage.maximum_filter(pepper_img,size = (n,n))
#最小值滤波
min_img = ndimage.minimum_filter(salt_img,size = (n,n))


#显示图像
plt.figure(figsize=(10,8))
plt.subplot(231)
plt.title("(a)original_img")
plt.imshow(img, cmap="gray")
plt.subplot(232)
plt.title("(b)pepper_img")
plt.imshow(pepper_img, cmap="gray")
plt.subplot(233)
plt.title("(c)salt_img")
plt.imshow(salt_img, cmap="gray")

plt.subplot(235)
plt.title("(d)max_img")
plt.imshow(max_img, cmap="gray")
plt.subplot(236)
plt.title("(e)min_img")
plt.imshow(min_img, cmap="gray")
plt.show()
