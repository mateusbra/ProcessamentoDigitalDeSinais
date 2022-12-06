import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz
entrada = np.fromfile("ruido_branco.pcm", dtype='int16')
filtro = np.array([0.25,0.25,0.25,0.25])#media movel
w = np.zeros(4)
tam = (len(entrada))
erroAmostras = np.zeros(tam)
yAmostras = np.zeros(tam)
dAmostras = np.zeros(tam)
u = 1 * 10**(-10)#w[0] = w[0] + U*erro*x[n]
#w[1] = w[1] + U*erro*x[n-1]
sample = np.zeros(4)
#sample = entrada
    
for i in range(0,tam):
    
    y = 0
    d = 0
    #multiplica e acumula convolucao
    sample[0] = entrada[i]
    for n in range(0,len(sample)):
        y += w[n]*sample[n]
        d += filtro[n]*sample[n]
        
   
    e = d - y
    for n in range(0,len(sample)):
        w[n] = w[n] + u*e*sample[n]
        
     #desloca amostra
    for n in range(len(sample)-1,0,-1):
        sample[n]=sample[n-1]
    
    erroAmostras[i] = e
    dAmostras[i] = d
    yAmostras[i] = y
    
plt.plot(erroAmostras)
plt.show()
print(w)
plt.stem(w)
plt.show()

plt.plot(dAmostras)
plt.show()

plt.plot(yAmostras)
plt.show()