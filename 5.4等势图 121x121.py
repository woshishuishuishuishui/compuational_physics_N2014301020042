import pylab as pl
class field:
    def __init__(self,V0=[],d=10):
        self.V0=V0    
        self.a=[]
        self.b=[]
        self.c=[]
        self.d=d
        for i in range(121):
            self.a.append(0)        
        for j in range(60-int(self.d/2)):
            self.V0.append(self.a)
        
        for i in range(40):
            self.b.append(0)
        for i in range(41):
            self.b.append(1)
        for i in range(40):
            self.b.append(0)
        self.V0.append(self.b)    
        
        for i in range(int(self.d)-1):
            self.V0.append(self.a)
            
        for i in range(40):
            self.c.append(0)
        for i in range(41):
            self.c.append(-1)
        for i in range(40):
            self.c.append(0)
        self.V0.append(self.c)
        
        for j in range(60-int(self.d/2)):
            self.V0.append(self.a)
        
        self.V=[]
    def update_V(self):
        Vnew=self.V0
        for k in range(100):
            Vold=Vnew    
            Vnew=[self.a]
            for i in range(60-int(self.d/2)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(39):
                vtemp.append((Vold[60-int(self.d/2)][i]+Vold[60-int(self.d/2)][i+2]+Vold[60-int(self.d/2)-1][i+1]+Vold[60-int(self.d/2)+1][i+1])/4)
            for i in range(41):
                vtemp.append(1)
            for i in range(39):
                vtemp.append((Vold[60-int(self.d/2)][i+80]+Vold[60-int(self.d/2)][i+82]+Vold[60-int(self.d/2)-1][i+81]+Vold[60-int(self.d/2)+1][i+81])/4)
            vtemp.append(0)
            Vnew.append(vtemp)
            
            for i in range(int(self.d)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[60-int(self.d/2)+i][j+1]+Vold[60-int(self.d/2)+i+2][j+1]+Vold[60-int(self.d/2)+i+1][j]+Vold[60-int(self.d/2)+i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(39):
                vtemp.append((Vold[60+int(self.d/2)][i]+Vold[60+int(self.d/2)][i+2]+Vold[60+int(self.d/2)-1][i+1]+Vold[60+int(self.d/2)+1][i+1])/4)
            for i in range(41):
                vtemp.append(-1)
            for i in range(39):
                vtemp.append((Vold[60+int(self.d/2)][i+80]+Vold[60+int(self.d/2)][i+82]+Vold[60+int(self.d/2)-1][i+81]+Vold[60+int(self.d/2)+1][i+81])/4)
            vtemp.append(0)
            Vnew.append(vtemp)    
            
            for i in range(60-int(self.d/2)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[i+60+int(self.d/2)][j+1]+Vold[i+60+int(self.d/2)+2][j+1]+Vold[i+60+int(self.d/2)+1][j]+Vold[i+60+int(self.d/2)+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            Vnew.append(self.a)
            
        for k in range(10000):
            Vold=Vnew    
            Vnew=[self.a]
            for i in range(60-int(self.d/2)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(39):
                vtemp.append((Vold[60-int(self.d/2)][i]+Vold[60-int(self.d/2)][i+2]+Vold[60-int(self.d/2)-1][i+1]+Vold[60-int(self.d/2)+1][i+1])/4)
            for i in range(41):
                vtemp.append(1)
            for i in range(39):
                vtemp.append((Vold[60-int(self.d/2)][i+80]+Vold[60-int(self.d/2)][i+82]+Vold[60-int(self.d/2)-1][i+81]+Vold[60-int(self.d/2)+1][i+81])/4)
            vtemp.append(0)
            Vnew.append(vtemp)
            
            for i in range(int(self.d)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[60-int(self.d/2)+i][j+1]+Vold[60-int(self.d/2)+i+2][j+1]+Vold[60-int(self.d/2)+i+1][j]+Vold[60-int(self.d/2)+i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(39):
                vtemp.append((Vold[60+int(self.d/2)][i]+Vold[60+int(self.d/2)][i+2]+Vold[60+int(self.d/2)-1][i+1]+Vold[60+int(self.d/2)+1][i+1])/4)
            for i in range(41):
                vtemp.append(-1)
            for i in range(39):
                vtemp.append((Vold[60+int(self.d/2)][i+80]+Vold[60+int(self.d/2)][i+82]+Vold[60+int(self.d/2)-1][i+81]+Vold[60+int(self.d/2)+1][i+81])/4)
            vtemp.append(0)
            Vnew.append(vtemp)    
            
            for i in range(60-int(self.d/2)-1):
                vtemp=[0]
                for j in range(119):
                    vtemp.append((Vold[i+60+int(self.d/2)][j+1]+Vold[i+60+int(self.d/2)+2][j+1]+Vold[i+60+int(self.d/2)+1][j]+Vold[i+60+int(self.d/2)+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            Vnew.append(self.a)
            
            deltaV=[]
            for i in range(121):
                for j in range(121):
                    deltaV.append(abs(Vnew[i][j]-Vold[i][j]))
            S=sum(deltaV)
            if S<0.00001*121*121:
                print(k)
                self.V=Vnew
                break     

v=[]
x=[]
y=[]
z=field(d=20)
z.update_V()
for k in range(4):
    for i in range(121):
        for j in range(121):
            if abs(z.V[i][j]-0.2*(k+1))<0.01:
                x.append(-60+i)
                y.append(-60+j)
            if abs(z.V[i][j]+0.2*(k+1))<0.01:
                x.append(-60+i)
                y.append(-60+j) 
a=[-60,-60,60,60,-60]            
b=[-60,60,60,-60,-60]
c=[-z.d/2,-z.d/2]
d=[-20,20]
e=[z.d/2,z.d/2]
f=[20,-20] 
pl.plot(x,y,".")
pl.plot(a,b)
pl.plot(c,d)
pl.plot(e,f)
pl.grid(True)
pl.show()    

