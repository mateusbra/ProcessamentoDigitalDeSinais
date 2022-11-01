import numpy as np
import matplotlib.pylab as plt
from scipy.signal import freqz
#a
#3z - 3.6        =0z^2 +   3z - 3.6
#(z-0.5)(z-0.9) =1z^2 - 1.4z +0.45
#
H_a_num = np.array([0,3,-3.6])
H_a_den = np.array([1,-1.4,0.45])

w,h = freqz(b=H_a_num,a=H_a_den)
plt.plot(abs(h))
plt.show()

#b
#z - 0          =0z^2 +  1z + 0
#(z-0.9)(z-1.2) =1z^2 -2.1z + 1.08
H_b_num = np.array([0,1,0])
H_b_den = np.array([1,-2.1,1.08])

w,h = freqz(b=H_b_num,a=H_b_den)
plt.plot(abs(h))
plt.show()

#c
#z + 0.9        = 0z^2+ 1z + 0.9
#z^2 + z + 0.41 = z^2 + 1z + 0.41
H_c_num = np.array([0,1,0.9])
H_c_den = np.array([1,1,0.41])

w,h = freqz(b=H_c_num,a=H_c_den)
plt.plot(abs(h))
plt.show()