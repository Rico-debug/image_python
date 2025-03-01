import skimage.feature
import skimage.segmentation
import matplotlib.pyplot as plt
from skimage import data

img = data.coffee()
for color_channel in (0,1,2):
    img[:,:,color_channel] = skimage.feature.local_binary_pattern(
        img[:,:,color_channel],8,1,method='var'
    )
plt.imshow(img)
plt.show()