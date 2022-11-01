import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz

entrada = np.fromfile("sweep.pcm", dtype='int16')

H = np.array([0.1,0.2,0.4,0.2,0.1])


w,h = freqz(b=H,fs=8000)
plt.plot(w,abs(h))
plt.show()

saida = np.convolve(entrada,H)

plt.plot(saida)
plt.show()
