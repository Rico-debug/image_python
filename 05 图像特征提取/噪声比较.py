from matplotlib import pyplot as plt
from skimage import data,io
from skimage.feature import graycoprops, graycomatrix
from pylab import mpl
import numpy as np

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
set_ch()

#计算灰度共生矩阵相似性
xhigh = []
yhigh = []
img_high_frequency = io.imread("D:\+++芯片测试\红蓝色点、色噪\色噪图片\色噪、团噪图片整理\GC8613 VS IMX415 Raw图\IMX415_80℃_遮黑_good_gray.bmp")
glcm1 = graycomatrix(img_high_frequency,[5],[0],256,symmetric=True,normed=True)
xhigh.append(graycoprops(glcm1, prop='dissimilarity')[0,0])
yhigh.append(graycoprops(glcm1, prop='correlation')[0,0])

xlow = []
ylow = []
img_low_frequency = io.imread("D:\+++芯片测试\红蓝色点、色噪\色噪图片\色噪、团噪图片整理\GC8613 VS IMX415 Raw图\GC8613_80℃_遮黑_bad_gray.bmp")
glcm2 = graycomatrix(img_low_frequency,[5],[0],256,symmetric=True,normed=True)
xlow.append(graycoprops(glcm2, prop='dissimilarity')[0,0])
ylow.append(graycoprops(glcm2, prop='correlation')[0,0])

# # 计算std
std_high = np.std(img_high_frequency)
std_low = np.std(img_low_frequency)

# #显示图像
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(2,2,1)
ax.imshow(img_high_frequency,cmap = 'gray')
ax.set_title("IMX415")
ax = fig.add_subplot(2,2,2)
plt.imshow(img_low_frequency,cmap = 'gray')
ax.set_title("GC8613")

ax = fig.add_subplot(2,2,3)
ax.bar("IMX415",std_high,width=0.3)
ax.bar("GC8613",std_low,width=0.3)
ax.set_title("图像std")


ax = fig.add_subplot(2,2,4)
ax.plot(xhigh,yhigh,'bo', label = "IMX415")
ax.plot(xlow,ylow,'go', label = "GC8613")
ax.set_title("灰度共生矩阵分析")
ax.set_xlabel('灰度共生矩阵相似性')
ax.set_ylabel('灰度共生矩阵相关性')
ax.legend()
plt.show()
