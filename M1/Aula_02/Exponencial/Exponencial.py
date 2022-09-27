import numpy as np
import matplotlib.pyplot as plt

a = 2
tam = 20
#Cria x e y
x = np.arange(0,tam,1)
y = []


for value in range(len(x)):
    y.append(a**(value))

plt.stem(x,y)  #plota as funções dependentes de eixo x e y
plt.show()


#Monta arquivo de saida
arq = open("exponencial.pcm","wb")
arq.write(np.array(y,dtype='int16'))
arq.close()