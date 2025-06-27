import matplotlib.pyplot as plt
import math as mt

class Jednodimenzionalno_Gibanje:
    def __init__(self,m,v0,x0,t_uk,dt=0.1):

        self.m = m
        self.v = [v0]
        self.x = [x0]
        self.a = []
        self.t_uk = t_uk
        self.dt = dt

    def racun(self,v,x,t,dt):

        F = #proizvoljan izraz za silu
        self.a.append(F/self.m)
        self.v.append(self.v[-1] + self.a[-1]*dt)
        self.x.append(self.x[-1] + self.v[-1]*dt)

    def gibanje(self):

        t=0
        vremena = [0]
        while t<self.t_uk:
            self.racun(self.v[-1],self.x[-1],t,self.dt)
            t+=self.dt
            vremena.append(t)
        plt.subplot(1,2,1)
        plt.xlabel("Vrijeme [s]")
        plt.ylabel("Položaj [m]")
        plt.plot(vremena, self.x)

        plt.subplot(1,2,2)
        plt.xlabel("Vrijeme [s]")
        plt.ylabel("Brzina [m/s]")
        plt.plot(vremena, self.v)

        plt.tight_layout()
        plt.show()

Tijelo = Jednodimenzionalno_Gibanje(1,1,0,20)
Tijelo.gibanje()