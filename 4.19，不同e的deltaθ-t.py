import pylab as pl
import math
class orbit:
    def __init__(self,e=0,a=1,y0=0,vx0=0,θ0=0,ω0=0,dt=0.0001,total_time=4):
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
    
for i in range(20):
    m=orbit(e=0+i/20)
    m.trajectory2()
    n=orbit(e=0+i/20,θ0=0.01)
    n.trajectory2()
    c=[]
    for i in range(len(m.t)):
        c.append(m.θ[i]-n.θ[i])
    pl.plot(m.t,c,".")
    pl.grid(True)
    pl.show()
