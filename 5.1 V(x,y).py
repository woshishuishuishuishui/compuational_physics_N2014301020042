import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as pl
class field:
    def __init__(self,V0=[],a=[],b=[],V=[]):
        self.V0=V0    
        self.a=a
        self.b=b
        for i in range(201):
            self.a.append(0)        
        for j in range(50):
            self.V0.append(self.a)
        
        for i in range(50):
            self.b.append(0)
        for i in range(101):
            self.b.append(1)
        for i in range(50):
            self.b.append(0)
        for i in range(101):
            self.V0.append(self.b)    
        
        for i in range(50):
            self.V0.append(self.a)
        self.V=V
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
            for i in range(101):
                for j in range(101):
                    Vnew[i+50][j+50]=1

        
        for k in range(10000):
            Vold=Vnew
            Vnew=[self.a]
            for i in range(199):
                vtemp=[0]
                for j in range(199):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            Vnew.append(self.a)
            for i in range(101):
                for j in range(101):
                    Vnew[i+50][j+50]=1
            deltaV=[]
            for i in range(201):
                for j in range(201):
                    deltaV.append(abs(Vnew[i][j]-Vold[i][j]))
            S=sum(deltaV)
            if S<0.00001*101*101:
                self.V=Vnew
                print(k)
                break     

v=[]
x=[]
y=[]
z=field()
z.update_V()
for i in range(201):
    for j in range(201):
        v.append(z.V[i][j])
        y.append(1-0.01*i)
        x.append(-1+0.01*j)
fig=plt.figure()  
ax=fig.add_subplot(111, projection='3d') 
ax.plot(x,y,v,".") 
plt.xlabel("x")
plt.ylabel("y")
plt.zlabel("V")
plt.show()
