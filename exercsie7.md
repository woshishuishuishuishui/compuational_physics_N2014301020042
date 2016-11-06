#摘要：
problem3.12 3.13 3.14 

#背景介绍：

poincare section是一种有效的研究问题的方法，他是一种很重要的思想。

经过3.2、3.3节，我们知道了，物理摆作为一个数学问题是可预知的，但是作为物理问题，他是不可预知的，意思是当初始条件或者某一方程中的系数有一较小变化时，解会有很大的偏离，通过题目可以印证这一点。

物理摆的微分方程和相关的欧拉法将方程转换为代码方法在课本上很详细。

#正文：
##3.12：poincare section：
##[代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.12代码.py)

在t=2nπ/Ω时作出的轨迹图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/0的庞加莱.png)

在t=(2nπ+π/4)/Ω时作出的轨迹图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/0.25pi的庞加莱.png)

在t=(2nπ+π/2)/Ω时做出的轨迹图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/0.5pi的庞加莱.png)



##3.13：解对θ0的稳定性：
##[FD=1.2的代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.13角位移的稳定性.py)
##[FD=0.5的代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/3.13角位移的稳定性FD%3D0.5.py)

FD=0.5时，取13个极大值点所在点：
                   
                   4.1127，-0.459807
                   7.41935,-1.24024
                   11.0081,-2.21579
                   14.5565,-3.15882
                   18.1048,-3.77666
                   21.7339,-4.524558
                   25.5242,-5.50013
                   29.1532,-6.57323
                   32.7823,-7.32115
                   36.2903,-8.00403
                   39.9194,-8.88202
                   43.75,-9.92261
                   47.2581,-10.8331
                   用计算器计算回归系数：B=-0.237024 A=0.476012
                   因此 logΔθ=Bt+A Δθ=e^A*e^Bt=1.6096*e^-0.2370t
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/FD%3D0.5的角位移差.png)

FD=1.2时，取8个极大值点所在点：
                  
                  5.92742，-6.92612
                  10.7258,-7.19667
                  14.5565,-7.75858
                  24.1935,-5.36524
                  29.7177,-4.72008
                  33.5484,-5.32362
                  43.1855,-1.55671
                  47.5806,-2.01457
                  用计算器计算回归系数：B=0.141568 A=-8.813870
                  因此 logΔθ=Bt+A Δθ=e^A*e^Bt=1.4866*10^(-4)*e^0.1416t 
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/初始角位移为0.2和0.2-0.001的差.png)

##3.14：解对q的稳定性：
##[FD=1.2的代码](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/解对q的稳定性.py)

对FD=0.5的代码完全一样

FD=1.2时，取8个极值点所在点：
                
                0.369624,-12.6543
                5.24194,-6.0986
                10.4503,-3.89776
                14.1801,-4.36602
                23.9919,-1.36915
                29.2003,-1.1116
                33.0981,-1.67352
                44.5901,0.433663
                用计算器计算回归系数：B=0.235786    A=-8.590968
                因此 logΔθ=Bt+A Δθ=e^A*e^Bt=1.8578*10^(-4)*e^0.2358t 
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/解对q的稳定性，FD%3D1.2.png)

FD=0.5时，取7个极值点所在点：

                1.07527,-10.7648
                3.83065,-8.19459
                7.42608,-7.01873
                11.4919,-6.71696
                15.8938,-6.69615
                20.4301,-6.75858
                25.1008,-6.80021
                用计算器计算回归系数：B=0.123403 A=-9.067140
                因此 logΔθ=Bt+A Δθ=e^A*e^Bt=1.1540*10^(-4)*e^0.1234t
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/解对q的稳定性，FD%3D0.5.png)

#结论：

3.12poincare section的做法很有意义，实际研究问题中是一种很巧妙的研究方法。

物理摆对于初始条件有可能是不稳定的，在3.13中FD=1.2时Δθ=e^A*e^Bt=1.4866*10^(-4)*e^0.1416t，由指数函数性质可知，这解对于初始条件θ0的较小变化，会有很大的偏离。

3.14虽然不是解的稳定性问题，是微分方程中系数的变化，但是也是说明了q因子的小变化，可能导致解的很大偏离。

由3.13和3.14，我们知道了什么是物理摆的不可预知性

#参考：

课本3.3 

蔡浩讲义 

秦大粤代码 
