##问题2.9摘要：
  计算有空气阻力的抛体运动轨迹，并考虑随海拔变化气体密度的改变（等温气体），并求出最大的射程。
##背景介绍：
  以欧拉法为基础解决这个问题。
##正文：
  如讲义所讲，
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016211418.png)
  
  
  在抛体运动中，写出欧拉法表示的牛顿定律和运动学公式
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016211433.png)
  
  另外，等温气体的密度随海拔变化公式
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016212104.png)
  
  1.计算某抛射角下的轨迹，程序如下：
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016210429.png)
  
  运行之后得到轨迹图：
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016210504.png)
  
  2.在第1.问基础上，计算最大射程，程序如下：
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016213611.png)
  
  运行之后得到结果如下：
  
  
  ![Alt text](https://github.com/woshishuishuishuishui/compuational_physics_N2014301020042/blob/master/QQ截图20161016213619.png)
  
  从程序内容可知，最后两个输出数字依次为最远射程抛射角和最远射程。
  
##结论：
     按照欧拉法可以做出有空气阻力、考虑空气密度随海拔变化情形下的抛体轨迹图，并大致找出最大射程的抛射角为46度（在我给的条件下），
     这和无阻力时最大射程抛射角为45度不同。

##致谢：
     张梓桐的程序、秦大粤的程序
     蔡浩的讲义
     

