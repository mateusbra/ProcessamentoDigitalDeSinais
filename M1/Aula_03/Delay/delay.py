import numpy as np
import matplotlib.pyplot as mlp


#entrada = np.fromfile("impulsoun.pcm", dtype='int16')
entrada = np.fromfile("Audio_entrada.pcm", dtype='int16')
tam = len(entrada)
t1 = 400 * 10**-3
t2 = 800 * 10**-3
fs = 8000
a0 = 0.5
a1 = 0.3
a2 = 0.2
n1 = int(t1 * fs)#4
n2 = int(t2 * fs)#8



saida = np.array([])

for i in range(tam):
    if(i-n1<0):
        resultado = a0 * entrada[i]
    elif(i-n2<0):
        resultado = a0 * entrada[i] + a1 * entrada[i - n1]
    else:
        resultado = a0 * entrada[i] + a1 * entrada[i - n1] + a2 * entrada[i - n2]
    saida = np.insert(saida,saida.size,resultado)
    

mlp.stem(entrada)
mlp.show()

mlp.stem(saida)  #plota as funções dependentes de eixo xx e y
mlp.show()

#Monta arquivo de saida
arq = open("Audio_saida.pcm","wb")
arq.write(np.array(saida,dtype='int16'))
arq.close()