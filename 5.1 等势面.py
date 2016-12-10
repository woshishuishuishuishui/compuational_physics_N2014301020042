import pylab as pl
class field:
    def __init__(self,V0=[],a=[],b=[]):
        self.V0=V0    
        self.a=a
        self.b=b
        for i in range(401):
            self.a.append(0)        
        for j in range(100):
            self.V0.append(self.a)
        
        for i in range(100):
            self.b.append(0)
        for i in range(201):
            self.b.append(1)
        for i in range(100):
            self.b.append(0)
        for i in range(201):
            self.V0.append(self.b)    
        
        for i in range(100):
            self.V0.append(self.a)
        self.x=[]
        self.y=[]
    def update_V(self):
        Vnew=self.V0
        for k in range(100):
            Vold=Vnew
            Vnew=[self.a]
            for i in range(399):
                vtemp=[0]
                for j in range(399):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            Vnew.append(self.a)
            for i in range(201):
                for j in range(201):
                    Vnew[i+100][j+100]=1

        
        for k in range(10000):
            Vold=Vnew
            Vnew=[self.a]
            for i in range(399):
                vtemp=[0]
                for j in range(399):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            Vnew.append(self.a)
            for i in range(201):
                for j in range(201):
                    Vnew[i+100][j+100]=1
            deltaV=[]
            for i in range(401):
                for j in range(401):
                    deltaV.append(abs(Vnew[i][j]-Vold[i][j]))
            S=sum(deltaV)
            if S<0.00001*401*401:
                V=Vnew
                print(k)
                break     

        for k in range(4):
            for i in range(401):
                for j in range(401):
                    if abs(V[i][j]-0.2*(k+1))<0.01:
                        self.x.append(-2+0.01*i)
                        self.y.append(2-0.01*j)
                      
a=[-1,-1,1,1,-1]
b=[-1,1,1,-1,-1]            
c=[-2,-2,2,2,-2]
d=[-2,2,2,-2,-2]               

z=field()
z.update_V()
pl.plot(z.x,z.y,".")
pl.plot(a,b)
pl.plot(c,d)
pl.grid(True)
pl.show()

