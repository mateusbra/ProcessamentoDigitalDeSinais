import numpy as np
import pylab
import matplotlib.pyplot as plt


w = np.arange(0,np.pi*2,np.pi/50)

#x = np.arange(0,tam,1)
y = 10*(np.sin(w))

#x2 = np.arange(0,tam,1)
x2 = np.arange(0,np.pi*2,np.pi/50)
y2 = (np.sin(10*w))

y3 = y + y2

#(1-x^L+1)/1-x

plt.stem(x,y)  #plota as funções dependentes de eixo x e y
plt.show()

plt.stem(x,y2)  #plota as funções dependentes de eixo x e y
plt.show()

plt.stem(x,y3)  #plota as funções dependentes de eixo x e y
plt.show()

w = np.arange(0,np.pi*2,np.pi/50)
#pylab.plot(y)
#pylab.plot(y2)


#-inf inf x[n]*e^-jwn




exponencial = np.exp(-1j*w)
#exponencial = np.cos(w)-1j*np.sin(w)
saida = y3*exponencial

#saida = np.fft.fft(y3)


plt.stem(saida)
plt.show()




#plt.stem(w,saida)
#plt.show()

#plt.stem(w,np.imag(saida))
#plt.show()
