from skimage import data, io, exposure
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

image = data.coffee()
image1 = exposure.adjust_gamma(image, 0.2)
image2 = exposure.adjust_gamma(image, 0.67)
image3 = exposure.adjust_gamma(image, 25)


plt.subplot(2,2,1)
plt.title("gamma = 1")
plt.imshow(image)

plt.subplot(2,2,2)
plt.title("gamma = 0.2")
plt.imshow(image1)

plt.subplot(2,2,3)
plt.title("gamma = 0.67")
plt.imshow(image2)

plt.subplot(2,2,4)
plt.title("gamma = 25")
plt.imshow(image3)

plt.show()