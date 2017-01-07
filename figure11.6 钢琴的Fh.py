import numpy as np
import pylab as pl
import math
class wave:
    def __init__(self,L=0.62,FT=650,b=1/8,m=0.0033,K=100000000000,u=0.01,f=262,vh0=0.5):
        self.L=L
        self.c=f*2*L
        self.FT=FT
        self.dx=L/1000
        self.dt=self.dx/self.c
        self.T=10000*self.dt
        self.b=b
        self.m=m
        self.K=K
        self.u=u
        self.t=[0]
        self.y1=[]
        self.y2=[]
        self.y3=[]
        self.y0=[]
        self.Fh=[]
        self.zh=[0]
        self.vh=[vh0]
        self.F=[]
        for i in range(int(self.L/self.dx)+1):
            self.y0.append(0)
        self.y=[]
        self.Y=[self.y0]
        self.X=[]
        for i in range(int(self.L/self.dx)+1):
            self.X.append(i*self.dx)
           
    def propagate(self):
        self.y1=self.y2=self.y0
        self.y.append(self.y2[-2])
        self.F.append(self.FT*(self.y[-1]/self.dx))
        self.Fh.append(-self.K*pow(self.y2[round((self.L*self.b)/self.dx)]-self.zh[-1],3))
        k=0
        while self.t[-1]<self.T:
            k=k+1 
            self.t.append(self.t[-1]+self.dt)
            self.y3.append(0)
            for i in range(round((self.L*self.b)/self.dx)-2):
                self.y3.append(-self.y1[i+1]+self.y2[i+2]+self.y2[i])
            self.y3.append(-self.y1[round((self.L*self.b)/self.dx)-1]+self.y2[round((self.L*self.b)/self.dx)]+self.y2[round((self.L*self.b)/self.dx)-2]\
                                    +0.25*self.dt*self.dt/self.u/self.dx*self.Fh[-1])
            self.y3.append(-self.y1[round((self.L*self.b)/self.dx)]+self.y2[round((self.L*self.b)/self.dx)+1]+self.y2[round((self.L*self.b)/self.dx)-1]\
                                    +0.5*self.dt*self.dt/self.u/self.dx*self.Fh[-1])
            self.y3.append(-self.y1[round((self.L*self.b)/self.dx)+1]+self.y2[round((self.L*self.b)/self.dx)+2]+self.y2[round((self.L*self.b)/self.dx)]\
                                    +0.25*self.dt*self.dt/self.u/self.dx*self.Fh[-1])
            for i in range(round(self.L/self.dx)-round((self.L*self.b)/self.dx)-2):
                self.y3.append(-self.y1[i+1+round((self.L*self.b)/self.dx)+1]+self.y2[i+2+round((self.L*self.b)/self.dx)+1]+self.y2[i+round((self.L*self.b)/self.dx)+1])  
            self.y3.append(0)
            self.y.append(self.y3[-2])
            self.F.append(self.FT*(self.y[-1]/self.dx))
            self.zh.append(self.zh[-1]+self.vh[-1]*self.dt)
            self.vh.append(self.vh[-1]-self.Fh[-1]/self.m*self.dt)
            self.Fh.append(-self.K*pow(self.y2[round((self.L*self.b)/self.dx)]-self.zh[-1],3))
            self.y1=self.y2
            self.y2=self.y3
            self.y3=[]
            if self.y2[round((self.L*self.b)/self.dx)]-self.zh[-1]>0:
                break
            
                    
a=wave()
a.propagate()
pl.plot(a.t,a.Fh)
pl.xlabel("t/s")
pl.ylabel("Fh/N")
pl.grid(True)
pl.show()

