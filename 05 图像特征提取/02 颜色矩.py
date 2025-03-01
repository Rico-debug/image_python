from skimage import data,io
import numpy as np
from scipy import stats

features = np.zeros((3,3))
img =data.coffee()

for k in range(img.shape[2]):
    mu = np.mean(img[:,:,k])
    detla = np.std(img[:,:,k])
    skew = np.mean(stats.skew(img[:,:,k]))
    features[0,k] = mu
    features[1,k] = detla
    features[2,k] = skew

print(features)