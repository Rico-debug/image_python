from skimage import data
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False

set_ch()

img = data.checkerboard()
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f) #默认结果中心点左上角转为图片中心位置
fimg = np.log(np.abs(fshift)) #结果是复数，求绝对值才是振幅

#展示结果
plt.subplot(121), plt.imshow(img,'gray'), plt.title('原始图像')
plt.subplot(122), plt.imshow(fimg,'gray'), plt.title('傅里叶频谱')
plt.show()
print()