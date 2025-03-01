from skimage import data, io, filters
from matplotlib import pyplot as plt
import numpy as np

#图像空间滤波函数
#img为原始图像，img1为拓展图像，img2为滤波后图像
def corrl2d(img, window):
    m = window.shape[0]
    n = window.shape[1]
    #边界通过加0拓展
    #img1为原始图像拓展，window为滤波模板,img2为空间滤波结果
    img1 = np.zeros((img.shape[0]+m-1,img.shape[1]+n-1))
    img1[(m-1)//2 : (img.shape[0] + (m-1)//2),(n-1)//2 : (img.shape[1] + (n-1)//2)] = img
    img2 = np.zeros(img.shape)
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            temp = img1[i : i+m, j : j+n]
            img2[i, j] = np.sum(np.multiply(temp, window))  #乘积之和为结果矩阵中的一个元素
    return img2

img = io.imread('D:/软件/软件学习/Python/bonescan.bmp',as_gray= True)

#laplace滤波
window1 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
img_laplace = corrl2d(img, window1)
img_laplace = 255 * (img_laplace - img_laplace.min())/(img_laplace.max() - img_laplace.min())
img_laplace_enhanced = img + img_laplace

#sobel + 5*5均值平滑
img_sobel = filters.sobel(img)
window2 = np.ones((5,5))/(5**2)
img_sobel_mean = corrl2d(img_sobel, window2)

#生成掩蔽图像
img_mask = img_laplace_enhanced * img_sobel_mean

#生成锐化增强图像
img_sharp_enhanced= img + img_mask

#gamma
img_enhaced = img_sharp_enhanced ** 0.5

#图像显示
plt.figure(figsize=(10,8))
img_list = [img, img_laplace, img_laplace_enhanced, img_sobel, img_sobel_mean
            ,img_mask, img_sharp_enhanced,img_enhaced]
plt.subplot(241)
plt.axis("off")
plt.title("(a)oringnal_img")
plt.imshow(img, cmap="gray")
plt.subplot(242)
plt.axis("off")
plt.title("(b)img_laplace")
plt.imshow(img_laplace, cmap="gray")
plt.subplot(243)
plt.axis("off")
plt.title("(c)img_laplace_enhanced")
plt.imshow(img_laplace_enhanced, cmap="gray")
plt.subplot(244)
plt.axis("off")
plt.title("(d)img_sobel")
plt.imshow(img_sobel, cmap="gray")
plt.subplot(245)
plt.axis("off")
plt.title("(e)img_sobel_mean")
plt.imshow(img_sobel_mean, cmap="gray")
plt.subplot(246)
plt.axis("off")
plt.title("(f)img_mask")
plt.imshow(img_mask, cmap="gray")
plt.subplot(247)
plt.axis("off")
plt.title("(g)img_sharp_enhanced")
plt.imshow(img_sharp_enhanced, cmap="gray")
plt.subplot(248)
plt.axis("off")
plt.title("(h)img_enhanced")
plt.imshow(img_enhaced, cmap="gray")

plt.show()



