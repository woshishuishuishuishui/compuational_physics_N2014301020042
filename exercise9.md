#摘要：
problem3.30

#背景介绍：

3.7节介绍了混沌的另一模型，运动场形状桌子的桌球。运动场形桌球是什么在课本上介绍的很详细。碰撞都是弹性的无摩擦的。

写出程序画出桌球的运动轨迹图和phase-space图。phase-space图的想法和庞加莱图想法相似。

模拟出桌球的运动后，研究混沌现象，对不同的运动场直跑道α=0.1,0.01,0.001，改变初位置、初速度，求Lyapunov系数。

#正文：

运动方程非常简单，课本上说的很详细，靠运动方程和欧拉法来写程序。

##关键点1：
如何确定碰撞点：课本P83介绍了一种方法是，欧拉法下，桌球一步一步的移动，每次dt移动后判断出界了吗，如果出界了，退回前一步，然后将这界内界外两相邻点之间再均分100份，一步步进行，当桌球再出界时，可认为这新出界点是碰撞点，代替最初没均分100份时的最后一步即可。

##关键点2：
确定了碰撞点后，需计算碰撞后的速度。下面推导，碰撞点为圆周部分的点时，用碰撞点和碰撞前速度，表示碰撞后速度，矢量表示方法：|x>

设碰前速度|v>,分速度vx，vy，碰后|v'>，分速度vx',vy',碰撞点的指向桌外的单位法向量|n>，分量nx，ny，某个与|n>垂直的单位向量为|n//>，碰撞点为(x，y)

根据碰撞前后法向速度反向，切向速度不变的规律：

|v>=(|v>·|n>)|n>+(|v>·|n//>)|n//>

|v'>=-(|v>·|n>)|n>+(|v>·|n//>)|n//>

消去|n//>：|v'>=|v>-2(|v>·|n>)|n>

对此式点乘分别|ex>、|ey>：

vx'=vx-2(|v>·|n>)nx

vy'=vy-2(|v>·|n>)ny

而|n>=|ex>(x-x0)/[(x-x0)^2+(y-y0)^2]^0.5+|ey>(y-y0)/[(x-x0)^2+(y-y0)^2]^0.5，x0，y0为圆心坐标，nx，ny也可用x，y表示。代入后：

vx'=vx-2(|v>·|n>)(x-x0)/[(x-x0)^2+(y-y0)^2]^0.5

vy'=vy-2(|v>·|n>)(y-y0)/[(x-x0)^2+(y-y0)^2]^0.5

这样就达到了目的：用碰撞前速度和碰撞点表示碰撞后速度。

##3.30：
做出桌球运动轨迹图： 
##[α=0.001轨迹图代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.30a%3D0.001轨迹图.py)

做出桌球运动的phase-space图：
##[α=0.001P-S代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.30a%3D0.001PS图.py)

结果：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.001，T%3D500轨迹图.png)
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.001，T%3D2000PS图.png)

##α=0.01的代码只用改变一下初始条件：α，总时间T（适当的时间做出来的图好看）

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.01，T%3D100轨迹图.png)
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.01，T%3D2000PS图.png)

##α=0.1：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.1，T%3D500轨迹图.png)
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.1，T%3D1000PS图.png)

##用了以上基础，稍微添加代码就可以做出细微改变初始条件时候的logR-t图像，R为两个不同解的桌球的距离。

##[总时间T=50内的logR-t的代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.30求logR-t.py)

##α=0.001，初始x0=0.2和x0=0.201的logR-t：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.001x0%3D0.201x0%3D0.2，T%3D50.png)

##α=0.01，初始x0=0.2和x0=0.201的logR-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.01，x0%3D0.201，x0%3D0.2，T%3D50.png)

##α=0.1，初始x0=0.2和x0=0.201的logR-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.1%2Cx0%3D0.201x0%3D0.2，T%3D50.png)

##α=0.001，初始vx0=0.8和vx0=0.801的logR-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.001，vx0%3D0.8vx0%3D0.801，T%3D50.png)

##α=0.01，初始vx0=0.8和vx0=0.801的logR-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.01，vx0%3D0.8vx0%3D0.801T%3D50.png)

##α=0.1，初始vx0=0.8和vx0=0.801的logR-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/α%3D0.1vx0%3D0.8vx0%3D0.801T%3D50.png)

##计算Lyapunov系数的方法：
在图上取点，输入计算器，计算线性回归方程的斜率，截距，相关系数，不能把所有点输进去是缺点。

例：α=0.01，x0=0.2和x0=0.201的logR-t：取点：
                                        
                                         (1.85484,-7.34378)
                                         
                                         (5.28226,-6.62968)
                                         
                                         (11.9758,-5.88046)
                                         
                                         (16.1694,-5.33025)
                                         
                                         (21.4113,-4.8737)
                                         
                                         (27.5,-4.26496)
                                        
                                         (31.4919,-3.82011)
                                         
                                         计算得：斜率B=0.1138208 截距A=-7.3300511 相关系数r=0.9945826
                                         
                                         
                                         因此它的Lyapunov系数为0.1138208。
