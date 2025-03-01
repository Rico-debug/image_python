from matplotlib import pyplot as plt
from skimage import data
from skimage.filters import laplace, gaussian

image = data.camera()
edge_laplace = laplace(image)
gaussian_image = gaussian(image)
edge_LoG = laplace(gaussian_image)
fig, ax =plt.subplots(ncols=2,nrows=2,sharex=True,sharey=True,figsize=(8,6))
ax[0,0].imshow(image, cmap='gray')
ax[0,0].set_title('original_img')
ax[0,1].imshow(edge_laplace,cmap='gray')
ax[0,1].set_title('laplace_edge')
ax[1,0].imshow(gaussian_image,cmap='gray')
ax[1,0].set_title('gaussian_image')
ax[1,1].imshow(edge_LoG,cmap='gray')
ax[1,1].set_title('LoG_edge')

for a in ax:
    for j in a:
        j.axis('off')
plt.tight_layout()
plt.show()