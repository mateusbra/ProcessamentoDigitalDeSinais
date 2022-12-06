import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz

entrada = np.fromfile("sweep.pcm", dtype='int16')

fs = 8000
fchz = 3000
fc = fchz/fs#400/8000
M = 100
H1 = np.array([])
H2 = np.array([])
for i in range(0,M):
    if(i-M/2==0):
        coeficiente = 2*np.pi*fc
    else:
        coeficiente = np.sin(2*np.pi*fc*(i-M/2))/(i-M/2)#SIN(2*PI*FC * (I%-M%/2)) / (I%-M%/2)
        
    #HAMMING
    #coeficiente = coeficiente * (0.54 - 0.46 * np.cos(2*np.pi*i/M)) #H[I%] = H[I%] * (0.54 - 0.46*COS(2*PI*I%/M%) )
    #BLACKMAN
    coeficiente = coeficiente * (0.42 - 0.5 * np.cos(2*np.pi*i/M) + 0.08 * np.cos(4*np.pi*i/M))

    H1 = np.insert(H1,H1.size,coeficiente)

    

#truncamento
#H = H[int(M/4):int(3*M/4)]
#for i in range(0,int(M/2)):
#    H = np.insert(H,H.size,0)
soma = 0
for i in range(0,M):
    soma = soma + H1[i]

for i in range(0,M):
    H1[i] = -H1[i]/soma

H1[int(M/2)] = H1[int(M/2)] + 1
plt.stem(H1)
plt.show()
saida = np.convolve(entrada,H1)

w,h = freqz(b=H1,fs=fs)
plt.plot(w,abs(h))
plt.show()

# for i in range(0,len(H1)):
#     H1[i] =  H1[i]*32768

#Monta arquivo de saida
with open("CoefPA.dat", "w") as f:
    for s in H1:
        f.write(str(s) +",\n")

        