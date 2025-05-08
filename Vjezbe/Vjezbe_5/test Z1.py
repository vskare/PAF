import numpy as np
import matplotlib.pyplot as plt
from calculus import derivacija_u_tocki, derivacija_na_integralu

def kubna_funk(x):
    return x**3
def trig_funk(x):
    return np.sin(x)

a=0
b=2

tocke_trig, deriv_trig = derivacija_na_integralu(trig_funk,a,b)

tocke_kubna, deriv_kubna = derivacija_na_integralu(kubna_funk,a,b)

plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(tocke_trig, trig_funk(tocke_trig), label='sin(x)', color='blue')
plt.plot(tocke_trig,deriv_trig, label='derivacija sin(x)', linestyle='--',color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('trigonometrijska funkcija i njena derivacija')
plt.legend()

plt.subplot(2,1,2)
plt.plot(tocke_kubna, kubna_funk(tocke_kubna),label='x^3',color='green')
plt.plot(tocke_kubna, deriv_kubna, label='derivacija x^3',linestyle='--',color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('kubna funkcija i njena derivacija')
plt.legend()

plt.show()