from skimage import data,color
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl
img = data.coffee()
img1 = img
img = color.rgb2gray(img)

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False

set_ch()

#在x方向实现傅里叶变换
m,n = img.shape
fx = img
for y in range(n):
    fx[:,y] = np.fft.fft(img[:,y])
for x in range(m):
    fx[x,:] = np.fft.fft(img[x,:])
fshift = np.fft.fftshift(fx)
fimg = np.log(np.abs(fshift))

#显示结果
plt.subplot(121),plt.imshow(img1, 'gray'), plt.title('原始图像')
plt.subplot(122),plt.imshow(fimg, 'gray'), plt.title('两次一维傅里叶')
plt.show()
