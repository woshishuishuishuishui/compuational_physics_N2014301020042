import pylab as pl
import math
class orbit:
    def __init__(self,e=0,a=1,y0=0,vx0=0,θ0=0,ω0=0,dt=0.0001,total_time=10):
        self.xc=[a*(1+e)]
        self.yc=[y0]
        self.rc=[pow(a*(1+e)*a*(1+e)+y0*y0,1/2)]
        self.vxc=[vx0]
        self.vyc=[2*math.pi*pow((1-e)/(a*(1+e)),1/2)]   
        self.dt=dt
        self.total_time=total_time
        self.t=[0]
        self.θ=[θ0]
        self.ω=[ω0]
        self.e=e
    def trajectory2(self):
        while self.t[-1]<self.total_time:
            self.vxc.append(self.vxc[-1]-4*math.pi*math.pi*self.xc[-1]*self.dt/pow(self.rc[-1],3))
            self.vyc.append(self.vyc[-1]-4*math.pi*math.pi*self.yc[-1]*self.dt/pow(self.rc[-1],3))
            self.ω.append(self.ω[-1]-self.dt*12*math.pi*math.pi*\
                          (self.xc[-1]*math.sin(self.θ[-1])-self.yc[-1]*math.cos(self.θ[-1]))\
                          *(self.xc[-1]*math.cos(self.θ[-1])+self.yc[-1]*math.sin(self.θ[-1]))\
                          /pow(self.rc[-1],5))
            self.xc.append(self.xc[-1]+self.vxc[-1]*self.dt)
            self.yc.append(self.yc[-1]+self.vyc[-1]*self.dt)
            self.rc.append(pow(pow(self.xc[-1],2)+pow(self.yc[-1],2),1/2))
            self.θ.append(self.θ[-1]+self.ω[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)

a=orbit(e=0.1)
a.trajectory2()
b=orbit(e=0.1,θ0=0.01)
b.trajectory2()
c=[]
for i in range(len(a.t)):
    c.append(a.θ[i]-b.θ[i])
d=[]
for i in range(len(a.t)):
    d.append(a.ω[i]-b.ω[i])
pl.plot(a.t,c,".")
pl.grid(True)
pl.show()
pl.plot(a.t,a.ω)
pl.grid(True)
pl.show()
pl.plot(b.t,b.ω)
pl.grid(True)
pl.show()
pl.plot(b.t,d)
pl.grid(True)
pl.show()
