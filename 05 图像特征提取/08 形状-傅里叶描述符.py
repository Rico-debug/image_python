import numpy as np
from matplotlib import pyplot as plt
from skimage import data,measure

#构建测试数据
x, y = np.ogrid[-np.pi:np.pi:100j,-np.pi:np.pi:100j]
r = np.sin(np.exp((np.sin(x)**3+np.cos(y)**2)))

#找出轮廓边界
contours = measure.find_contours(r,0.8)
#显示对应边界
fig,ax = plt.subplots()
ax.imshow(r,interpolation='nearest',cmap=plt.cm.gray)
for n, contour in enumerate(contours):
    ax.plot(contour[:,1],contour[:,0],linewidth = 2)
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

#提取傅里叶形状描述符
contour_array = contour
contour_complex = np.empty(contour_array.shape[:-1],dtype=complex)
contour_complex.real = contour_array[:,0]
contour_complex.imag = contour_array[:,1]
fourier_result = np.fft.fft(contour_complex)
print(fourier_result.shape)
