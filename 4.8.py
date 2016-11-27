import pylab as pl
import math
class orbit:
    def __init__(self,β=2,e=0.017,a=1,m=6*pow(10,24),M=2*pow(10,30),y0=0,vx0=0,dt=0.005,total_time=250):
        self.β=β
        self.x=[a*(1+e)]
        self.y=[y0]
        self.r=[pow(a*(1+e)*a*(1+e)+y0*y0,1/2)]
        self.vx=[vx0]
        self.vy=[2*math.pi*pow((1-e)*(1+m/M)/(a*(1+e)),1/2)]
        self.dt=dt
        self.total_time=total_time
        self.t=[0]
    def trajectory(self):
        while self.t[-1]<self.total_time:
            self.vx.append(self.vx[-1]-4*math.pi*math.pi*self.x[-1]*self.dt/pow(self.r[-1],3))
            self.vy.append(self.vy[-1]-4*math.pi*math.pi*self.y[-1]*self.dt/pow(self.r[-1],3))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.r.append(pow(pow(self.x[-1],2)+pow(self.y[-1],2),1/2))
            self.t.append(self.t[-1]+self.dt)
        self.x.append(0)
        self.y.append(0)
    def find_a_T(self):
        c=[]
        d=[] 
        for i in range(len(self.t)-2):
            if self.y[i+2]>=0 and self.y[i+1]<0 or self.y[i+2]>0 and self.y[i+1]<=0:
                c.append(self.t[i+1])
            if self.y[i+2]<=0 and self.y[i+1]>0 or self.y[i+2]<0 and self.y[i+1]>=0:
                d.append(abs(self.x[i+1]-self.x[0]))
        print(c[0])
        print(d[0]/2)        
        print(pow(c[0],2)/pow(d[0]/2,3))

a=orbit(e=0.007,a=0.72,m=4.9*pow(10,24))
a.trajectory()
a.find_a_T()
pl.plot(a.x,a.y,".")
pl.grid(True)
pl.show()

b=orbit(e=0.206,a=0.39,m=2.4*pow(10,23))
b.trajectory()
b.find_a_T()
pl.plot(b.x,b.y,".")
pl.grid(True)
pl.show()
            
c=orbit(e=0.017,a=1,m=6*pow(10,24))
c.trajectory()
c.find_a_T()
pl.plot(c.x,c.y,".")
pl.grid(True)
pl.show()            
        
d=orbit(e=0.093,a=1.52,m=6.6*pow(10,23))
d.trajectory()
d.find_a_T()
pl.plot(d.x,d.y,".")
pl.grid(True)
pl.show()

e=orbit(e=0.048,a=5.2,m=1.9*pow(10,27))
e.trajectory()
e.find_a_T()
pl.plot(e.x,e.y,".")
pl.grid(True)
pl.show()

f=orbit(e=0.056,a=9.54,m=5.7*pow(10,26))
f.trajectory()
f.find_a_T()
pl.plot(f.x,f.y,".")
pl.grid(True)
pl.show()

g=orbit(e=0.046,a=19.19,m=8.8*pow(10,25))
g.trajectory()
g.find_a_T()
pl.plot(g.x,g.y,".")
pl.grid(True)
pl.show()

h=orbit(e=0.01,a=30.06,m=1.03*pow(10,26))
h.trajectory()
h.find_a_T()
pl.plot(h.x,h.y,".")
pl.grid(True)
pl.show()

i=orbit(e=0.248,a=39.53,m=6*pow(10,24))
i.trajectory()
i.find_a_T()
pl.plot(i.x,i.y,".")
pl.grid(True)
pl.show()
