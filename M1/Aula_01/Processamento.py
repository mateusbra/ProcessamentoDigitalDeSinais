import numpy as np
import matplotlib.pyplot as plt

#Le arquivo de entrada
data = np.fromfile("Audio_entrada.pcm", dtype='int16')
#Printa arquivo de entrada
print("Audio_entrada:",data)

#Multiplica as magnitudes de entrada por 2
for idx, magnitud in np.ndenumerate(data):
  data[idx] = magnitud * 2

#Printa arquivo de saida
print("Audio_saida:",data)

#Monta arquivo de saida
arq = open("Audio_saida.pcm","wb")
arq.write(data)
arq.close()
