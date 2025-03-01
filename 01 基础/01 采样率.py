from skimage import data
from matplotlib import pyplot as plt
import numpy as np

image = data.coffee()
print(image.shape)
print(type(image))

ratio = 50
image1 = np.zeros((int(image.shape[0]/ratio),
                  int(image.shape[1]/ratio),
                  image.shape[2]),dtype="int32")

for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            delta = image[i*ratio:(i+1)*ratio, j*ratio:(j+1)*ratio, k]
            image1[i, j, k] = np.mean(delta)


plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image1)
plt.show()


