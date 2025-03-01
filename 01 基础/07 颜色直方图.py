from skimage import data, io, exposure
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

image = data.coffee()

hist_r = exposure.histogram(image[:,:,0],nbins=256)
hist_g = exposure.histogram(image[:,:,1],nbins=256)
hist_b = exposure.histogram(image[:,:,2],nbins=256)

plt.figure(figsize=(20,8))
plt.subplot(221)
plt.title("(a)picture")
plt.imshow(image)

plt.subplot(222)
plt.title("(b)hist_r")
plt.hist(hist_r,bins=256,edgecolor="None",facecolor="red")

plt.subplot(223)
plt.title("(c)hist_g")
plt.hist(hist_g,bins=256,edgecolor="None",facecolor="green")

plt.subplot(224)
plt.title("(d)hist_b")
plt.hist(hist_b,bins=256,edgecolor="None",facecolor="blue")

plt.show()