import numpy as np
import matplotlib.pyplot as mlp


entrada = np.fromfile("Audio_entrada.pcm", dtype='int16')

tam = len(entrada)
t1 = 400*10**-3
fs = 8000
a0 = 0.5
a1 = 0.3
n1 = int(t1*fs)


saida = np.array([])

for i in range(tam):
    if(i-n1<0):
        resultado = a0 * entrada[i]
    else:
        resultado = a0 * entrada[i] + a1 * saida[i - n1]
    saida = np.insert(saida,saida.size,resultado)
    
mlp.stem(entrada)
mlp.show()

mlp.stem(saida)  #plota as funções dependentes de eixo xx e y
mlp.show()

#Monta arquivo de saida
arq = open("eco.pcm","wb")
arq.write(np.array(saida,dtype='int16'))
arq.close()