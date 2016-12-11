#摘要：
problem5.1，5.4
#背景介绍：
拉普拉斯方程的解法和之前章节不同，需要用到relaxation方法，就是通过循环，递推出一个比较精确的解。这里用到的方法是雅克比法，它的介绍在书上有，可以看出它很依赖边界条件。

#正文：
程序主要通过三个功能实现，一是输入初始解，二是递推，三是每次递推后检验最新的解是不是收敛程度很高了可以认为是精确解了。

##[等势线的代码：5.1](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.1%20等势面.py)

等势线的结果图：此时网格分为401*401的网格，大正方形边界是4*4的，小正方形是2*2的

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161210214015.png)


由里到外等势线电势为0.8,0.6,0.4,0.2.

##[V=V(x,y)图像的代码：5.1](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.1%20V(x%2Cy).py)

V=V(x,y)图像结果如下：此时内部正方形为1*1，外部为2*2，分了101*101的网格

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.1V(x%2Cy).png)

##[等势线的代码：5.4，121*121的网格](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4等势图%20121x121.py)

等势线的结果图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4等势图%20121x121.png)


##[等势线的代码：5.4，61*61的网格](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4等势图%2061x61.py)

等势线的结果图：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4等势图%2061x61.png)

##[V=V(x,y)图像的代码：5.4，网格时61*61的](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4%20V(x，y).py)


V=V(x,y)图像结果如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.4V(x%2Cy)，61x61.png)




#结论：
5.1结果显示解具有预想的对称性：关于y=±x对称，关于x、y轴对称。5.4结果显示它也具有对称性，关于x轴对称，等势图关于x、y都对称。


从5.4可以看出网格分的细时得出的等势图更精确，更好看，但是结果显示61*61的网格需要1000次左右的循环。121*121的网格需要2500次左右的循环。


5.1程序存在小错误，具体是略微改变了边界条件，但是结果并没有很大出入。5.4改正了错误，篇幅增大很多。
