import matplotlib.pyplot as plt
import numpy as np
import math as m

v0 = 4
theta = 45

g = 9.81
t_ukupno = 10
dt = 0.02
theta_r = m.radians(theta)

x0 = 0
y0 = 0

vx = [v0*m.cos(theta_r)]
vy = [v0*m.sin(theta_r)]
ax = 0
ay = -g

x = [x0]
y = [y0]
t=[0]
n=0

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