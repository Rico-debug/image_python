import numpy as np
from skimage import data, util
from scipy import ndimage
import math
from matplotlib import pyplot as plt

img = data.astronaut()
noise_img = np.zeros(img.shape)
new_img = np.zeros(img.shape)

for i in range(3):
    grayimg = data.astronaut()[:,:,i]
    #对图像加入椒盐噪声
    noise_img[:,:,i] = util.random_noise(grayimg,mode="s&p",seed=None,clip=True)

    #中值滤波
    n = 3
    new_img[:,:,i] = ndimage.median_filter(noise_img[:,:,i],size = (n,n))

#显示图像
plt.figure(figsize=(10,8))
plt.subplot(131)
plt.title("(a)original_img")
plt.imshow(img, cmap="gray")
plt.subplot(132)
plt.title("(b)noise_img")
plt.imshow(noise_img, cmap="gray")
plt.subplot(133)
plt.title("(c)new_img")
plt.imshow(new_img, cmap="gray")
plt.show()
