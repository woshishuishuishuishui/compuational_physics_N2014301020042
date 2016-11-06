import pylab as pl
import math
class chaos1:
    def __init__(self,g=9.8,l=9.8,Ω=2/3,dt=0.04,w0=0,FD=1.2,total_time=50,\
                 q=0.5,θo=0.2):
        self.θ=[θo]
        self.w=[w0]
        self.dt=dt
        self.t=[0]
        self.total_time=total_time
        self.FD=FD
        self.g=g
        self.l=l
        self.Ω=Ω
        self.q=q
    def poincare(self):
        time=0
        while(time<self.total_time):
            self.w.append(self.w[-1]-(self.g/self.l)*math.sin(self.θ[-1])*self.dt-self.q*self.w[-1]*self.dt+self.FD*math.sin(self.Ω*self.t[-1])*self.dt)
            self.θ.append(self.θ[-1]+self.w[-2]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            time+=self.dt
            if self.θ[-1]>math.pi:
                self.θ[-1]=self.θ[-1]-2*math.pi
            if self.θ[-1]<-math.pi:
                self.θ[-1]=self.θ[-1]+2*math.pi
         


c=chaos1(FD=0.5)
c.poincare()
d=chaos1(FD=0.5,θo=2-0.001) 
d.poincare()
delta_θ_0_5=[]
for i in range(len(c.t)):
    delta_θ_0_5.append(math.log(abs(c.θ[i]-d.θ[i])))

pl.plot(c.t,delta_θ_0_5)
pl.xlabel('time/s')
pl.ylabel('log(deltaθ)')
pl.show()
