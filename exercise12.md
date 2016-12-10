#摘要：
problem5.1，5.4
#背景介绍：
拉普拉斯方程的解法和之前章节不同，需要用到relaxation方法，就是通过循环，递推出一个比较精确的解。这里用到的方法是雅克比法，它的介绍在书上有，可以看出它很依赖边界条件。

#正文：
程序主要通过三个功能实现，一是输入初始解，二是递推，三是每次递推后检验最新的解是不是收敛程度很高了可以认为是精确解了。

##[等势面的代码：5.1](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.1%20等势面.py)

等势面的结果图：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161210214015.png)


由里到外等势线电势为0.8,0.6,0.4,0.2.

##[V=V(x,y)图像的代码：5.1](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/5.1%20等势面.py)

V=V(x,y)图像结果如下：


#结论：
结果显示解具有预想的对称性：关于y=±x对称，关于x、y轴对称。
需要进一步实践，多了解拉普拉斯方程的计算物理解法。
仔细观察程序存在小错误，具体是略微改变了边界条件，但是结果并没有很大出入。受制于时间下次再做不会再犯这种错。
