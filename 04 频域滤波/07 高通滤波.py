from skimage import data,color
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False

set_ch()

new_img = data.coffee()
new_img = color.rgb2gray(new_img)
f1 = np.fft.fft2(new_img)
f1_shift = np.fft.fftshift(f1)
f1_img = np.log(np.abs(f1_shift))
#理想低通滤波器
rows,cols = new_img.shape
crow, ccol = int(rows/2),int(cols/2) #计算频谱中心
mask = np.zeros((rows,cols),np.uint8)
D = 50
for i in range(rows):
    for j in range(cols):
        if np.sqrt(i*i+j*j)<= D:
            mask[crow-D:crow+D, ccol-D: ccol+D] = 1
f1_shift = f1_shift * (1-mask)  #将mask
f2_img = np.log(np.abs(f1_shift))
#傅里叶逆变换
f_ishift = np.fft.ifftshift(f1_shift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
img_back = (img_back - np.amin(img_back)) / (np.amax(img_back)-np.amin(img_back)) #调整大小范围便于显示

#展示
plt.subplot(221), plt.imshow(new_img, cmap="gray"), plt.title("原始图像")
plt.subplot(222), plt.imshow(f1_img, "gray"), plt.title("原始图像傅里叶")
plt.subplot(223), plt.imshow(img_back, cmap="gray"), plt.title("低通滤波后图像")
plt.subplot(224), plt.imshow(f2_img, "gray"), plt.title("低通滤波后傅里叶")
plt.show()
