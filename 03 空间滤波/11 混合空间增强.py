from skimage import io, filters
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal


def corrl2d (img, window):
    s = signal.correlate(img, window, mode = "same", method = 'auto')
    return s.astype(np.uint8)

#原始图像
img_path = 'D:/软件/软件学习/Python/bonescan.bmp'
img = io.imread(img_path)
# plt.imshow(img)
# plt.show()

window = np.array([[-1,-1,-1],[-1,-8,-1],[-1,-1,-1]])
img_laplace = corrl2d(img, window)
img_laplace = 255 * (img_laplace - img_laplace.min())/(img_laplace.max()-img_laplace.min())
img_laplace_enhance = img + img_laplace

img_sobel = filters.sobel(img)
window_mean = np.ones((5, 5))/(5**2)
img_sobel_mean = corrl2d(img_sobel, window_mean)

img_mask = img_laplace_enhance + img_sobel_mean
img_sharp_enhance = img + img_mask

img_enhance = img_sharp_enhance ** 0.5

#显示图像
imglist = [img, img_laplace, img_laplace_enhance, img_sobel, img_sobel_mean,
           img_mask, img_sharp_enhance, img_enhance]

# for grayimg in imglist:
#     plt.figure()
#     plt.axis("off")
#     plt.imshow(grayimg, cmap='gray')