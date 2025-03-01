import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi
from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel
from pylab import mpl

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
set_ch()

def compute_feats(image,kernels):
    feats = np.zeros(len(kernels),2,dtype=np.double)
    for k,kernal in enumerate(kernels):
        filtered = ndi.convolve(image,kernal,mode='wrap')
        feats[k,0] = filtered.mean()
        feats[k,1] = filtered.var()
    return feats

def match(feats,ref_feats):
    min_error = np.inf
    min_i = None
    for i in range(ref_feats.shape[0]):
        error = np.sum((feats-ref_feats[i,:])**2)
    if error < min_error:
        min_error = error
        min_i = i
    return min_i

#准备Gabor卷积核
kernels = []
for theta in range(4):
    theta = theta/4 * np.pi
    for sigma in (1,3):
        for frequency in (0.05,0.25):
            kernel = np.real(gabor_kernel(frequency,theta = theta,sigma_x=sigma,sigma_y=sigma))
            kernels.append(kernel)
shrink = (slice(0,None,3),slice(0,None,3))
brick = img_as_float(data.load('brick.png'))[shrink]
grass = img_as_float(data.load('grass.png'))[shrink]
wall = img_as_float(data.load('rough-wall.png'))[shrink]
image_names = ('砖块','草地','墙壁')
images = (brick,grass,wall)

#准备参考特征
ref_feats = np.zeros((3,len(kernels),2),dtype=np.double)
ref_feats[0,:,:] = compute_feats(brick, kernels)
ref_feats[1,:,:] = compute_feats(grass, kernels)
ref_feats[2,:,:] = compute_feats(wall, kernels)
