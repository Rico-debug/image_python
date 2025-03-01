from skimage import data,color
from matplotlib import pyplot as plt
import numpy as np

img = data.coffee()
grayimg  = color.rgb2gray(img)
print(grayimg)
plt.subplot(121)
plt.axis("off")
plt.imshow(grayimg,cmap="gray")
rows,cols = grayimg.shape
labels = np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if (grayimg[i, j] < 0.4):
            labels[i, j] = 0
        elif(grayimg[i,j] <0.8):
            labels[i, j] = 1
        else:
            labels[i, j] = 2
psdimg = color.label2rgb(labels)  #不同的灰度区间采用不同颜色
plt.subplot(122)
plt.axis("off")
plt.imshow(psdimg)

plt.show()