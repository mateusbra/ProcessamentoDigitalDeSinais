import numpy as np
import matplotlib.pyplot as mlp
# y(k)=x(k)+1/2*x(k-1)+1/4*y(k-1)+1/5*x(k-2)-1/2*y(k-2)
x = np.ones([10])#degrau

y = np.array([])
print(x)
for k in range(-2,8+1):
    print(k)
    if(k<0):
        resultado = 0
    elif(k - 1<0):
        resultado = x[k]
    elif(k - 2<0):
        resultado = x[k] + 1/2 * x[k - 1 + 2] + 1/4 * y[k - 1 + 2] #+2 pois y[0] será equivalente ao y[-2]
    else:
        resultado = x[k] + 1/2 * x[k - 1 + 2] + 1/4 * y[k - 1 + 2] + 1/5 * x[k - 2 + 2] - 1/2 * y[k - 2 + 2]  #+2 pois y[0] será equivalente ao y[-2]
        print(resultado)       
    y = np.insert(y,y.size,resultado)
print(y)
mlp.stem(range(-2,8+1),y)
mlp.show()

mlp.stem(range(-2,8),x)
mlp.show()