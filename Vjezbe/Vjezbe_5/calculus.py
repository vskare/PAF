import numpy as np

def derivacija_u_tocki(f,x,h=0.1,metoda='three-step'):
    if metoda == 'three-step':
        return (f(x+h) - f(x-h))/(2*h)
    else:
        return (f(x+h) - f(x))/h
    
def derivacija_na_integralu (f,a,b,h=0.1,metoda='three-step'): #a donja granica, b gornja granica
    tocke = np.linspace(a,b,num=100)
    derivacije = [derivacija_u_tocki(f,x,h=0.1,metoda='three-step') for x in tocke]
    return tocke,derivacije

def pravokutna_aproksimacija(f,a,b,n):
    dx = (b-a)/n
    x_vrijednosti = np.linspace(a,b,n+1)
    y_vrijednosti = f(x_vrijednosti)
    donja_medja = dx*np.sum(y_vrijednosti[:-1])
    gornja_medja = dx*np.sum(y_vrijednosti[1:])
    return donja_medja,gornja_medja

def trapezna_formula(f,a,b,n):
    dx = (b-a)/n
    x_vrijednosti = np.linspace(a,b,n+1)
    y_vrijednosti = f(x_vrijednosti)
    integral = dx*(np.sum(y_vrijednosti)-0.5*(y_vrijednosti[0]+y_vrijednosti[-1]))
    return integral