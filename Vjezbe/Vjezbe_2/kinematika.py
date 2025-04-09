import matplotlib.pyplot as plt
import numpy as np
import math as m


def jednoliko_gibanje(F,m,v0,x0,t_ukupno,dt):
    a0 = F/m
    a = [a0]
    v=[v0]
    x=[x0]
    t=[0]
    n=0

    for i in np.arange(0,t_ukupno,dt):
        v.append(v[n]+a[n]*dt)
        x.append(x[n]+v[n+1]*dt)
        a.append(a0)
        t.append(t[n]+dt)
        n+=1
    
    plt.subplot(1,3,1)
    plt.xlabel('t/[s]')
    plt.ylabel('x/[m]')
    plt.title('x-t graf')
    plt.plot(t,x)

    plt.subplot(1,3,2)
    plt.xlabel('t/[s]')
    plt.ylabel('v/[m/s]')
    plt.title('v-t graf')
    plt.plot(t,v)

    plt.subplot(1,3,3)
    plt.xlabel('t/[s]')
    plt.ylabel('a/[m/s^2]')
    plt.title('a-t graf')
    plt.plot(t,a)

    plt.show()

def kosi_hitac(theta,v0,x0,y0,t_ukupno,dt):
    vx = [v0*m.cos(m.radians(theta))]
    vy = [v0*m.sin(m.radians(theta))]
    ax = 0
    ay = -9.81
    x = [x0]
    y = [y0]
    t = [0]
    n = 0

    for i in np.arange(0,t_ukupno,dt):
        if y[n]<=0 and i!=0:
            break
        vx.append(vx[n]+ax*dt)
        vy.append(vy[n]+ay*dt)
        x.append(x[n]+vx[n+1]*dt)
        y.append(y[n]+vy[n+1]*dt)
        t.append(t[n]+dt)
        n+=1

    plt.subplot(1,3,1)
    plt.title('x-y graf')
    plt.xlabel('x/[m]')
    plt.ylabel('y/[m]')
    plt.plot(x,y)

    plt.subplot(1,3,2)
    plt.title('x-t graf')
    plt.xlabel('t/[s]')
    plt.ylabel('x/[m]')
    plt.plot(t,x)

    plt.subplot(1,3,3)
    plt.title('y-t graf')
    plt.xlabel('t/[s]')
    plt.ylabel('y/[m]')
    plt.plot(t,y)

    plt.show()