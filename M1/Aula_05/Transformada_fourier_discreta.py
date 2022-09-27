import numpy as np
import pylab
import matplotlib.pyplot as plt


#x[n] = a^n u[n] tal que |a| < 1 para convergir
#transformada é o somatorio de -inf até inf x[n]*e^-jwn
#sinal u[n] faz com que analisemos de 0 até inf do sinal
#teremos soma de 0 a inf de (a*e^-jw)^n
#Soma infinita = 1/1-r
# 1/1-a*e^-jw
a = 1/2


w = np.arange(0,2*np.pi,np.pi/50)
numerador = 1
denominador = 1-a*np.exp(-1j*w)
X = numerador/denominador
magnitude = np.abs(X)
fase = np.angle(X)


plt.stem(w,magnitude)
plt.show()

plt.stem(w,fase)
plt.show()