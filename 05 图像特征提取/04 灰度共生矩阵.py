from skimage import data
from skimage.feature import graycomatrix,graycoprops
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
set_ch()

patch_size = 21
img = data.camera()

#选取图像中的草地块
grass_locations =[(400,170),(454,329),(390,380),(400,470)]
grass_patches = []
for loc in grass_locations:
    grass_patches.append(img[loc[0]:loc[0]+patch_size,loc[1]:loc[1]+patch_size])
#选取图像中的天空块
sky_locations =[(60,60),(60,300),(100,368),(50,460)]
sky_patches = []
for loc in sky_locations:
    sky_patches.append(img[loc[0]:loc[0]+patch_size,loc[1]:loc[1]+patch_size])

#计算每个灰度块的共生矩阵
xg = []
yg = []
for patches in grass_patches:
    glcm = graycomatrix(patches, [10], [0],symmetric=True,normed=True)
    xg.append(graycoprops(glcm,'dissimilarity')[0,0])
    yg.append(graycoprops(glcm,'correlation')[0,0])
xs = []
ys = []
for patches in sky_patches:
    glcm = graycomatrix(patches, [10], [0],symmetric=True,normed=True)
    xs.append(graycoprops(glcm,'dissimilarity')[0,0])
    ys.append(graycoprops(glcm,'correlation')[0,0])

#展示结果
#展示图像和取样块
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(321)
ax.imshow(img,cmap='gray')
for (y,x) in grass_locations:
    ax.plot(x+patch_size/2,y+patch_size/2,'gs')
for (y,x) in sky_locations:
    ax.plot(x+patch_size/2,y+patch_size/2,'bs')
ax.set_xlabel("原始图像")
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')

#展示共生矩阵值
ax = fig.add_subplot(322)
ax.plot(xg,yg,'go',label='Grass')
ax.plot(xs,ys,'bo',label='sky')
ax.set_xlabel("glcm_dissimilarity")
ax.set_ylabel("glcm_correlation")
ax.legend()
#展示灰度块
for i,patches in enumerate(grass_patches):
    ax  = fig.add_subplot(3,len(grass_patches),len(grass_patches)*1+i+1)
    ax.imshow(patches,cmap='gray',interpolation='nearest',vmin=0,vmax=255)
    ax.set_xlabel('Grass%d'%(i+1))
for i,patches in enumerate(sky_patches):
    ax  = fig.add_subplot(3,len(grass_patches),len(grass_patches)*2+i+1)
    ax.imshow(patches,cmap='gray',interpolation='nearest',vmin=0,vmax=255)
    ax.set_xlabel('Sky%d'%(i+1))

plt.suptitle("GLCM_features")
plt.show()
