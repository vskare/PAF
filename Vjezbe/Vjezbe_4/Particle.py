import math as m
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,theta,x0=0,y0=0):
        self.v0 = v0
        self.theta = m.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.vx = v0*m.cos(self.theta)
        self.vy = v0*m.sin(self.theta)
        self.g = -9.81
        self.trajectory = [x0,y0]
    
    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0*m.cos(self.theta)
        self.vy = self.v0*m.sin(self.theta)
        self.trajectory = [(self.x0, self.y0)]

    def __move(self,dt):
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.vy += self.g*dt
        self.trajectory.append((self.x, self.y))
    
    def range(self,dt):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x
    
    def plot_trajectory(self):
        x = []
        y = []
        while self.y >= 0:
            x.append(self.x)
            y.append(self.y)
            self.__move(0.01)
        plt.plot(x,y)
        plt.show()
        self.reset()