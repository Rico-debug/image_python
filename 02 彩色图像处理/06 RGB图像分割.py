from skimage import data
from matplotlib import pyplot as plt
import math
import numpy as np
import sys

image = data.colorwheel()
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

#选择样本区域
r1 = r[128:255, 85:169]  #定义红色
r1_u = np.mean(r1)
#计算样本点红色分量的标准差
r1_d = 0.0
for i in range(r1.shape[0]):
    for j in range(r1.shape[1]):
        r1_d = r1_d + (r1[i, j]-r1_u)*(r1[i, j]-r1_u)
r1_d = math.sqrt(r1_d/r1.shape[0]/r1.shape[1])

#寻找符合条件的点，r2为红色分割图像
r2 = np.zeros(r.shape, dtype = "uint8")
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r[i, j] >= (r1_u - 1.25 * r1_d) and r[i, j] <= (r1_u + 1.25 * r1_d):
            r2[i, j] = 1
#image2为根据红色分割后的RGB图像
image2 = np.zeros(image.shape, dtype = "uint8")
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r2[i, j] == 1:
            image2[i, j, :] = image[i, j, :]

#显示结果
plt.figure(figsize=(12,8))
plt.subplot(231)
plt.imshow(image)
plt.title("(a)original_img")

plt.subplot(232)
plt.imshow(r, cmap="gray")
plt.title("(b)R_channel")

plt.subplot(233)
plt.imshow(g)
plt.title("(c)G_channel")

plt.subplot(234)
plt.imshow(b)
plt.title("(d)B_channel")

plt.subplot(235)
plt.imshow(r2, cmap="gray")
plt.title("(e)split_img")

plt.subplot(236)
plt.imshow(image2, cmap="gray")
plt.title("(f)result_img")

plt.show()