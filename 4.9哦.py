import pylab as pl
import math
class orbit:
    def __init__(self,β=2.5,a=1,m=6*pow(10,24),M=2*pow(10,30),x0=2,y0=0,vx0=0,vy0=4,dt=0.001,total_time=3):
        self.β=β
        self.x=[x0]
        self.y=[y0]
        self.r=[pow(x0*x0+y0*y0,1/2)]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=dt
        self.total_time=total_time
        self.t=[0]
    def trajectory(self):
        while self.t[-1]<self.total_time:
            self.vx.append(self.vx[-1]-4*math.pi*math.pi*self.x[-1]*self.dt/pow(self.r[-1],self.β+1))
            self.vy.append(self.vy[-1]-4*math.pi*math.pi*self.y[-1]*self.dt/pow(self.r[-1],self.β+1))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.r.append(pow(pow(self.x[-1],2)+pow(self.y[-1],2),1/2))
            self.t.append(self.t[-1]+self.dt)
            
a=orbit(β=2.05,vy0=0.4*math.pi,x0=1)
a.trajectory()
pl.plot(a.x,a.y,".")
pl.grid(True)
pl.show()
