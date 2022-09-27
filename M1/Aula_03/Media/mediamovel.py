import numpy as np
import matplotlib.pyplot as mlp

#entrada = [10,2,8,-4,-2,3]
entrada = np.fromfile("sweep.pcm", dtype='int16')
#entrada = np.fromfile("impulsoun.pcm", dtype='int16')
#entrada = np.fromfile("degrauun.pcm", dtype='int16')

k = 100
y = np.zeros(k)
tam = len(entrada)
#Cria x e y
x = np.full(k,1/k)
saida = np.array([])

for j in range(tam):
    for i in range(k-1,-1,-1): # itera de k-1 até 0
        y[i] = y[i-1] #desloca o vetor de amostras
        if(i==0):
            y[i] = entrada[j]
            total = 0
            for it in range(k): #itera de 0 até k-1
                total = total + y[it] * x[it]
                
            saida = np.insert(saida,saida.size,total)


mlp.stem(entrada)
mlp.show()

mlp.stem(saida)  #plota as funções dependentes de eixo xx e y
mlp.show()

#Monta arquivo de saida
arq = open("mediamovel.pcm","wb")
arq.write(np.array(saida,dtype='int16'))
arq.close()