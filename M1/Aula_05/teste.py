import numpy as np
import matplotlib.pyplot as plt




w = np.arange(0,np.pi*2,np.pi/64)

#x = np.arange(0,tam,1)
y = 10*(np.sin(w))

#x2 = np.arange(0,tam,1)
x2 = np.arange(0,np.pi*2,np.pi/64)
y2 = (np.sin(10*w))
y3 = y+y2

N = 128
n = np.arange(N)
k = n.reshape((N,1))
M = np.exp(-1j*2*np.pi*k*n/N)
print(2*np.pi*k*n/N)

#print(M)

saida = M@y3
#print(saida)

plt.stem(abs(saida))
plt.show()