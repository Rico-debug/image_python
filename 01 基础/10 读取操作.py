from skimage import io
from matplotlib import pyplot as plt
import numpy as np

img_path = 'D:\图片\壁纸\wallhaven-48k95j.jpg'
image = io.imread(img_path)
plt.imshow(image)
plt.show()
#颜色通道
# image_r = image[:,:,0]
# image_g = image[:,:,1]
# image_b = image[:,:,2]
#
# plt.subplot(221)
# plt.imshow(image)
# plt.subplot(222)
# plt.imshow(image_r,cmap='gray')
# plt.subplot(223)
# plt.imshow(image_g,cmap='gray')
# plt.subplot(224)
# plt.imshow(image_b,cmap='gray')
# plt.show()

#采样率
ratio = 2

image_tmp = np.zeros((int(image.shape[0]/ratio),
                  int(image.shape[1]/ratio),
                  image.shape[2]),dtype="int32")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            delta = image[i * ratio:(i + 1) * ratio, j * ratio:(j + 1) * ratio, k]
            image_tmp[i,j,k] = np.mean(delta)
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image_tmp)
plt.show()


