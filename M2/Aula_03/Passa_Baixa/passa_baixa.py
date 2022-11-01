import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz

from sympy.abc import s
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import pole_zero_plot

fs = 8000
fc = 1000
wc = 2*np.pi*fc
Flinha = 2*fs

a = wc/(Flinha + wc)
b = (wc-Flinha)/(Flinha + wc)
#y[n] = ax[n] + ax[n-1] - by[n-1]
#Y(z) = a * X(z) + a * X(z) * z^-1 - b * Y(z) * z^-1
#Y(z)/X(z) =  (a + a * z^-1)/ (1 + b * z^-1)
tf1 = TransferFunction(a*s-a, s-(b), s)
pole_zero_plot(tf1) 
num = np.array([a,a])
den = np.array([1,b])

entrada = np.fromfile("sweep.pcm", dtype='int16')
saida = np.zeros(len(entrada))
for i in range(len(entrada)):
    if(i-1<0):
        saida[i] = a*entrada[i]
    else:
        saida[i] = a*entrada[i] + a*entrada[i-1] - b*saida[i-1]

plt.plot(entrada)
plt.show()

plt.plot(saida)
plt.show()

w,h = freqz(b=num,a=den)
plt.plot(abs(h))
plt.show()

arq = open("saida.pcm","wb")
arq.write(np.array(saida,dtype='int16'))
arq.close()