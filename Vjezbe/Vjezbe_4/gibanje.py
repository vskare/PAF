import Particle
import math as m

p1 = Particle.Particle(10,60)
print(p1.plot_trajectory())
print(p1.range(0.01)) #domet pomocu particle 8.899999999999993
print(((10**2)*m.sin(2*m.radians(60))/9.81)) #izracun dometa 8.82798576742547