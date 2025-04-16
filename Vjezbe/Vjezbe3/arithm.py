import numpy as np
import math as m

#a)
x = [12.5,3.2,4,58.485,8,3.13,2.99,36.5,19.2,22.23]
sum_x=0

for i in x:
    sum_x+=i

avg_x = sum_x/len(x)

print("sredina: ", avg_x)

sigma_x = 0

for i in x:
    sigma_x+=(i-avg_x)**2

sigma_x = m.sqrt(sigma_x/len(x))

print("devijacija: ", sigma_x)

#b)

print("sredina: ", np.mean(x))
print("devijacija: ", np.std(x))