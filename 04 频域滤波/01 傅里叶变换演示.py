import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
#中文显示函数
def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False

set_ch()

def show(ori_fuc,ft, sampling_period = 5 ):
    n = len(ori_fuc)
    interval = sampling_period / n
    #绘制原始图像
    plt.figure(figsize=(10,12))
    plt.subplot(211)
    plt.plot(np.arange(0, sampling_period, interval), ori_fuc, 'black')
    plt.xlabel('时间'),plt.ylabel('振幅')
    plt.title('原始信号')

    #绘制变换之后的函数
    plt.subplot(212)
    frequency = np.arange(n/2) / (n * interval)  #????
    # print(frequency)
    nfft = abs(ft[range(int(n/2))] / n)
    plt.plot(frequency, nfft, 'red')
    plt.xlabel('频率/Hz'), plt.ylabel('频谱')
    plt.title('傅里叶变换结果')
    plt.show()

#生成频率=1（角速度为2Pi）的正弦
time = np.arange(0, 5, .005)
x = np.sin(2*np.pi*1*time)
x2 = np.sin(2*np.pi*20*time)*2
x3 = np.sin(2*np.pi*60*time)
x += x2 + x3
y = np.fft.fft(x)
show(x, y)

#生成方波，振幅=1，频率=10Hz
#interval = 0.05s, 200 points/s
x = np.zeros(len(time))
x[::20] = 1
y = np.fft.fft(x)
show(x, y)

#生成脉冲波
x = np.zeros(len(time))
x[380:400] = np.arange(0, 1, 0.05)
x[400:420] = np.arange(1, 0, -0.05)
y = np.fft.fft(x)
show(x, y)



