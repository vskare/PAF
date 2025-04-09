import matplotlib.pyplot as plt
import numpy as np

F = 12
m = 10
dt = 0.5
t_ukupno = 10

t=[0]
n=0

v0 = 0
x0 = 0
a0 = F/m

v = [v0]
x = [x0]
a = [a0]

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