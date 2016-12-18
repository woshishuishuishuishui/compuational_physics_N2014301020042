#摘要：
problem6.9 6.10 6.12 6.13
#背景介绍：
含时的线性偏微分方程：波动方程 也可以用计算方法得出解，对质点位置的偏导数的近似在电场求解中已经用过，对于时间的偏导数也是一样。

最终达到的效果是：一个质点在t时刻的位移由它自己在之前t-dt和t-2dt的位移以及它相邻两个质点在t-dt的位移递推得出。

具体表达：y(i,n+1)=2(1-r^2)y(i,n)-y(i,n-1)+r^2*[y(i+1,n)+y(i-1,n)]   r=cΔt/Δx

此次作业包含两种类型边界条件的弦振动，两端固定的弦，和一端自由一端固定的弦。

如果是两端固定的弦，递推表达式可以用在除两端点的所有质点上，只要给出前两个时刻的波形图、波形函数，并且根据课本我们的初始条件一直取为：初始时刻各个质点速度为0，因此只需要给出一个时刻的波形图，我们认为第二个时刻的波形图不变，也就是等同于认为初始条件：初始时刻各质点速度为0.

如果是一端自由的弦，递推表达式在两端点外的质点上的处理与两端固定时一样，但是自由端（设为右端）的位移表达关系需要改动一下，根据课本介绍P158-P159，具体表达为：

y(M,n+1)=2(1-r^2/2)y(M,n)-y(M,n-1)+r^2*y(M-1,n)     M为最右端质点位置的计数值

这样对于两种边界条件的弦我们根据以上递推和初始波形图就可以得出波动方程的解。

另外根据课本介绍r=cΔt/Δx在取为1时结果比较精确。

#正文：
#[6.9:画波形图、频谱图的代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9波形图%20傅里叶系数%20.py)

波形图展示：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9波形图1.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9波形图2.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9波形图3.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9波形图4.png)


频谱图展示：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.9%20频率3000.png)

作为对比，做一个两端固定的弦，初始条件相同的频谱图，它的代码在6.12题的正文中有：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12频谱%20高斯波包.png)

#[6.10代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.10.py)

根据背景介绍，我们的初始条件是全部质点的初速度为0，在此初始条件下，波动方程解为：

u(x,t)=ΣDn * cos(nπct/L) * sin(nπx/L)    ,    Dn=(2/L)∫φ(x)sin(nπx/L)dx

可见如果我们的初始波形φ(x)=sin(3πx/L)，那么只有D3不为0，其余Dn为0(本征函数正交性)

将此初始波形写入程序，运行后得到频谱图：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.10%20频谱.png)

发现这正符合预期，在n=3，对应的f=450Hz处，有非0系数，而其余f对应的系数均为0.


#[6.12代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12%20频谱%20直线%20高斯波包.py)

此处代码做出了高斯波包中心点在X0=0.4频谱图，和符合真实吉他弦初始条件的：在X0=0.4处提起弦，初始波形由以(0,0) (0.4,1) (1,0)为端点的两条线段组成的频谱图。

结果展示：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12频谱%20高斯波包.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12频谱%20直线.png)

可见真实情形的频谱图只包含f=150Hz一个明显的频率，这说明此初始条件下弹出的音调为150Hz的频率。

如果我们改变弦的材料就是改变c值，相应的改变了c/2L的值，就可以改变吉他的效果。

当然如果改变初始条件，也会得到不同的频谱，也就是弹出不同的音调，稍微改变代码，改变初始直线波形的最高点位置，即弹的位置：

X0=0.2：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12%20直线%200.2.png)

X0=0.1：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.12%20直线%200.1.png)

与X0=0.4的频谱果然有不同。这证明了弹不同的位置会有不同的音调组合，但是基频150Hz总是主要成分。

#[6.12代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.13%20频谱对比.py)


此处高斯波包的中心点在X0=0.4,根据这个代码可以看出我们可以做出考察点在x0=0.1,0.4,0.5的频谱图：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/6.13%20频谱对比.png)


#结论：

6.9的一端自由的弦的解与两端固定的弦的频谱图不同，他的基频不是150Hz(c/2L)

6.10利用解析解和计算方法得到的解去验证同一个问题得到一致结论，一定程度证明计算方法得到的解释精确的

6.12研究初始条件贴近真实吉他情形的两端固定弦，发现它的频谱以基频为主要成分，改变波形图即改变弹吉拨动弦的位置，可以发现频谱图成分发生明显变化，但是基频还是主要成分。如果再去改变基频，即改变弦的材料，就可以实现不同的音效。

6.13发现不同考察点频谱成分有差异，这也是符合解析解的结果的，因为u(x,t)=ΣDn * cos(nπct/L) * sin(nπx/L)，如果固定考察点，Dn * sin(nπx/L)为傅里叶系数，可见它是和考察点位置x紧密相关的

#致谢：

课本6.1,6.2

学长们的代码，如何求傅里叶系数部分，np.fft.rfft的用法
