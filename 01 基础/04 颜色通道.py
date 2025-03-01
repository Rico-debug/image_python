from skimage import data, io
from matplotlib import pyplot as plt
import numpy as np

image = data.coffee()

image_r = image[:,:,0]
image_g = image[:,:,1]
image_b = image[:,:,2]
#展示三个通道

plt.subplot(2,2,1)
io.imshow(image)
plt.subplot(2,2,2)
io.imshow(image_r)
plt.subplot(2,2,3)
io.imshow(image_g)
plt.subplot(2,2,4)
io.imshow(image_b)
plt.show()

