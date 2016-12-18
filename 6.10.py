import numpy as np
import pylab as pl
import math
class wave:
    def __init__(self,L=1,c=300,dx=0.001,T=0.04,x0=0.05,X0=0.4):
        self.L=L
        self.c=c
        self.dx=dx
        self.dt=dx/c
        self.T=T
        self.t=[0]
        self.y1=[]
        self.y2=[]
        self.y3=[]
        self.y0=[]
        self.x0=x0
        self.X0=X0
        for i in range(1001):
            self.y0.append(math.sin(3*math.pi/self.L*self.dx*i))
        self.y0[0]=0
        self.y=[]
        self.Y=[self.y0]
           
    def propagate(self):
        self.y1=self.y2=self.y0
        self.y.append(self.y2[int(self.x0/0.001)])
        while self.t[-1]<self.T:
            self.t.append(self.t[-1]+self.dt)
            self.y3.append(0)
            for i in range(999):
                self.y3.append(-self.y1[i+1]+self.y2[i+2]+self.y2[i])
            self.y3.append(0)    
            self.y.append(self.y3[int(self.x0/0.001)])
            self.y1=self.y2
            self.y2=self.y3
            self.y3=[]
            for i in range(10):
                if len(self.t)==i*100:
                    self.Y.append(self.y2)
a=wave()
a.propagate()
P=(abs(np.fft.rfft(a.y)))**2
frequency=np.linspace(0,a.c/(a.dx*2),len(P))

pl.plot(frequency,P)
pl.xlim(0,3000)
pl.xlabel("frequency")
pl.ylabel("power")
pl.show()
