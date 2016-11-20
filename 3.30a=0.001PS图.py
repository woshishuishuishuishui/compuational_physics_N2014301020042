import pylab as pl
class billiard:
    def __init__(self,α=0.001,r=1,x0=0.2,y0=0.5,vx0=1/pow(2,1/2),vy0=1/pow(2,1/2),total_time=1000,dt=0.01):
        self.α=α
        self.r=r
        self.vx0=vx0
        self.vy0=vy0
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.t=[0]
        self.T=total_time
        self.dt=dt

    def trajectory(self):
        def judge1(x,y):
            return(x*x+(y-self.α*self.r)*(y-self.α*self.r))
        def judge2(x,y):
            return(x*x+(y+self.α*self.r)*(y+self.α*self.r))    

        def nx1(x,y):
            return(x/pow(x*x+(y-self.α*self.r)*(y-self.α*self.r),1/2))
        def ny1(x,y):
            return((y-self.α*self.r)/pow(x*x+(y-self.α*self.r)*(y-self.α*self.r),1/2))
        def vn1(x,y,vx,vy):
            return(vx*nx1(x,y)+vy*ny1(x,y))
        def vx_after1(x,y,vx,vy):
            return((-2*vn1(x,y,vx,vy)*nx1(x,y))+vx)
        def vy_after1(x,y,vx,vy):
            return((-2*vn1(x,y,vx,vy)*ny1(x,y))+vy)
        
        def nx2(x,y):
            return(x/pow(x*x+(y-self.α*self.r)*(y-self.α*self.r),1/2))
        def ny2(x,y):
            return((y-self.α*self.r)/pow(x*x+(y-self.α*self.r)*(y-self.α*self.r),1/2))
        def vn2(x,y,vx,vy):
            return(vx*nx2(x,y)+vy*ny2(x,y))
        def vx_after2(x,y,vx,vy):
            return((-2*vn2(x,y,vx,vy)*nx2(x,y))+vx)
        def vy_after2(x,y,vx,vy):
            return((-2*vn2(x,y,vx,vy)*ny2(x,y))+vy)
        
        while self.t[-1]<self.T:
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.vx.append(self.vx[-1])
            self.vy.append(self.vy[-1])
            self.t.append(self.t[-1]+self.dt)
            if self.y[-1]>=self.α*self.r and judge1(self.x[-1],self.y[-1])>=self.r*self.r:
                for i in range(100):
                    if judge1(self.x[-2]+self.vx[-2]*(i+1)*self.dt/100,self.y[-2]+self.vy[-2]*(i+1)*self.dt/100)>=self.r*self.r:
                        self.x[-1]=self.x[-2]+self.vx[-2]*(i+1)*self.dt/100
                        self.y[-1]=self.y[-2]+self.vy[-2]*(i+1)*self.dt/100
                        self.vx[-1]=(vx_after1(self.x[-1],self.y[-1],self.vx[-2],self.vy[-2]))
                        self.vy[-1]=(vy_after1(self.x[-1],self.y[-1],self.vx[-2],self.vy[-2]))
            if self.y[-1]<=-self.α*self.r and judge2(self.x[-1],self.y[-1])>=self.r*self.r:
                for i in range(100):
                    if judge2(self.x[-2]+self.vx[-2]*(i+1)*self.dt/100,self.y[-2]+self.vy[-2]*(i+1)*self.dt/100)>=self.r*self.r:
                        self.x[-1]=self.x[-2]+self.vx[-2]*(i+1)*self.dt/100
                        self.y[-1]=self.y[-2]+self.vy[-2]*(i+1)*self.dt/100
                        self.vx[-1]=(vx_after2(self.x[-1],self.y[-1],self.vx[-2],self.vy[-2]))
                        self.vy[-1]=(vy_after2(self.x[-1],self.y[-1],self.vx[-2],self.vy[-2]))
            if abs(self.y[-1])<self.α*self.r and abs(self.x[-1])>=self.r:
                for i in range(100):
                    if abs(self.x[-2]+self.vx[-2]*(i+1)*self.dt/100)>=self.r:        
                        self.x[-1]=self.x[-2]+self.vx[-2]*(i+1)*self.dt/100
                        self.y[-1]=self.y[-2]+self.vy[-2]*(i+1)*self.dt/100 
                        self.vx.append(-self.vx[-1])
                        self.vy.append(self.vy[-1])
Vx=[]
X=[]
a=billiard()
a.trajectory()
for i in range(len(a.t)):
    if abs(a.y[i])<pow(pow(a.vx0,2)+pow(a.vy0,2),1/2)*a.dt:
        X.append(a.x[i])
        Vx.append(a.vx[i])
pl.plot(X,Vx,".")
pl.xlabel("X")
pl.ylabel("Vx")
pl.xlim(-1,1)
pl.ylim(-1.05,1.05)
pl.grid(True)
pl.show() 
