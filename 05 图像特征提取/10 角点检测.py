import numpy as np
from skimage import data
from matplotlib import pyplot as plt

def susan_mask():
    mask = np.ones((7,7))
    mask[0,0] = 0
    mask[0,1] = 0
    mask[0,5] = 0
    mask[0,6] = 0
    mask[1,0] = 0
    mask[1,6] = 0
    mask[5,0] = 0
    mask[5,6] = 0
    mask[6,0] = 0
    mask[6,1] = 0
    mask[6,5] = 0
    mask[6,6] = 0
    return mask
print(susan_mask())

def susan_corner_detection(img):
    img =img.astype(np.float64)
    g = 37/2                      #模板内有37个像素，阈值g决定了USAN区域面积的最大值，以及所检测角点的尖锐程度，g值越小，检测到的角点越尖锐。
    circularMask = susan_mask()
    output = np.zeros(img.shape)
    for i in range(3,img.shape[0]-3): #使得模板能够走遍图片（边缘3排）
        for j in range(3,img.shape[1]-3):
            ir = np.array(img[i-3:i+4,j-3:j+4]) #和图片大小一致
            ir = ir[circularMask==1]
            ir0 = img[i,j]
            t = 10 ##阈值t表示所能检测角点的最小对比度，决定了角点提取的数量，t值越小，可提取的角点数量越多。
            a = np.sum(np.exp(-((ir-ir0)/t)**6)) #为什么是sum
            if a<=g:
                a=g-a
            else:
                a=0
            output[i,j]=a
    return output

image = data.camera()
out = susan_corner_detection(image)
plt.imshow(out,cmap='gray')
plt.show()

