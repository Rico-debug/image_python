from skimage import data,color
from matplotlib import pyplot as plt
import numpy as np

#定义灰度值到彩色变换
L = 255
def GetR(gray):
    if gray < L/2:
        return 0
    elif gray > L/4*3:
        return L
    else:
        return 4*gray - 2*L

def GetG(gray):
    if gray < L/4:
        return 4*gray
    elif gray > L/4*3:
        return 4*L - 4*gray
    else:
        return L

def GetB(gray):
    if gray < L/4:
        return L
    elif gray > L/2:
        return 0
    else:
        return 2*L - 4*gray

img = data.coffee()
grayimg = color.rgb2gray(img)*255
colorimg = np.zeros(img.shape, dtype = "uint8")
for ii in range(img.shape[0]):
    for jj in range(img.shape[1]):
        r,g,b = GetR(grayimg[ii,jj]),GetG(grayimg[ii,jj]),GetB(grayimg[ii,jj])
        colorimg[ii,jj,:] = (r,g,b)

plt.subplot(121)
plt.axis("off")
plt.imshow(grayimg,cmap="gray")
plt.subplot(122)
plt.axis("off")
plt.imshow(colorimg)
plt.show()