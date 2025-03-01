from skimage import data
from matplotlib import pyplot as plt

img = data.brick()
plt.imshow(img)
plt.show()