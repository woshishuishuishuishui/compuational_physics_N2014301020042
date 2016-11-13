#摘要：
problem3.18 3.19 3.20 3.21

#背景介绍：

3.4节通过讲解向我们说明物理摆达到稳定后的周期并不一定是驱动力FD的周期，摆的解是许多Ω'=k*Ω的摆的叠加。并告诉我们物理摆达到混沌状态的方式是，随FD向某一值变化过程，物理摆稳定后的周期逐渐增加，增加的方式是T'=2^n*T，周期越来越大，直到周期性消失。

一个体现这一点的方法是poincare section。根据poincare section的想法，随着FD的相位改变，相应的观察同时刻物理摆的解，具体的，FD相位每改变2π，即每隔Δt=T，取一下物理摆的θ和ω。如果物理摆稳定后的周期T'=T，则达到稳定后，每次隔观察Δt=T到的(θ，ω)是相同的。如果物理摆稳定后周T'=2^n*T，则达到稳定后，每隔Δt=2^n*T(θ，ω)是相同的，若将每相邻2^n次观察分为一组，则组内(θ，ω)各不相同，但是再之后的一组2^n次观察值会重复上一组2^n次观察的(θ，ω)。物理摆稳定后开始取点，做出的poincare section是有2^n个点的图。

另一个可以验证这种增加的方式是T'=2^n*T的方法是bifurcation diagram。根据bifurcation diagram的概念，他的想法和庞加莱想法相同，但是可以更加直观的看到多大的FD的物理摆解是T'=2^n*T的，并且T'随FD的变化。

#正文：

##3.18：
##[代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.18代码.py)

做的poincare section是从300个周期以后取的点，这时以后肯定是稳定状态的。不然没达到稳定的点会干扰轨迹图，没法看周期是几倍T。

FD=1.4时的poincare section：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.18%20FD%3D1.4.png)

FD=1.44时的poincare section：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.18%20F%3D1.44.png)

FD=1.465时的poincare section：![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.18%20FD%3D1.465.png)


##3.19：
如背景介绍说的，这题中说的取点方法没法验证物理摆稳定后的周期T'=2^n*T。

##3.20：
##[代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.20代码.py)

运行图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.20图.png)


代码中将1.35到1.5等分为100份。
运行图中的FD=1.44，我们认为它的解稳定后的周期为2T，理由如背景介绍所说，因为它对应“两团”θ，但是它确实是很多个θ，原因是，通过我们的代码可以看出，我们把时间分为间隔dt长度的左开右闭区间，再来逐
个区间检验庞加莱想取的时间点在不在这个区间内，所以说我们取的点和庞加莱想取的点差距小于dt，不一定是庞加莱想取的那个点，因此受dt的限制，不是严格的按庞加
莱的想法每隔T取点。所以会出现运行图的bifurcation diagram中每个FD会对应“很多”个点，而不是2^n个，但是还是能够区分的，在n较小时。

bifurcation不知道怎么求，这个图实在太糙了

##3.21：
可以通过运行程序时改变相关参量来运行

#结论：
通过3.18和3.20两种方法，可以验证物理摆稳定后的周期为2^n*T。

3.18的优点在于数点容易，缺点在于只能逐个点去验证。

3.20的优点在于可以看出一个FD的摆达到稳定后的周期为多少，并且可以看出物理摆是随FD增大(至少是从FD=1.35开始)，周期逐渐增大，然后达到混沌。缺点是如果你的dt不够小，每一个点实际是一个“点团”，实际操作来数一个FD为几个点非常难。并且有一个矛盾，你的FD分的越粗，你越好数点，但是分的越粗糙，越不容易分析什么时候周期倍增。

#参考：
主要参考上一次的作业。

课本3.4节
