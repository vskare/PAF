import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as ho

h1 = ho.HarmonicOscillator(2,8,3,11,0.01)
a1,v1,x1,t1 = h1.eulerova_metoda(11)
plt.scatter(t1,x1,color="orange")

h2=ho.HarmonicOscillator(2,8,3,11,0.02)
a2,v2,x2,t2=h2.eulerova_metoda(11)
plt.scatter(t2,x2,color="green")

h3=ho.HarmonicOscillator(2,8,3,11,0.05)
a3,v3,x3,t3=h3.eulerova_metoda(11)
plt.scatter(t3,x3,color="blue")

plt.title("x-t")
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()