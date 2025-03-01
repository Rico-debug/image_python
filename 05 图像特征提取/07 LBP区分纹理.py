'''
基于二值模式的图像纹理分类
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi
from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel
from pylab import mpl
Method ='uniform'

def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
set_ch()

def plot_circle(ax,center,radius,color):
    circle = plt.Circle(center,radius,facecolor=color, edgecolor='0.5')
    ax.add_patch(circle)

def plot_lbp_model(ax,binary_values):
    '''LBPf方法模型绘制'''
    #Geometry spec
    theta = np.deg2rad(45)
    R = 1
    r = 0.15
    w = 1.5
    gray = '0.5'
    #Draw the center pixel
    plot_circle(ax,(0,0),radius=r,color=gray)
    #Draw the surrounding pixels
    for i ,facecolor in enumerate(binary_values):
        x = R * np.cos(i*theta)
        y = R * np.sin(i*theta)
        plot_circle(ax,(x,y),radius=r,color=str(facecolor))
    #Draw the pixel grid
    for x in np.linspace(-w,w,4):
        ax.axvline(x,color = gray)
        ax.axhline(x,color = gray)
    #tweak the layout
    ax.axis('image')
    ax.axis('off')
    size = w + 0.2
    ax.set_xlim(-size,size)
    ax.set_ylim(-size,size)

fig, axes = plt.subplots(ncols=5,figsize=(7,2))
titles = ['flat','flat','edge','corner','non-uniform']
binary_patterns = [np.zeros(8),
                   np.ones(8),
                   np.hstack([np.ones(4),np.zeros(4)]),
                   np.hstack([np.zeros(3),np.ones(5)]),
                   [1,0,0,1,1,1,0,0]]
for ax, values, name in zip(axes,binary_patterns,titles):
    plot_lbp_model(ax, values)
    ax.set_title(name)

#二值模式特征提取
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb

#settings for LBP
radius  = 3
n_points =8*radius
def overlay_labels(image,lbp,labels):
    mask = np.logical_or.reduce([lbp == each for each in labels])
    return label2rgb(mask,image = image,bg_label=0,alpha=0.5)

def highlight_bars(bars,indexes):
    for i in indexes:
        bars[i].set_facecolor('r')

image =data.brick()
lbp = local_binary_pattern(image,n_points,radius,Method)

def hist(ax,lbp):
    n_bins = int(lbp.max()+1)
    return ax.hist(lbp.ravel(),density =True,bins=n_bins, range = (0,n_bins),facecolor='0.5')

#绘制LBP直方图
fig, (ax_img, ax_hist) = plt.subplots(nrows=2,ncols=3,figsize=(9,6))
plt.gray()
titles = ('edge','flat','corner')
w = width = radius -1
edge_labels = range(n_points//2-w,n_points//2+w+1)
flat_labels  = list(range(0,w+1))+list(range(n_points-w,n_points+2))

i_14 = n_points//4
i_34 = 3*(n_points//4)
corner_labels = (list(range(i_14-w,i_14 +w+1))+list(range(i_34-w,i_34+w+1)))
label_sets = (edge_labels,flat_labels,corner_labels)
for ax,labels in zip(ax_img,label_sets):
    ax.imshow(overlay_labels(image,lbp,labels))
for ax,labels,name in zip(ax_hist,label_sets,titles):
    counts,_,bars = hist(ax,lbp)
    highlight_bars(bars,labels)
    ax.set_ylim(top=np.max(counts[:-1]))
    ax.set_xlim(right=n_points + 2)
    ax.set_title(name)
ax_hist[0].set_ylabel('Percentage')
for ax in ax_img:
    ax.axis('off')

#使用LBP对图像纹理分类
radius = 2
n_points = 8*radius
def kullback_leibler_divergence(p,q):
    p = np.asarray(p)
    q = np.asarray(q)
    filt = np.logical_and(p!=0,q!=0)
    return np.sum(p[filt]*np.log2(p[filt]/q[filt]))
def match(refs,img):
    best_socre =10
    best_name = None
    lbp = local_binary_pattern(img, n_points, radius,Method)
    n_bins = int(lbp.max()+1)
    hist,_ = np.histogram(lbp, density=True,bins=n_bins,range=(0,n_bins),)
    for name,ref in refs.items():
        ref_hist,_ = np.histogram(ref,density=True,bins=n_bins,range=(0,n_bins))
    score = kullback_leibler_divergence(hist, ref_hist)
    if score < best_socre:
        best_socre = score
        best_name = name
    return best_name

brick = data.brick()
grass = data.grass()
cell = data.cell()
refs = {
    'brick':local_binary_pattern(brick, n_points,radius,Method),
    'grass':local_binary_pattern(grass, n_points,radius,Method),
    'cell':local_binary_pattern(cell, n_points,radius,Method)
}

#绘制LBP纹理直方图
fig,((ax1,ax2,ax3),(ax4,ax5,ax6)) =plt.subplots(nrows=2,ncols=3,figsize=(9,6))
plt.gray()
ax1.imshow(brick)
ax1.axis('off')
hist(ax4,refs['brick'])
ax4.set_ylabel('Percentage')

ax2.imshow(grass)
ax2.axis('off')
hist(ax5,refs['grass'])
ax5.set_xlabel('Uniform LBP values')

ax3.imshow(cell)
ax3.axis('off')
hist(ax6,refs['cell'])
plt.show()



