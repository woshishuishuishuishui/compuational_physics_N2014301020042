#摘要：
problem4.19,4.20

#背景介绍：
用欧拉法解卫星的自转运动，说明解是混沌的，写出程序能计算L系数与离心率e的关系。

非混沌解的Δθ-t，且不限制θ在2π长的区间中，发现它起伏明显，说明理由。

#正文：

运动方程在课本上非常清楚，没必要再写。

##4.19：
##[代码：做出给定e，略改变初始条件的Δθ-t](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.19，不同e的deltaθ-t.py)

不限制θ在2π区间内，程序可以实现做出给定离心率的轨迹图、θ-t图等。

初始条件为θ0=0和θ0=0.01作出的Δθ-t，行星轨迹在远“日”点开始。

结果如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第一组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第二组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第三组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第四组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第五组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第六组.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/第七组.png)

可以看出前八个解不是混沌的，之后的是。


##[在此基础上计算L系数，从0到0.95取20个等间隔0.05的离心率来求L，利用了线性回归方程的公式。代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.19，不同e的deltaθ-t.py)

L-e的散点图和L值列表，结果如下：


![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/L系数结果.png)


#4.20:

[作出e=0.1，θ0=0和θ0=0.01的Δθ-t、w1-t、w2-t、Δw-t代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.20.py)

结果图如下，依次是Δθ-t w1-t w2-t Δw=w1-w2 - t ：


![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.20Δθ-t和w1-t.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.20w2-t和Δw-t.png)

e=0.1时的解根本不是混沌的(对θ0来说)，从他的Δθ-t来看。


#结论：
