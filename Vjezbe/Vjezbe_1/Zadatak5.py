import matplotlib.pyplot as plt
import numpy as np
def jednadzba_pravca(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = y1 - k*x1
    print("y = {}x + {}".format(k,l))

x1 = float(input("Unesite x koordinatu prve tocke: "))
y1 = float(input("Unesite y koordinatu prve tocke: "))
x2 = float(input("Unesite x koordinatu druge tocke: "))
y2 = float(input("Unesite y koordinatu druge tocke: "))
jednadzba_pravca(x1,y1,x2,y2)
plt.xlabel('x')
plt.ylabel('y')
k = (y2-y1)/(x2-x1)
l = y1 - k*x1
x_vrijednosti = np.linspace(x1,x2)
y_vrijednosti = k*x_vrijednosti + l
plt.plot(x_vrijednosti, y_vrijednosti)
plt.plot([x1,x2], [y1,y2], 'o')
spremanje = input("zelite li spremiti graf kao pdf ili ga prikazati u programu (pdf/program)")
if spremanje == 'program':
    plt.show()
elif spremanje == 'pdf':
    filename = input("unesite ime datoteke") +'.pdf'
    plt.savefig(filename)