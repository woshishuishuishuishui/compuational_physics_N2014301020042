import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as pl
class field:
    def __init__(self,V0=[],d=10):
        self.V0=V0    
        self.a=[]
        self.b=[]
        self.c=[]
        self.d=d
        for i in range(61):
            self.a.append(0)        
        for j in range(30-int(self.d/2)):
            self.V0.append(self.a)
        
        for i in range(20):
            self.b.append(0)
        for i in range(21):
            self.b.append(1)
        for i in range(20):
            self.b.append(0)
        self.V0.append(self.b)    
        
        for i in range(int(self.d)-1):
            self.V0.append(self.a)
            
        for i in range(20):
            self.c.append(0)
        for i in range(21):
            self.c.append(-1)
        for i in range(20):
            self.c.append(0)
        self.V0.append(self.c)
        
        for j in range(30-int(self.d/2)):
            self.V0.append(self.a)
        
        self.x=[]
        self.y=[]
        self.V=[]
    def update_V(self):
        Vnew=self.V0
        for k in range(100):
            Vold=Vnew    
            Vnew=[self.a]
            for i in range(30-int(self.d/2)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(19):
                vtemp.append((Vold[30-int(self.d/2)][i]+Vold[30-int(self.d/2)][i+2]+Vold[30-int(self.d/2)-1][i+1]+Vold[30-int(self.d/2)+1][i+1])/4)
            for i in range(21):
                vtemp.append(1)
            for i in range(19):
                vtemp.append((Vold[30-int(self.d/2)][i+40]+Vold[30-int(self.d/2)][i+42]+Vold[30-int(self.d/2)-1][i+41]+Vold[30-int(self.d/2)+1][i+41])/4)
            vtemp.append(0)
            Vnew.append(vtemp)
            
            for i in range(int(self.d)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[30-int(self.d/2)+i][j+1]+Vold[30-int(self.d/2)+i+2][j+1]+Vold[30-int(self.d/2)+i+1][j]+Vold[30-int(self.d/2)+i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(19):
                vtemp.append((Vold[30+int(self.d/2)][i]+Vold[30+int(self.d/2)][i+2]+Vold[30+int(self.d/2)-1][i+1]+Vold[30+int(self.d/2)+1][i+1])/4)
            for i in range(21):
                vtemp.append(-1)
            for i in range(19):
                vtemp.append((Vold[30+int(self.d/2)][i+40]+Vold[30+int(self.d/2)][i+42]+Vold[30+int(self.d/2)-1][i+41]+Vold[30+int(self.d/2)+1][i+41])/4)
            vtemp.append(0)
            Vnew.append(vtemp)    
            
            for i in range(30-int(self.d/2)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[i+35][j+1]+Vold[i+37][j+1]+Vold[i+36][j]+Vold[i+36][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            Vnew.append(self.a)
            
        for k in range(10000):
            Vold=Vnew    
            Vnew=[self.a]
            for i in range(30-int(self.d/2)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[i][j+1]+Vold[i+2][j+1]+Vold[i+1][j]+Vold[i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(19):
                vtemp.append((Vold[30-int(self.d/2)][i]+Vold[30-int(self.d/2)][i+2]+Vold[30-int(self.d/2)-1][i+1]+Vold[30-int(self.d/2)+1][i+1])/4)
            for i in range(21):
                vtemp.append(1)
            for i in range(19):
                vtemp.append((Vold[30-int(self.d/2)][i+40]+Vold[30-int(self.d/2)][i+42]+Vold[30-int(self.d/2)-1][i+41]+Vold[30-int(self.d/2)+1][i+41])/4)
            vtemp.append(0)
            Vnew.append(vtemp)
            
            for i in range(int(self.d)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[30-int(self.d/2)+i][j+1]+Vold[30-int(self.d/2)+i+2][j+1]+Vold[30-int(self.d/2)+i+1][j]+Vold[30-int(self.d/2)+i+1][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            vtemp=[0]
            for i in range(19):
                vtemp.append((Vold[30+int(self.d/2)][i]+Vold[30+int(self.d/2)][i+2]+Vold[30+int(self.d/2)-1][i+1]+Vold[30+int(self.d/2)+1][i+1])/4)
            for i in range(21):
                vtemp.append(-1)
            for i in range(19):
                vtemp.append((Vold[30+int(self.d/2)][i+40]+Vold[30+int(self.d/2)][i+42]+Vold[30+int(self.d/2)-1][i+41]+Vold[30+int(self.d/2)+1][i+41])/4)
            vtemp.append(0)
            Vnew.append(vtemp)    
            
            for i in range(30-int(self.d/2)-1):
                vtemp=[0]
                for j in range(59):
                    vtemp.append((Vold[i+35][j+1]+Vold[i+37][j+1]+Vold[i+36][j]+Vold[i+36][j+2])/4)
                vtemp.append(0)
                Vnew.append(vtemp)
            
            Vnew.append(self.a)
            
            deltaV=[]
            for i in range(61):
                for j in range(61):
                    deltaV.append(abs(Vnew[i][j]-Vold[i][j]))
            S=sum(deltaV)
            if S<0.00001*61*61:
                print(k)
                self.V=Vnew
                break     


v=[]
x=[]
y=[]
z=field()
z.update_V()
for i in range(61):
    for j in range(61):
        v.append(z.V[i][j])
        y.append(-30+j)
        x.append(-30+i)
fig=plt.figure()  
ax=fig.add_subplot(111, projection='3d') 
ax.plot(x,y,v) 
plt.xlabel("x")
plt.ylabel("y")
plt.zlabel("V")
plt.show()
