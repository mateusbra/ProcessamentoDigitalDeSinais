import numpy as np
import matplotlib.pyplot as mlp


#entrada = [1,0.5,0.25,0.125]
entrada = np.fromfile("impulsoun.pcm", dtype='int16')
#entrada = np.fromfile("degrauun.pcm", dtype='int16')
#entrada = np.fromfile("sweep.pcm", dtype='int16')
k = 8
tam = len(entrada)
#Cria x e y
#h = np.full(k,1/k)#media movel
h = [1,0.5,0.25,0.125]
saida = np.convolve(entrada,h)
    

print(entrada)
mlp.stem(entrada)
mlp.show()

mlp.stem(saida)  #plota as funções dependentes de eixo xx e y
mlp.show()

#Monta arquivo de saida
arq = open("mediamovel.pcm","wb")
arq.write(np.array(saida,dtype='int16'))
arq.close()