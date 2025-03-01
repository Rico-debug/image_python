from skimage import data, util
from scipy import ndimage
import math
from matplotlib import pyplot as plt


img = data.astronaut()[:,:,0]
#加入噪声
noise_img = util.random_noise(img, mode = 's&p',seed = None, clip = True)

#中值滤波
n = 3
new_img = ndimage.median_filter(noise_img,size = (3,3))

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

