#摘要：
problem4.8,4.9

#背景介绍：

用欧拉法解太阳系内行星运动，计算T、a，验证开普勒第三定律。

对于非平方反比力的不闭合轨道，验证一下“轨道越圆，质点运动的下一圈和这一圈的差别越小”。

#正文：

运动方程在课本上非常清楚，并按照例4.1来写程序，课本说这样写的是比较准的，而原来那种写法本身就计算不出一个很好的解。

##4.8：
按照牛顿定律解出的远日点速度式子（4.11）和远日点到日距离为a（1+e），并按照表4.1中m、a、e，计算出远日点速度和远日点距离作为初始条件，按照欧拉法计算出解。

如果初始y=0，求a就取行星第一次穿过y轴的点，计算他与初始位置的横坐标之差绝对值为2a。

如果初始y=0，vy>0，求T就取行星第一次从下往上穿过y轴的点，它对应的和初始时刻的时间为T。

##[代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.8.py)

初始条件是九大行星的初始条件，轨迹图：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/前四个轨迹图.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/后五个轨迹图.png)

对应的打印出的T、a、T^2/a^3：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/前四个数据.png)

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/后五个数据.png)

其中前两个数据顺序颠倒一下后，列出的9个结果就是按距日距离从小到大的顺序排列的数据结果。

##4.9：
取β=2.05，根据牛顿定律，可以算得如果初始条件满足v^2*r^(β-1)=4π^2，且初速度与到太阳的初位移垂直，那么将做圆周运动。

改变初始v^2*r^(β-1)，它偏离4π^2越远，认为它的第一周运动越不圆，越接近4π^2，认为它的第一周越圆（前提运动是可以完成2π旋转的，第一周的意思就是完成第一次2π旋转）

在这，取定r0=1，改变v来实现偏离圆形轨道。

##[某一个初始条件的代码示例](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/4.9哦.py)

改变v，同时某些时候需要改变T，使周数足够让我们观察它的轨道偏离封闭轨道状态的“速度”是快是慢。

结果示意图：

##v=2π（是圆周运动的条件）：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.1π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.1pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.2π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.2pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.3π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.3pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.4π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.4pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.5π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.5pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.6π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.6pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=2.7π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D2.7pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.9π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.9pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.8π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.8pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.7π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.7pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.6π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.6pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.5π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.5pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.4π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.4pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.3π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.3pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.2π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.2pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.1π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1.1pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=1.0π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D1pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=0.9π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D0.9pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=0.8π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D0.8pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=0.7π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D0.7pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=0.6π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D0.6pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)

##v=0.5π：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/v%3D0.5pi，v%5E2xr%5E(β-1)%3D4pi%5E2.png)


通过观察可以验证题目最后给出的判断

#结论：
4.8题9大行星初始条件代入后，算得的T^2/a^3十分接近1，这符合普勒第三定律，并且按照牛顿定律，该值理论上为1，故计算的结果比较符合定律。

当然只要初始条件能够使轨迹是椭圆的，那么它就应该满足T^2/a^3=1，随意输出初始条件计算的结果确实符合这一点。

4.9题我们对β=2.05，偏离圆封闭轨道的不同初始条件下的轨道做了详细的轨迹图，充分验证了题目让我们验证的结论：在β不为2时，轨道是不封闭的，并且轨道如果偏离圆轨道越远（轨道完全由初始条件给定，所以偏离圆轨道的程度就是初始条件偏离圆封闭轨道初始条件的程度），则轨道不封闭程度越高，即它相邻两周的轨迹差别越大。

#参考：
课本4.1 4.2
