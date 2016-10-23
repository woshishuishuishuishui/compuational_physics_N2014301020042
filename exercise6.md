##问题2.10摘要：
  1.对给定点，给定初始速度，发炮打固定点，求出射角和轨迹。包括目标高于和低于炮。
  
  2.对给定点，求击中它的最小速度
  
##背景介绍：
  以欧拉法为基础解决这个问题。
  
##正文：
  相应理论和上一次作业一样。但是空气阻力要考虑风速影响，如课本三十四页式子所示
  
  
  
  1.对给定点，给定初始速度，发炮打固定点，求出射角和轨迹，代码(https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/作业2.10，给定目标和炮弹初速度，求出射角，目标高于炮)
  
  它可以实现：输入目标点坐标，输入炮的发射初速度，给出在1度精确范围内最优发射角，并作出轨迹图。但是还不能实现到达目标点后轨迹图停止，而是穿过目标后延伸。
  运行结果：
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/炮打定点运行.png)
 
  对于炮高于目标：代码
(https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/打定点炮，定点低于炮)
  
  它的作用和上面打高于炮的目标一样。
  运行结果：
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/定点低于炮的%20取负角运行.png)
  
  2.对给定点，求击中它的最小速度，代码
  (https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/打定点炮，最小速度)
  
  运行十几分钟没结果，所以无结果图。
  如果可以，可以把程序里的初速度的扫描都1到10000，只要炮弹实际速度能够达到10000m/s，那样更可能得到解。
  
##结论：
     如果可以，无论第一问还是第二问，扫描角度都可以选用range(900)，对应角度就是计数变量i/10之类。
     
     
     第一问求轨迹对于无解的情况没法处理
     
     
     第二问很大一部分输入给定点的情况下是能看出来无法操作的，但是感觉还可以继续改，如果有时间
     
     
     一个很大的问题是我的两幅展示结果图，都是穿过目标后继续前行的，所以很不好看，希望老师可以注意



##致谢：
     主要模仿上一次作业的程序
