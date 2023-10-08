# 实践

## 1. 基于DQN算法的无人机三维城市空间航线规划

### [**源码**](https://)

本文基于强化学习算法DQN实现离散3维城市空间环境下的智能航线规划，能根据无人机感知进行避障，并根据风速情况选择能耗较低的路线。

### 环境需求

python 3.7

pytorch(cuda)

### 模型简介

在x100 y100 z22的三维空间中，采用课程学习方式对无人机智能体进行训练，利用设置好的不同难度的课程对智能体进行梯度训练，能让智能体更快地获取决策经验。由于训练初期缺乏决策经验，需要随机选择行为对环境进行试探，本文设置随机试探周期为1000，周期内采用ε-贪心策略选择智能体行为，周期内贪心概率从1逐渐递减到0.01。1000周期后贪心概率保持在0.01。在一个周期的训练场景中随机生成15个无人机对象，当所有无人机进入终止状态（电量耗尽、坠毁、到达目标点、超过最大步长）后进入下一个周期的训练，当80%以上的无人机能够到达目标点时进入下一难度等级的训练。
经过13万周期、19小时的迭代训练，最终无人机智能体能够在难度10的环境中以较高的任务完成率安全到达目标点。

[![avatar](https://github.com/Chenjiangwen/ImageHostingService/blob/main/pic/1696648737923GIF_2023-10-7_11-18-01.gif)

### 项目说明 

DQN.py:(main函数 入口1)设置模型训练参数与城市环境参数，对DQN模型进行训练，输出Qlocal.pth与Qtarget.pth文件

watch_uav.py：(main函数 入口2)对训练好的决策模型进行测试，载入Qlocal.pth与Qtarget.pth文件，对无人机航迹规划过程进行可视化

<img src="https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696647878731%E8%88%AA%E8%BF%B9%E5%9B%BE.jpg" alt="1696647878731航迹图.jpg" style="zoom:50%;" />

env.py：设置env类，对城市环境进行描述，实现该环境中的所有UAV与传感器运行的仿真模拟

model.py：神经网络模型的定义

replay_buffer.py：经验池的定义

UAV.py：定义UAV类，对无人机的自身参数与行为进行描述

### 系统框架

![1696647893730DQN无人机航迹规划系统框架图.jpg](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696647893730DQN%E6%97%A0%E4%BA%BA%E6%9C%BA%E8%88%AA%E8%BF%B9%E8%A7%84%E5%88%92%E7%B3%BB%E7%BB%9F%E6%A1%86%E6%9E%B6%E5%9B%BE.jpg)

### 训练参数设置 

env.py:

```
  env.reset()  #对仿真环境中的房屋建筑集合、无人机集合、传感器集合进行随机生成，对训练环境进行初始化 
  
  #Set the simulation environment parameters
  env. __init__() #对仿真环境参数进行设置
```

DQN.py

```
  BATCH_SIZE = 128    #批量大小
  TAU = 0.005 
  gamma = 0.99   #折扣率
  LEARNING_RATE = 0.0004   #学习率
  TARGET_UPDATE = 10   #Q网络更新周期 
  num_episodes = 40000  #训练周期长度 
  print_every = 1  
  hidden_dim = 16 ## 64 ## 16 #隐藏层维数 
  min_eps = 0.01    #贪心概率
  max_eps_episode = 10   #最大贪心次数
  space_dim = 42 # n_spaces   状态空间维度
  action_dim = 27 # n_actions   动作空间维度
  threshold = 200    
```

UAV.py:

```
  UAV. __init__()  #对UAV的参数进行设置
```

### 无人机状态空间

UAV.py:

```
def state(self):
        dx=self.target[0]-self.x
        dy=self.target[1]-self.y
        dz=self.target[2]-self.z
        state_grid=    [self.x,self.y,self.z,dx,dy,dz,self.target[0],self.target[1],self.target[2],self.d_origin,self.step,self.distance,self.dir,self.p_crash,self.now_bt,self.cost]
        #更新临近栅格状态  Update adjacent grid state
        self.ob_space=[]
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    if i==0 and j==0 and k==0:
                        continue
                    if self.x+i<0 or self.x+i>=self.ev.len or self.y+j<0 or self.y+j>=self.ev.width or self.z+k<0 or self.z+k>=self.ev.h:
                        self.ob_space.append(1) 
                        state_grid.append(1)
                    else:
                        self.ob_space.append(self.ev.map[self.x+i,self.y+j,self.z+k])  #添加无人机临近各个栅格状态
                        state_grid.append(self.ev.map[self.x+i,self.y+j,self.z+k])
        return state_grid  #无人机状态向量
```

### 奖励函数设置

UAV.py:

无人机未到达终止状态（未到达终点、未坠毁、为超最大步长）

```
        #计算总奖励 
        r=r_climb+r_target+r_e-crash*self.p_crash   
```

无人机到达终止状态

```
        #终止状态判断
        if self.x<=0 or self.x>=self.ev.len-1 or self.y<=0 or self.y>=self.ev.width-1 or self.z<=0 or self.z>=self.ev.h-1 or self.ev.map[self.x,self.y,self.z]==1 or random.random()<self.p_crash:
            #发生碰撞，产生巨大惩罚
            return r-200,True,2
        if self.distance<=5:
            #到达目标点，给予大量奖励
            #self.ev.map[self.x,self.y,self.z]=0
            return r+200,True,1 
        if self.step>=self.d_origin+2*self.ev.h:
            #步数超过最差步长，给予惩罚
            return r-20,True,5
        if self.cost>self.bt:
            #电量耗尽，给予大量惩罚
            return r-20,True,3
```

***

***

## 2. EC-EN-674-Flight-Dynamics-Controls

### [Youtube](https://www.youtube.com/playlist?list=PLa79EwlpK4ZMsxfw_ab-9_kLygiABV4_z) 、[Book](https://drive.google.com/file/d/1I3dwUmBBzwT_A1MlBk2XRl4clZ7RHuOQ/view?usp=share_link) 、[源码](https://github.com/betaBison/EC-EN-674-Flight-Dynamics-Controls#installation)

# GPT-Academic Report

# 小型无人飞行器：理论与实践

![16966547117351696654711084.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16966547117351696654711084.png)

[Randy Beard](https://ece.byu.edu/directory/randy-beard), 
[Tim McLain](http://me.byu.edu/faculty/timmclain)

[普林斯顿大学出版社, 2012](http://press.princeton.edu/titles/9632.html)

[uavbook.pdf](https://drive.google.com/file/d/1I3dwUmBBzwT_A1MlBk2XRl4clZ7RHuOQ/view?usp=share_link)
  这个文件是一个正在进行中的工作。我们的打算是将这个文件成为这本书的第二版。但请注意，它还没有经过仔细的校对，我们会定期更新它。

## 课堂资料

以下课堂资料作为教师的资源包含在内。幻灯片紧密跟随着书内容。

|章节|PDF 幻灯片|Powerpoint|最后修改日期|
|--|--|--|--|
|第1章 - 引言|[chap1.pdf](https://drive.google.com/file/d/1BgkuPdWmuBEjq4wjoKsQt478QV647QF1/view?usp=sharing)|[chap1.pptx](https://docs.google.com/presentation/d/1069hP_fnDPJ7n0Yn9XWzCKAQD9GAdNtp/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年4月4日|
|第2章 - 坐标系|[chap2.pdf](https://drive.google.com/file/d/1BhIit4UtQw8ZNq0OuVPiBfhZjbGl2vAM/view?usp=sharing)|[chap2.pptx](https://docs.google.com/presentation/d/1BNcvtAA3_X0Et8xZiMOweiBR8-C3c6Ze/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2019年1月11日|
|第3章 - 运动学和动力学|[chap3.pdf](https://drive.google.com/file/d/1BOwGqoJ2WjiIUYDA8p77TGwV-Ttrd4hc/view?usp=sharing)|[chap3.pptx](https://docs.google.com/presentation/d/1BQsToiKlEMoJvgGMwaeCR74O0-SWdaxs/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年1月14日|
|第4章 - 力和力矩|[chap4.pdf](https://drive.google.com/file/d/1BjJuj8QLWV9E1FX6sHVHXIGaIizUaAJ5/view?usp=sharing)|[chap4.pptx](https://docs.google.com/presentation/d/1BQUoSlMYmB1Ni-PPFfyMbsSvPC_z26av/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年1月21日|
|第5章 - 线性设计模型|[chap5.pdf](https://drive.google.com/file/d/1BRS8PaOMrFdotGgb7oXOZloANh3fzUAo/view?usp=sharing)|[chap5.pptx](https://docs.google.com/presentation/d/1BfpnwWnK5A31pZdNu3rZ48Nu3AefLnfk/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年2月10日|
|第6章 - 自动驾驶设计|[chap6.pdf](https://drive.google.com/file/d/1BfLD2KDyalXuANrA14RC29EWIw3xF4fU/view?usp=sharing)|[chap6.pptx](https://docs.google.com/presentation/d/1BPBHWl0PiHGs43uYlk_qiRLSvKXZrx9G/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年2月10日|
|第7章 - 传感器|[chap7.pdf](https://drive.google.com/file/d/1BMceIPDGzBda9w5R5LrNnouabS8lQ9s_/view?usp=sharing)|[chap7.pptx](https://docs.google.com/presentation/d/1BRVcewET8_s5urj7NmXIDZUsrej0kvDw/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年2月14日|
|第8章 - 状态估计|[chap8.pdf](https://drive.google.com/file/d/1BSbH_F7KbP4tnSOwurSScwoVGsrTmHpg/view?usp=sharing)|[chap8.pptx](https://docs.google.com/presentation/d/1BSgBhzfr4RhCdZn-HX4v3pY1bCLp5YC0/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年2月27日|
|第9章 - 非线性设计模型|[chap9.pdf](https://drive.google.com/file/d/1BelIP25e4QFLps4Rr49jyzP1maox328C/view?usp=sharing)|[chap9.pptx](https://docs.google.com/presentation/d/1BiQW_uHnIt9JfBFo4hMPqclEEbza7HVL/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2014年11月4日|
|第10章 - 航点与轨迹跟踪|[chap10.pdf](https://drive.google.com/file/d/1BLu3HMqT8-OW1ys-xyoZup_wtSX_v3bq/view?usp=sharing)|[chap10.pptx](https://docs.google.com/presentation/d/1-ZHy0ZFqL6NHSczAFKX2qdaY6gI8CPBF/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年3月11日|
|第11章 - 路径管理器|[chap11.pdf](https://drive.google.com/file/d/1BhtShrqNmy14c7k_R0Ayn-kW8IyZ1Jc3/view?usp=sharing)|[chap11.pptx](https://docs.google.com/presentation/d/1BUhwTIXyWRpKR8hPGnqNi7Z8tHGEC3pY/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2022年3月21日|
|第12章 - 路径规划|[chap12.pdf](https://drive.google.com/open?id=1BYx4o9P_fJOLZX2myGs3UrlUqkvLZWEo&authuser=randy.beard%40gmail.com&usp=drive_fs)|[chap12.pptx](https://docs.google.com/presentation/d/1BaMLi2jQSZSfDlGhnDnIbq7AnoDtDMLv/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2017年4月3日|
|第13章 - 摄像头|[chap13.pdf](https://drive.google.com/file/d/1BZ2CogzLgJWudjRf7Mbldu7niqdTg9ss/view?usp=sharing)|[chap13.pptx](https://docs.google.com/presentation/d/1Bfw9UboxHPoOi0mAUc1srGIhUwQxW_fo/edit?usp=sharing&ouid=115325376918178448854&rtpof=true&sd=true)|2017年4月10日|

## 项目文件

本 GitHub 账户中的模板文件旨在帮助学生完成书中提到的项目。我们发现，如果学生使用这些文件开始项目，通常每章大约需要3小时的时间。完整的项目解决方案可根据请求提供给教师。我们恳请学生和教师不要在网上公开发布完整的项目解决方案。该项目提供了一个极好的学习体验，我们相信，任何亲自完成该项目的人将更好地为小型无人机的最先进技术做出贡献。

## 评论

- 书中给出的 Zagi 系数存在一些问题。我们建议您使用以下稍作修改的气象雷鸟飞机系数。[aerosonde.m](project/aerosonde.zip)
- 对于 Aerosonde 型号，请使用初始速度 Va = 35 m/s，并且半径为 250 米。
- 附加信息：Aerosonde 的重量实际上为 25 公斤。此外，巡航速度约为 Va = 35 m/s。

## 视频解决方案

- [YouTube 视频展示第2章的解决方案。](http://youtu.be/LgiHUznfP_4)
- [YouTube 视频展示第3章的解决方案。](http://youtu.be/KCoRO-G-VPg)
- [YouTube 视频展示第4章的解决方案。](http://youtu.be/jT5_ZDyNCTI)
- [YouTube 视频展示第5章的解决方案。](http://youtu.be/cyLi8WAbOWs)
- [YouTube 视频展示第6章的解决方案。](http://youtu.be/1CoF2rJHs4c)
- [估计结果的屏幕截图](project/chap8_results.zip)
- [YouTube 视频展示第10章的解决方案。](http://youtu.be/1NEssGinf_8)
- [YouTube 视频展示第11章的解决方案。](http://youtu.be/aGAdjbtSoso)
- [YouTube 视频展示第12章的解决方案。](http://youtu.be/bdYb45bpID4)

## 补充材料

我们计划不定期添加此页面的补充材料。我们也欢迎广大社区的贡献。如果您有意添加材料，请联系作者。

- **将 MavSim 改装为水下车辆模拟器**
  - [水下车辆模拟器](https://bitbucket.org/jfarrant/python_fixedwing_mavsim) - 作者 James Farrant
- **完整的纵向状态直接和间接卡尔曼滤波器**
书中介绍的卡尔曼滤波器旨在作为教程，并适用于处理处理能力非常有限的航空器。利用所有可用传感器来估计完整的状态是一种更好的方法。构建卡尔曼滤波器有两种方法：直接状态估计和间接状态估计。以下pdf文档和Simulink模型描述并实现了这两个滤波器的纵向完整状态。从模拟结果可以看出，这种方法比书中描述的方法要好得多。
  - [关于卡尔曼滤波的 UAVBook 补充内容（更新于2017年3月15日）](https://drive.google.com/file/d/1BykD4nuG7dsSfZqCPxO3Sx9zug8pLblt/view?usp=sharing)
  - [两个纵向状态的滤波器的仿真。](https://drive.google.com/file/d/1BxVKGlevI9ggi5BnS39tEGzBdzYbmboB/view?usp=sharing)
- **将物体投放到目标上**
  - [关于物体投放的 UAVBook 补充内容（更新于2017年10月25日）](https://drive.google.com/file/d/1Bp82Zcr4HBaqA-RObUA5uBVb0IWK651e/view?usp=sharing)
- **Dubins 飞机路径**
第11章讨论的Dubins路径假设MAV以恒定高度飞行。相关模型通常称为Dubins车模型。Dubins车模型可以扩展为包括高度的Dubins飞机模型。以下是有关相关Dubins飞机路径的解释：
  - Mark Owen，Randal W. Beard，Timothy W. McLain，“Implementing Dubins Airplane Paths on Fixed-wing UAVs”，Handbook of Unmanned Aerial Vehicles，编辑 Kimon P. Valavanis，George J. Vachtsevanos，Springer Verlag，第XII节，第68章，第1677-1702页，2014年。[预印版](https://drive.google.com/file/d/1BnRrIl1Kc7B674GPAv5yik1wrfCtStai/view?usp=sharing)
  - [实现Dubins飞机路径的Simulink文件](https://drive.google.com/file/d/1BzMnfsncxxOInVSVGpuugRqCjJBnSbmU/view?usp=sharing) 运行Simulink文件 mavsim_dubins.slx。
- **轨道跟踪的前馈项**
通过在滚转角上添加前馈项可以改善轨道跟踪。下面给出了在有风和无风情况下的描述：
  - [UAVBook关于轨道跟踪的前馈项补充](https://drive.google.com/file/d/1BsqTqIOWB1MreGTr2WjwCplAdMXZx00Z/view?usp=sharing)
- **Zagi飞机系数**
书中给出的Zagi飞机的空气动力系数来自[这篇论文](https://drive.google.com/file/d/1ByIODhuEInhebfH5-wlHbGHxyO3PA62H/view?usp=sharing)。
- **总能量控制**
与教科书中描述的纵向自动驾驶相对的选择是“总能量控制系统”，在[这里](https://drive.google.com/file/d/1Bor3cVtHWZI0TN-gkThKBMWIAqOc5DBr/view?usp=sharing)有介绍。
  
    总能量控制系统的非线性版本在以下论文中有描述。
  
    Matthew Argyle, Randal W. Beard, “Nonlinear Total Energy Control for the Longitudinal Dynamics of an Aircraft,” 美国控制会议论文集, 波士顿, 马萨诸塞州, 2016. [PDF](https://drive.google.com/file/d/1ByPPrxSrBNcFMv35rYhIezPpBGP_h_ic/view?usp=sharing)
  
    更详细的内容请参考
  
    Matthew E. Argyle, “Modeling and Control of a Tailsitter with a Ducted Fan,” 博士学位论文, 布里格姆杨百年大学, 2016.  [PDF](https://drive.google.com/file/d/1BvHV0jO2BvOaUOhbPEWAEJXuH0SVActa/view?usp=sharing)
  - 总能量控制方法的优点是它与空气动力模型无关。
- **多旋翼加速计和姿态控制**
加速计常用于估计多旋翼飞行器的横滚和俯仰角。由于多旋翼的气动特性与固定翼飞行器相当不同，所以书中描述的方法在多旋翼飞行器上不适用。关于从多旋翼飞行器的加速计中可以提取哪些数据的详细解释可以在以下论文中找到
  - Robert Leishman, John Macdonald, Randal W. Beard, Timothy W. McLain, “Quadrotors and Accelerometers: State Estimation with an Improved Dynamic Model,”  IEEE控制系统杂志, vol. 34, no. 1, p. 28-41, 2014年2月. [Preprint](https://drive.google.com/file/d/1BnmrOpGfBuE_MIGxtByq6Z2kwcaklSrM/view?usp=sharing).
- **卡尔曼滤波器**
关于卡尔曼滤波器的简介，请参阅Sebastian Thurn在Udacity人工智能课程中的[章节](https://www.udacity.com/course/viewer#!/c-cs373/l-48723604)。
- **天气和风数据**
[网站](http://www.usairnet.com/cgi-bin/launch/code.cgi?Submit=Go&sta=KPVU&state=UT)提供逐小时的风和天气信息
- **学生项目（样例）**
  
    **Nathan Madsen, 2014** [实现了着陆架和跑道相互作用模型，以及自动降落功能。](https://drive.google.com/file/d/1BrYEfp4L_d04B5dN3vPePlo74pE9GzDT/view?usp=sharing)
  
    **Andrew Hendrick, 2014** [使用AVL计算了Zagi和Pelican的空气动力系数](https://drive.google.com/file/d/1BvIKYjPv6ZW9iafDMKswumowi2FW8CLz/view?usp=sharing)
  
    **Michael Boren, 2014** 对RRT*算法的实现。[项目](https://drive.google.com/file/d/1Bq4HsfX3i6N6AED3UnU8ozhsMs2mUCcM/view?usp=sharing)
  
    **Michael Eyler, 2019** [LQR控制](https://github.com/eyler94/EE674LQR.git)
  
    **Brandon Forsgren, 2019**  [ROS/C++实现](https://github.com/b4sgren/mav_simulator)
  
    **Derek Knowles, 2019** [路径规划Voronoi图](https://github.com/betaBison/EC-EN-674-Flight-Dynamics-Controls/tree/master/project)
  
    **Easton Potokar, 2022** [应用于水下航行器](https://github.com/contagon/AUVControl)
  
    **Mason Peterson, 2022** [四旋翼平面轨迹跟踪器](https://github.com/mbpeterson70/quadplane_project)
  
   <!-- BROKEN LINK **Dan Richards, 2022** [多章节单元测试](https://github.com/dcrich/MAV-Unit-Tests) -->
  
    **John Morrell, 2022** [特征结构分配](https://github.com/Tarnarmour/FlightDynamics_Eigenstructure/blob/main/README.md)
  
  <br/>
  
![ed45d42889c543fc7fc446ef3947111f.gif](https://github.com/Chenjiangwen/ImageHostingService/blob/main/pic/1696727730936ed45d42889c543fc7fc446ef3947111f.gif)
  
  ***
  
  ***
  
  ## 3. HIT-UAV：一种用于基于无人机的目标检测的高空红外热数据集
  
  ## 简介
  
  HIT-UAV包含来自不同场景（学校、停车场、道路、操场等）的无人机捕获的43470帧中提取的2898个红外热图像，涵盖了广泛的内容，包括对象（人、自行车、汽车、其他车辆）、飞行高度数据（从60到130米）、相机视角数据（从30到90度）和日光强度（白天和夜晚）。
  
  ## 标注
  
  HIT-UAV提供了两种边界框类型，即标准和旋转。

旋转标注可以减少边界框的重叠，提高检测算法的性能。

- 标准边界框记录格式：$[xc, yc, w, h]$。
- 旋转边界框记录格式：$[xc, yc, w, h, \theta]$，其中$\theta$表示与标准边界框的水平方向的旋转角度。
  
  ![1696655200789fig_bbox.jpg](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696655200789fig_bbox.jpg)
  
  对于每种标注方法，我们提供了XML和JSON标签文件，以帮助用户利用HIT-UAV：
- *normal_xml*文件夹：使用XML文件记录标准边界框。
- *normal_json*文件夹：使用JSON文件记录标准边界框。
- *rotate_xml*文件夹：使用XML文件记录旋转边界框。
- *rotate_json*文件夹：使用JSON文件记录旋转边界框。
  
  ## 样本图像
  
  使用YOLOv4进行检测的示例图像。
  
  ![1696655202740fig_sample_result.jpg](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696655202740fig_sample_result.jpg)
  
  ## 论文
  
  https://doi.org/10.1038/s41597-023-02066-6
  
  ## 引用

```
Jiashun Suo, Tianyi Wang, Xingzhou Zhang, Haiyang Chen, Wei Zhou和Weisong Shi。HIT-UAV：一种用于基于无人机的目标检测的高空红外热数据集。Scientific Data 10, 227 (2023)。
```

  或

```
@article{suo2022hit,  
    title       = {HIT-UAV: A high-altitude infrared thermal dataset for Unmanned Aerial Vehicle-based object detection},  
    author      = {Suo, Jiashun and Wang, Tianyi and Zhang, Xingzhou and Chen, Haiyang and Zhou, Wei and Shi, Weisong},  
    journal     = {Scientific Data},  
    volume      = {10},
    pages       = {227},
    year        = {2023},
    publisher   = {Nature Publishing Group UK London}
}
```

## 4. 旋转框检测

![1696728242917detection.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696728242917detection.png) ![1696728456982train_batch6.jpg](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696728456982train_batch6.jpg)

![1696728541918results.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696728541918results.png)

### 有问题反馈

在使用中有任何问题，建议先按照[install.md](./docs/install.md)检查环境依赖项，再按照[GetStart.md](./docs/GetStart.md)检查使用流程是否正确，善用搜索引擎和github中的issue搜索框，可以极大程度上节省你的时间。

若遇到的是新问题，可以用以下联系方式跟我交流，为了提高沟通效率，请尽可能地提供相关信息以便我复现该问题。

- 知乎（@[略略略](https://www.zhihu.com/people/lue-lue-lue-3-92-86)）
- 代码问题提issues,其他问题请知乎上联系

## 关于作者

```javascript
  Name  : "胡凯旋"
  describe myself："咸鱼一枚"
```

***

## 5. YOLOV7-OBB：You Only Look Once OBB旋转目标检测模型在pytorch当中的实现

## YOLOV7-OBB：You Only Look Once OBB旋转目标检测模型在pytorch当中的实现

---

## 目录

1. [仓库更新 Top News](#仓库更新)
2. [相关仓库 Related code](#相关仓库)
3. [性能情况 Performance](#性能情况)
4. [所需环境 Environment](#所需环境)
5. [文件下载 Download](#文件下载)
6. [训练步骤 How2train](#训练步骤)
7. [预测步骤 How2predict](#预测步骤)
8. [评估步骤 How2eval](#评估步骤)
9. [参考资料 Reference](#Reference)

## Top News

**`2023-02`**:**仓库创建，支持step、cos学习率下降法、支持adam、sgd优化器选择、支持学习率根据batch_size自适应调整、新增图片裁剪、支持多GPU训练、支持各个种类目标数量计算、支持heatmap、支持EMA。**  

## 相关仓库

|目标检测模型|路径|
|:--|:--|
|YoloV7-OBB|https://github.com/Egrt/yolov7-obb|
|YoloV7-Tiny-OBB|https://github.com/Egrt/yolov7-tiny-obb|

## 性能情况

|训练数据集|权值文件名称|测试数据集|输入图片大小|mAP 0.5|
|:--:|:--:|:--:|:--:|:--:|
|SSDD|[yolov7_obb_ssdd.pth](https://github.com/Egrt/yolov7-obb/releases/download/V1.0.0/yolov7_obb_ssdd.pth)|SSDD-Val|640x640|95.22|

### 预测结果展示

![1696728745917test.jpg](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/1696728745917test.jpg)

## 所需环境

torch=1.10.1
torchvision=0.11.2
为了使用amp混合精度，推荐使用torch1.7.1以上的版本。

## 文件下载

SSDD数据集下载地址如下，里面已经包括了训练集、测试集、验证集（与测试集一样），无需再次划分：  
链接: https://pan.baidu.com/s/1Lpg28ZvMSgNXq00abHMZ5Q
提取码: 2021

## 训练步骤

### a、训练VOC07+12数据集

1. 数据集的准备   
**本文使用VOC格式进行训练，训练前需要下载好VOC07+12的数据集，解压后放在根目录**  
2. 数据集的处理   
修改voc_annotation.py里面的annotation_mode=2，运行voc_annotation.py生成根目录下的2007_train.txt和2007_val.txt。   
生成的数据集格式为image_path, x1, y1, x2, y2, x3, y3, x4, y4(polygon), class。 
3. 开始网络训练   
train.py的默认参数用于训练VOC数据集，直接运行train.py即可开始训练。   
4. 训练结果预测   
训练结果预测需要用到两个文件，分别是yolo.py和predict.py。我们首先需要去yolo.py里面修改model_path以及classes_path，这两个参数必须要修改。   
**model_path指向训练好的权值文件，在logs文件夹里。   
classes_path指向检测类别所对应的txt。**   
完成修改后就可以运行predict.py进行检测了。运行后输入图片路径即可检测。

### b、训练自己的数据集

1. 数据集的准备  
**本文使用VOC格式进行训练，训练前需要自己制作好数据集，**    
训练前将标签文件放在VOCdevkit文件夹下的VOC2007文件夹下的Annotation中。   
训练前将图片文件放在VOCdevkit文件夹下的VOC2007文件夹下的JPEGImages中。   
2. 数据集的处理  
在完成数据集的摆放之后，我们需要利用voc_annotation.py获得训练用的2007_train.txt和2007_val.txt。   
修改voc_annotation.py里面的参数。第一次训练可以仅修改classes_path，classes_path用于指向检测类别所对应的txt。   
训练自己的数据集时，可以自己建立一个cls_classes.txt，里面写自己所需要区分的类别。   
model_data/cls_classes.txt文件内容为：

```python
cat
dog
...
```

修改voc_annotation.py中的classes_path，使其对应cls_classes.txt，并运行voc_annotation.py。  

3. 开始网络训练  
**训练的参数较多，均在train.py中，大家可以在下载库后仔细看注释，其中最重要的部分依然是train.py里的classes_path。**  
**classes_path用于指向检测类别所对应的txt，这个txt和voc_annotation.py里面的txt一样！训练自己的数据集必须要修改！**  
修改完classes_path后就可以运行train.py开始训练了，在训练多个epoch后，权值会生成在logs文件夹中。  
4. 训练结果预测  
训练结果预测需要用到两个文件，分别是yolo.py和predict.py。在yolo.py里面修改model_path以及classes_path。  
**model_path指向训练好的权值文件，在logs文件夹里。  
classes_path指向检测类别所对应的txt。**  
完成修改后就可以运行predict.py进行检测了。运行后输入图片路径即可检测。

## 预测步骤

### a、使用预训练权重

1. 下载完库后解压，在百度网盘下载权值，放入model_data，运行predict.py，输入

```python
img/street.jpg
```

2. 在predict.py里面进行设置可以进行fps测试和video视频检测。

### b、使用自己训练的权重

1. 按照训练步骤训练。  
2. 在yolo.py文件里面，在如下部分修改model_path和classes_path使其对应训练好的文件；**model_path对应logs文件夹下面的权值文件，classes_path是model_path对应分的类**。
3. 运行predict.py，输入

```python
img/street.jpg
```

4. 在predict.py里面进行设置可以进行fps测试和video视频检测。

## 评估步骤 

### a、评估VOC07+12的测试集

1. 本文使用VOC格式进行评估。VOC07+12已经划分好了测试集，无需利用voc_annotation.py生成ImageSets文件夹下的txt。
2. 在yolo.py里面修改model_path以及classes_path。**model_path指向训练好的权值文件，在logs文件夹里。classes_path指向检测类别所对应的txt。**  
3. 运行get_map.py即可获得评估结果，评估结果会保存在map_out文件夹中。

### b、评估自己的数据集

1. 本文使用VOC格式进行评估。  
2. 如果在训练前已经运行过voc_annotation.py文件，代码会自动将数据集划分成训练集、验证集和测试集。如果想要修改测试集的比例，可以修改voc_annotation.py文件下的trainval_percent。trainval_percent用于指定(训练集+验证集)与测试集的比例，默认情况下 (训练集+验证集):测试集 = 9:1。train_percent用于指定(训练集+验证集)中训练集与验证集的比例，默认情况下 训练集:验证集 = 9:1。
3. 利用voc_annotation.py划分测试集后，前往get_map.py文件修改classes_path，classes_path用于指向检测类别所对应的txt，这个txt和训练时的txt一样。评估自己的数据集必须要修改。
4. 在yolo.py里面修改model_path以及classes_path。**model_path指向训练好的权值文件，在logs文件夹里。classes_path指向检测类别所对应的txt。**  
5. 运行get_map.py即可获得评估结果，评估结果会保存在map_out文件夹中。

## Reference

https://github.com/WongKinYiu/yolov7

https://github.com/bubbliiiing/yolov7-pytorch
