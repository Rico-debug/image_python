from skimage import data,exposure
from matplotlib import pyplot as plt


img = data.coffee()
channel_R = exposure.histogram(img[:,:,0],nbins = 255,normalize=True)
channel_G = exposure.histogram(img[:,:,1],nbins = 255,normalize=True)
channel_B = exposure.histogram(img[:,:,2],nbins = 255,normalize=True)
# print(channel_R)
plt.figure(figsize=(10,8))
plt.subplot(221)
plt.imshow(img)
plt.title('original_img')
plt.subplot(222)
plt.bar(channel_R[1],channel_R[0],color = 'red')
plt.title("R_hist")
plt.subplot(223)
plt.bar(channel_G[1],channel_B[0],color = 'green')
plt.title("g_hist")
plt.subplot(224)
plt.bar(channel_B[1],channel_B[0],color = 'blue')
plt.title("b_hist")
plt.show()