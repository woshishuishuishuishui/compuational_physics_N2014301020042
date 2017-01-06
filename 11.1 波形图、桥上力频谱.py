import numpy as np
import pylab as pl
class wave:
    def __init__(self,L=0.65,c=320,FT=149,dx=0.00065,T=0.0203125,b=1/5):
        self.L=L
        self.c=c
        self.FT=FT
        self.dx=dx
        self.dt=self.dx/self.c
        self.T=T
        self.b=b
        self.t=[0]
        self.y1=[]
        self.y2=[]
        self.y3=[]
        self.y0=[]
        self.F=[]
        self.N1=int(self.b*self.L/self.dx)
        self.N2=int((self.L-self.b*self.L)/self.dx)
        for i in range(self.N1+1):
            self.y0.append(0.03/(self.b*self.L)*i*self.dx)
        for i in range(self.N2):
            self.y0.append(-0.03/(self.L-self.b*self.L)*(i+1)*self.dx+0.03)
        self.y=[]
        self.Y=[self.y0]
        self.X=[]
        for i in range(int(self.L/self.dx)+1):
            self.X.append(i*self.dx)
           
    def propagate(self):
        self.y1=self.y2=self.y0
        self.y.append(self.y2[1])
        self.F.append(self.FT*(self.y[-1]/self.dx))
        k=0
        while self.t[-1]<self.T:
            k=k+1 
            self.t.append(self.t[-1]+self.dt)
            self.y3.append(0)
            for i in range(int(self.L/self.dx)-1):
                self.y3.append(-self.y1[i+1]+self.y2[i+2]+self.y2[i])
            self.y3.append(0)    
            self.y.append(self.y3[1])
            self.F.append(self.FT*(self.y[-1]/self.dx))
            self.y1=self.y2
            self.y2=self.y3
            self.y3=[]
            for i in range(11):
                if k==100*i:
                    self.Y.append(self.y2)
            
a=wave()
a.propagate()
P=np.fft.fft(a.F)
A=[]
for i in P:
    A.append(i.real*i.real+i.imag*i.imag)
frequency=np.linspace(0,a.c/(a.dx),len(P))
pl.plot(frequency,A)
pl.xlim(0,5000)
pl.xlabel("frequency")
pl.ylabel("power")
pl.grid(True)
pl.show()

pl.plot(a.t,a.F)
pl.grid(True)
pl.show()

for i in range(len(a.Y)):
    pl.plot(a.X,a.Y[i])
    pl.grid(True)
    pl.show()
