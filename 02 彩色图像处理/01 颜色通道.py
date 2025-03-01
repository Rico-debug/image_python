from skimage import data
from matplotlib import pyplot as plt

image = data.coffee()
plt.axis("off")
plt.subplot(221)
plt.imshow(image)
plt.title("original")


imageR = image[:,:,0]
plt.axis("off")
plt.subplot(222)
plt.imshow(imageR,cmap="gray")
plt.title("Red")

imageG = image[:,:,1]
plt.axis("off")
plt.subplot(223)
plt.imshow(imageG,cmap="gray")
plt.title("Green")


imageB = image[:,:,2]
plt.axis("off")
plt.subplot(224)
plt.imshow(imageB,cmap="gray")
plt.title("Blue")

plt.show()
