#期末作业：乐器中的振动与波的物理分析  
齐诚  2014301020042     物基1  

#摘要：  
应用振动与波的物理知识和计算方法来说明决定乐器音调、音色的物理条件，并分析这些条件的影响。  





#背景介绍：  
第六章中我们对波动方程的解进行了计算方法的研究，具体计算了两端点固定或者一端固定的弦，初始条件为各点初速度均为0、初波形图给定的波动方程的解。其中练习题6.12引出了一个初始条件、边界条件与吉他弦相近的问题。  

本次作业我们接着这个内容，应用振动与波的物理内容，说明决定乐器发出音调的物理条件有哪些，并用计算方法分析这些物理条件带来的影响。具体的乐器是吉他与钢琴。  

#吉他
###吉他的音调与什么有关、振动的弦如何发声
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/吉他结构图.png)

如图，吉他弦跨过桥bridge，桥bridge与soundboard音板固连，如果桥被弦带动而动，音板也会获得速度，这个速度我们认为与弦作用于bridge的力成正比。另外，音板运动导致的声压与音板的运动速度成正比。由这两个成比例关系，我们可知声压与弦作用于桥的力成比例。这个力是垂直于音板的分力。
设弦中张力为T，则作用于桥的力为：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/桥力表达式.png)

其中y对x的偏导取在与桥接触的点处。
如果我们能给出波动方程的解，计算出桥接触处的y对x偏导，那么得到了与之成比例的声压的P-t关系，通过傅里叶展开，分析它有哪些振动成分，也就清楚了所发声音的音调（频率）成分。

###模拟吉他弦的振动，解出波动方程
两端固定弦的波动方程的解析解为：  

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/两端固定弦的解析解.png)

吉他模型中，波动方程边界条件为两端固定，初始条件为各点初速度为0，人手拉弦一点，使弦成两条线段相交于提起点，初始波形如图：  

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/提起的吉他弦初始波形.png)  

（我们设提起的最高点对应横坐标为βL，之后将研究这个提起点位置的的影响）

有了对解析解的认识，在计算方法计算之前，我们可以得知在吉他模型的初始条件下，系数Cn为0.

为了用计算方法解出波动方程，我们对波动方程中的坐标x、t分割，推导出它的等价方程，过程如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/波动方程近似表示.png)

以上式为基础，可以写出求波动方程的计算解的程序，并如前一部分所说，为了研究声调我们需要将桥所受作用力进行傅里叶展开，来看它个频率成分的振幅大小，这需要用到快速傅里叶变换的手段。我们将课本P358，figure11.2给出的条件写入程序进行模拟。弦长L=0.65m，提起点为βL=L/5，β=1/5，c为320m/s，绳中张力149N，r=1，dx=0.65mm，经历10000个dt。

[代码在此](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20波形图、桥上力频谱.py)

可以得到若干个时刻的波形图如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1题，波形图.png)

桥点作用力的F-t图像：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20F-t.png)


桥点的作用力频谱如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20β%3D0.2的频谱.png)

从解析解我们得知，基频f1=c/2L=247Hz，我们的频谱图显示，作用于桥点的力的基频成分的振幅最大，相应的声音中频率为基频f1的声音强度是最大的，之后三个2f1、3f1、4f1逐个递减。在5f1处，强度为0，之后6f1、7f1…………强度很小，但10f1,15f1成分的振幅还是明显在0附近。
###为什么上述条件下的5f1的振动成分振幅为0？

我们做出初始弦的提起点不同的一些弦振动的桥点作用力的频谱图，在a=wave()括号中依次输入β=1/10，β=1/20，β=1/25，运行程序，所得频谱图如下：

提起点为βL，β=1/10的频谱：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20β%3D0.1的频谱.png)

提起点为βL，β=1/20的频谱：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20β%3D0.05的频谱.png)

提起点为βL，β=1/25的频谱：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20β%3D0.04的频谱.png)

通过频谱图我们发现，f为n倍基频的成分的振幅都是0.解析解中，f为n倍基频的成分的振幅：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/β成分消失的解析.png)

这解释了为什么提起点为βL的弦振动中桥点作用力的n=1/β的成分振幅为0。

###不连续的初始条件导致的不连续解

我们在以上的计算模拟中，初始条件用的是提起的是一个点，但是当用手拨动吉他弦时，我们并不是拉弦的某一点，甚至无法近似为只拨动弦的一个点。这不光滑的初始条件会使解不光滑。我们把程序中的L等分为1000份改为100份，再运行程序观察波形图。

改为划分L为100份，波形图：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.1%20M%3D100的锯齿波形图.png)

这锯齿状并不是来源于L的分割更粗，而是来源于不光滑的初始条件。
我们可以改善初始条件，即初始波形图，来获得更光滑、更合理的解。
首先我们假设我们提起的不是一个点，而是一小段线段，即如图初始条件：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20提起一个小线段的初始波形.png)

写入程序，运行。[代码在此](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20提起一段线段波形图.py)

运行后：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20提起一个小线段的波形图.png)

与最初的提起一个点的弦的波形图对比，发现光滑程度略微有些改善，但还不够好。

我们假设用一个圆柱来模拟手指伸入弦中，即初始波形如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20圆形初始条件的初始波形.png)


写入程序，运行。[代码在此](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20圆形初始条件波形图.py)

运行后：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.6%20圆形初始条件的波形图.png)

我们发现，即使将弦L划分100份不够精细，但是解是十分光滑的。并且圆柱伸入弦是十分接近圆柱形手指拨动弦的。
当然应该指出，在我们的代码中，圆取的大小、位置都十分特殊，它的半径为弦的最高点纵坐标，即圆心落在x轴上。这样的话在求解圆柱伸入弦中的切点问题时会很方便，通过几何关系就可以求出切点坐标。虽然程序中缺失一点一般性，但是我们能从这特殊的拨动吉他弦位置的解知道，一个合理的初始条件下解的光滑性很好。

#钢琴
###钢琴的音调与什么有关、振动的弦如何发声
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/钢琴结构示意图.png)

钢琴的原理比吉他更复杂，它也是靠弦振动来作用于桥点，桥点固连音板，音板振动，引起空气压缩产生声波。它的复杂在于，弦受到一个锤子的打击，二者碰撞过程中弦获得一定的位移与速度，之后二者分离，弦做满足两端固定波动方程的运动。
换言之，如果取锤、弦碰撞结束时刻为初始时刻，初始条件为一定的初始波形、一定的速度分布。我们也可以取初始时刻为碰撞开始的时刻，对碰撞机理、碰撞过程做一定简化，来求解弦的振动。这时严格来说弦满足的不是波动方程了，因为它收到了一定的外力，我们不能得到解析解了，只能把这种碰撞简化体现在计算方法中。

与吉他相同，如果解出了弦的运动解，可以表示出桥点的力，利用快速傅里叶变换将此力做傅里叶展开，可以分析声调的频率各成分的强度。

###模拟吉他弦的振动，对锤与弦的碰撞简化处理

如前一部分所述，我们要求解弦与锤的碰撞过程中弦与锤的运动。锤子的简化如下，由一个物块与轻弹簧相连构成：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/锤示意图.png)

根据课本介绍，这个轻弹簧在它两端的作用力![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/弹簧作用力.png) z为弹簧压缩量。

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/钢琴弦碰撞过程方程.png)

要注意这方程适用于碰撞过程，也就是y(i)-Y< s时。在计算程序中，我们取三个相邻弦分割元参与碰撞，即满足上述方程，受到的力Fh也分配到三个质元上，比例为中间一个受到0.5Fh，两边的受到0.25Fh。
与吉他模一样，将以上方程进行近似处理，如下：

![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/钢琴弦碰撞方程的计算表示.png)

以此为基础，我们可以写出计算程序。我们按照课本P366，figure11.6的条件进行计算，锤子初速度vh0=0.5m/s，f=262Hz，L=0.62m，其中需要另外赋值质量密度μ=0.01kg/m。L分割为1000等份。

[代码在此：figure11.6 钢琴的Fh](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20钢琴的Fh.py)

[代码在此：figure11.6 接触点的y-t](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20接触点的y-t.py)

[代码在此：figure11.6 桥点作用力的频谱](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20F的频谱.py)

依次运行结果如下：
碰撞作用力Fh-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20钢琴的Fh.png)

碰撞接触中心的弦点的y-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20接触中心点的Y-t.png)

桥点作用力F的频谱：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.6%20力的频谱.png)

观察三个运行结果，可以发现碰撞时间为2.75ms左右，可见碰撞过程很短促。在碰撞结束以后，整个弦又成了两端固定的自由振动弦，做周期运动。桥点作用力的频谱可以反映声调的各频率成分的强度大小，可见此时基频262Hz的强度最大，其他频率的成分强度很小。

###如何弹出不同的音调、频率成分？
对于同一根琴弦，同一个锤子，如果我们改变锤子的初速度，桥点作用力的频谱成分比例也会发生改变，而不是各频率成分的强度比例不变、变化相同的倍数。这与我们的直观感受有点相悖。改变上一部分的程序的初速度，即a=(vh0=4),运行程序，得到如下结果：

碰撞作用力Fh-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.7%20钢琴的Fh.png)

碰撞接触中心的弦点的y-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.7%20接触中心点的y-t.png)

桥点作用力F的频谱：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/figure11.7%20力的频谱.png)

果然，与我们的直觉不同，频谱各成分的强度比改变了，此时f1和2f1的强度比比之前小了。这说明改变锤子初速度可以实现改变音调的频谱成分。这种现象的根源在于Kz^3这种形式的力，即非线性弹性力。这现象在各类乐器中十分常见。当然，从两个不同初速度锤子引起的声调频谱图可以看出，速度大的频谱的总强度要更大。这意味着，声音强度不同，音调成分不同。

###改变弦线，改变锤子的弹性性质，来改变频谱、改变音调
钢琴有许多根弦，不同的弦在我们的方程中，意味着某些系数的改变，如张力FT、质量密度μ、弦长L、弹性系数K、锤子质量m等等，他们与c=(T/μ)^0.5、基频f=c/2L等等密切相关。
我们按照课本练习题11.8给出的条件，重新运行之前的程序，即在运行时：a=wave(vh0=0.5,L=1.06，T=349，K=60000000000，m=0.0043，F=65)
a=wave(vh0=4,L=1.06，T=349，K=60000000000，m=0.0043，F=65)

得到如下的结果：

锤速度为vh0=0.5m/s：

碰撞作用力Fh-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.6中C调%20低2%20钢琴的Fh.png)

碰撞接触中心的弦点的y-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.6中C调%20低2%20接触中心点y-t.png)

桥点作用力F的频谱：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.6中C调%20低2%20力的频谱.png)

锤速度为vh0=4m/s：

碰撞作用力Fh-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.7中C调%20低2%20钢琴的Fh.png)

碰撞接触中心的弦点的y-t：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.7中C调%20低2%20接触中心点y-t.png)

桥点作用力F的频谱：
![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/11.8%20figure11.7中C调%20低2%20力的频谱.png)

可见此时频谱成分相较之前那根弦、那个锤子发生了显著改变，强度最明显的不是基频成分了，而是二倍基频成分。
