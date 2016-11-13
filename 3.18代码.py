import pylab as pl
import math
class poincare_section:
    def __init__(self,g=9.8,l=9.8,Ω=2/3,dt=0.01,w0=0,FD=1.2,total_time=3800,\
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
        self.N=int(total_time*self.Ω/(2*math.pi))
        self.focus_point_θ=[] 
        self.focus_point_w=[]
    def poincare(self):
        while(self.t[-1]<self.total_time):
            self.w.append(self.w[-1]-(self.g/self.l)*math.sin(self.θ[-1])*self.dt-self.q*self.w[-1]*self.dt+self.FD*math.sin(self.Ω*self.t[-1])*self.dt)
            self.θ.append(self.θ[-1]+self.w[-2]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            if self.θ[-1]>math.pi:
                self.θ[-1]=self.θ[-1]-2*math.pi
            if self.θ[-1]<-math.pi:
                self.θ[-1]=self.θ[-1]+2*math.pi
        for i in range(100):
            for j in range(len(self.t)):
                if ((301+i)*2*math.pi)/self.Ω-self.dt/2<self.t[j]<=((301+i)*2*math.pi)/self.Ω+self.dt/2:
                    self.focus_point_θ.append(self.θ[j])
                    self.focus_point_w.append(self.w[j])
        pl.plot(self.focus_point_θ,self.focus_point_w,".")
        pl.xlabel("θ/rad")
        pl.ylabel("w/(rad/s)") 
        pl.xlim(-4,4)
        pl.ylim(-3,3)
        pl.show()
        
a=poincare_section(FD=1.465)
a.poincare()        
