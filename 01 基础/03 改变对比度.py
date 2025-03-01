from skimage import data
from matplotlib import pyplot as plt
import numpy as np

def change_alpha(image, a):
    im_change = np.zeros(shape = image.shape,dtype = "uint8")
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                if image[i, j, k]*a > 255:
                    im_change[i, j, k]=255
                elif image[i, j, k]*a < 0:
                    im_change[i, j, k] = 0
                else:
                    im_change[i, j, k] = image[i, j, k]*a
    return im_change

if __name__ == '__main__':
    image1 = data.coffee()
    a = 2
    plt.imshow(change_alpha(image1, a))
    plt.show()
