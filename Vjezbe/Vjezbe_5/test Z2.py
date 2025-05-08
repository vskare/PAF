import numpy as np
import matplotlib.pyplot as plt
from calculus import pravokutna_aproksimacija, trapezna_formula

def funkcija(x):
    return np.exp(-x**2)

analiticki_integral = np.sqrt(np.pi)/2

a=0
b=2

broj_koraka=[10,50,100,200]

rez_pravokutna=[]
rez_trapezna=[]

for n in broj_koraka:
    donji_maks, gornji_maks = pravokutna_aproksimacija(funkcija,a,b,n)
    rez_pravokutna.append((donji_maks, gornji_maks))

    integral_trapezna = trapezna_formula(funkcija,a,b,n)
    rez_trapezna.append(integral_trapezna)

plt.figure(figsize=(10,6))
plt.axhline(y=analiticki_integral, color='r',linestyle='--',label='analiticko rjesenje')

donje_maks = [donja for donja, _ in rez_pravokutna]
gornje_maks = [gornja for _, gornja in rez_pravokutna]
plt.plot(broj_koraka, donje_maks,label='pravokutna (donji maks)')
plt.plot(broj_koraka, gornje_maks, label='pravokutna (gornji maks)', linestyle='--')

plt.plot(broj_koraka,rez_trapezna, label='trapezna formula',linestyle='-.')
plt.xlabel('broj koraka')
plt.ylabel('vrijednost integrala')
plt.title('numericka integracija funkcije $e^{-x^2}$')
plt.legend()
plt.grid(True)
plt.show()