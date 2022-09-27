import numpy as np
import matplotlib.pyplot as plt

fo = 100 #Frequencia
fs = 8000 #Frequencia de amostragem
tam = 800 #Tam
a = 1
#Cria x e y
x = np.arange(0,tam,1)
y = (a*np.cos(2*np.pi*x*(fo/fs)))

plt.stem(x,y)  #plota as funções dependentes de eixo x e y
plt.show()


#Monta arquivo de saida
arq = open("senoidal.pcm","wb")
arq.write(np.array(y,dtype='int16'))
arq.close()
