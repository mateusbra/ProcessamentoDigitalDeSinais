import numpy as np
import matplotlib.pyplot as mlp
# y(k)=0,2*x(k)+0,3x(k-1)+0,3*x(k-2)+0,2*x(k-3)
x = np.ones([10])#degrau

y = np.array([])
print(x)
for k in range(-2,8+1):
    print(k)
    if(k<0):
        resultado = 0
    elif(k - 1<0):
        resultado = 0.2 * x[k]
    elif(k - 2<0):
        resultado = 0.2 * x[k] + 0.3 * x[k - 1 + 2] #+2 pois y[0] será equivalente ao y(-2)
    elif(k - 3<0):
        resultado = 0.2 * x[k] + 0.3 * x[k - 1 + 2]  + 0.3 * x[k - 2 + 2] #+2 pois y[0] será equivalente ao y(-2)
    else:
        resultado = 0.2 * x[k] + 0.3 * x[k - 1 + 2]  + 0.3 * x[k - 2 + 2] + 0.2 * x[k - 3 + 2]
          #+2 pois y[0] será equivalente ao y(-2)
        print(resultado)       
    y = np.insert(y,y.size,resultado)
print(y)
mlp.stem(range(-2,8+1),y)
mlp.show()

mlp.stem(range(-2,8),x)
mlp.show()