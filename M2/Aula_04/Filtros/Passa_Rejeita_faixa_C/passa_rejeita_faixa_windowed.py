import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz

entrada = np.fromfile("sweep.pcm", dtype='int16')

fs = 8000
fchz1 = 2000
fc1 = fchz1/fs#400/8000
fchz2 = 3000
fc2 = fchz2/fs#400/8000
M = 100



H1 = np.array([])#passa baixa
H2 = np.array([])#passa alta
H3 = np.zeros(100)#passa faixa
for i in range(0,M):
    if(i-M/2==0):
        coeficiente1 = 2*np.pi*fc1
        coeficiente2 = 2*np.pi*fc2
    else:
        coeficiente1 = np.sin(2*np.pi*fc1*(i-M/2))/(i-M/2)
        coeficiente2 = np.sin(2*np.pi*fc2*(i-M/2))/(i-M/2)
    #HAMMING
    #coeficiente = coeficiente * (0.54 - 0.46 * np.cos(2*np.pi*i/M)) #H[I%] = H[I%] * (0.54 - 0.46*COS(2*PI*I%/M%) )
    #BLACKMAN
    coeficiente1 = coeficiente1 * (0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M))
    coeficiente2 = coeficiente2 * (0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M))
    H1 = np.insert(H1,H1.size,coeficiente1)
    H2 = np.insert(H2,H2.size,coeficiente2)
    

soma1 = 0
soma2 = 0
for i in range(0,M):
    soma1 = soma1 + H1[i]
    soma2 = soma2 + H2[i]
    
for i in range(0,M):
    H1[i] = H1[i]/soma1
    H2[i] = -H2[i]/soma2
H2[int(M/2)] = H2[int(M/2)] + 1 #passa alta

for i in range(0,M):
    H3[i] = H1[i] + H2[i]
    
for i in range(0,M):
    H3[i] = -H3[i]   #inverter rejeita faixa para passa banda
H3[int(M/2)] = H3[int(M/2)] + 1 #inverter rejeita faixa para passa banda
plt.stem(H3)
plt.show()


w,h = freqz(b=H3,fs=fs)
plt.plot(w,abs(h))
plt.show()

saida = np.convolve(entrada,H3)
plt.plot(saida)
plt.show()

for i in range(0,len(H3)):
    H3[i] =  H3[i]*32768

#Monta arquivo de saida
with open("CoefPF.dat", "w") as f:
    for s in H3:
        f.write(str(s) +",\n")
