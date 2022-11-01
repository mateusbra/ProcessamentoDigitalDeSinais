import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz

entrada = np.fromfile("sweep.pcm", dtype='int16')

fs = 8000
fchz = 400
fc = fchz/fs#400/8000
M = 100
BLACKMAN = np.array([])
HAMMING = np.array([])
for i in range(0,M):
    #HAMMING
    coeficiente =   (0.54 - 0.46 * np.cos(2*np.pi*i/M)) #H[I%] = H[I%] * (0.54 - 0.46*COS(2*PI*I%/M%) )
    #BLACKMAN
    coeficiente =   (0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M))

    BLACKMAN = np.insert(BLACKMAN,BLACKMAN.size,coeficiente)
    HAMMING = np.insert(HAMMING,HAMMING.size,coeficiente)
    

plt.stem(BLACKMAN)
plt.show()


plt.stem(HAMMING)
plt.show()


