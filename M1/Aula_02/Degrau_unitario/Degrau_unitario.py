import numpy as np
import matplotlib.pyplot as plt


tam = 200
#Cria x e y
x = np.linspace(-tam, tam-1, num=2*tam, dtype=float)
y = np.zeros(tam*2,dtype=float)

#Multiplica as magnitudes de entrada por 2
for idx, val_x in np.ndenumerate(x):
  if(val_x>=0):
    y[idx] = 16000
      
plt.stem(x,y)  #plota as funções dependentes de eixo x e y
plt.show()

#Printa arquivo de saida


#Monta arquivo de saida

arq = open("degrauun.pcm","wb")
arq.write(np.array(y,dtype='int16'))
arq.close()