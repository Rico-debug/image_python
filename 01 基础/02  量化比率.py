from skimage import data
from matplotlib import pyplot as plt
import numpy as np

image = data.coffee()
print(image)
print(type(image))
ratio = 64
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            image[i][j][k] = int(image[i][j][k]*ratio)/8


plt.imshow(image)
plt.show()

