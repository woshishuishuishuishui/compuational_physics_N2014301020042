import pylab as pl
class field:
    def __init__(self,V0=[],a=[],b=[],c=[],d=10):
        self.V0=V0    
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        for i in range(201):
            self.a.append(0)        
        for j in range(100-int(self.d/2)):
            self.V0.append(self.a)
        
        for i in range(90):
            self.b.append(0)
        for i in range(21):
            self.b.append(1)
        for i in range(90):
            self.b.append(0)
        self.V0.append(self.b)    
        
        for i in range(self.d-1):
            self.V0.append(self.a)
            
        for i in range(90):
            self.c.append(0)
        for i in range(21):
            self.c.append(-1)
        for i in range(90):
            self.c.append(0)
        self.V0.append(self.c)
        
        for j in range(100-int(self.d/2)):
            self.V0.append(self.a)
        
        self.x=[]
        self.y=[]
    def update_V(self):
        Vnew=self.V0
        for k in range(100):
            Vold=Vnew    
            Vnew=[self.a]
            for i in range(199):
                vtemp=[0]
                for j in range(199):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
                Vnew.append(self.a)
            for l in range(21):
                Vnew[100-int(self.d/2)][l+90]=1
                Vnew[100+int(self.d/2)][l+90]=-1
        
        for k in range(10000):
            Vold=Vnew
            Vnew=[self.a]
            for i in range(199):
                vtemp=[0]
                for j in range(199):
                    vtemp.append((Vold[i][j]+Vold[i+2][j]+Vold[i][j+2]+Vold[i+2][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            Vnew.append(self.a)
            for l in range(21):
                Vnew[100-int(self.d/2)][l+90]=1
                Vnew[100+int(self.d/2)][l+90]=-1
            deltaV=[]
            for i in range(201):
                for j in range(201):
                    deltaV.append(abs(Vnew[i][j]-Vold[i][j]))
            S=sum(deltaV)
            if S<0.00001*201*201:
                V=Vnew
                print(k)
                break     

        for k in range(9):
            for i in range(201):
                for j in range(201):
                    if abs(V[i][j]-0.1*(k+1))<0.01:
                        self.x.append(-100+j)
                        self.y.append(-100+i)
                    if abs(V[i][j]+0.1*(k+1))<0.01:
                        self.x.append(-100+j)
                        self.y.append(-100+i) 
            
z=field()
z.update_V()
a=[-100,-100,100,100,-100]            
b=[-100,100,100,-100,-100]
c=[-z.d/2,-z.d/2]
d=[-10,10]
e=[z.d/2,z.d/2]
f=[10,-10]              
pl.plot(z.x,z.y,".")
pl.plot(a,b)
pl.plot(c,d)
pl.plot(e,f)
pl.grid(True)
pl.show()
