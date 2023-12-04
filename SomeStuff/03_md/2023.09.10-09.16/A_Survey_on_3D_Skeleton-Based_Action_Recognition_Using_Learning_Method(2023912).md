[https://arxiv.org/abs/2002.05907](https://arxiv.org/abs/2002.05907)

[Submitted on 14 Feb 2020]

题目：A Survey on 3D Skeleton-Based Action Recognition Using Learning Method

**本文研究包含了四个主要贡献：**

- 本文详细而清晰地介绍了3D骨架序列数据的优势以及三种深度模型的特点，并阐述了基于3D骨架的深度学习方法在动作识别中的一般流程。
- 对于每种深度模型，从数据驱动的角度介绍了几种基于骨架数据的最新算法，包括空间-时间建模、骨架数据表示以及共现特征学习的方法，这也是需要解决的经典问题。
- 本文讨论了最新的挑战性数据集NTU-RGB+D 120以及几种排名靠前的方法。随后，探讨了未来的研究方向。
- 第一项研究综合考虑了基于RNN、基于CNN和基于GCN的各种深度模型，用于3D骨骼动作识别。

---

![16944799980611694479997757.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16944799980611694479997757.png)

这篇综述文章总结了基于三维骨骼的动作识别研究。全文可以概括为以下几点:

### 引言

- 动作识别任务的重要性
- 骨骼数据的优势
- 基于深度学习的动作识别一般流程

![16944811880621694481187468.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16944811880621694481187468.png)

### 主流动作识别技术

#### 基于循环神经网络(RNN)的方法

- 时空建模方法
  - two-stream RNN architecture
  - traversal method of a given skeleton sequence
  - attention RNN with a CNN model
- 网络结构设计
  - Shuai and Wanqing proposed a **<u>independently recurrent neural network</u>**, which could solve the problem of gradient exploding and vanishing, throuth which could make it possible and more robust to build a longer and deeper RNN for high sematic feature learning.
- 数据驱动方法
  - add global contex-aware attention to LSTM networks； 为LSTM添加全局上下文感知的注意力机制，可以选择性地关注骨骼序列中的信息性关节。
  - Lee等人首先将骨骼转换到另一个坐标系统中以增强对尺度、旋转和平移的稳健性，然后从转换后的数据中提取显著的动作特征。
  
  ![16945093799391694509379484.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16945093799391694509379484.png)

#### 基于卷积神经网络(CNN)的方法

为了满足卷积神经网络的输入要求，3D骨骼序列数据被转换为伪图像。然而，同时具有空间和时间信息的适当表示通常并不容易，因此许多研究人员将骨骼关节编码为多个2D伪图像，然后将其输入到卷积神经网络中学习有用的特征。

- 骨骼序列表示
  - Wang提出了联合轨迹图（JTM），通过颜色编码将关节轨迹的空间配置和动态表示为三个纹理图像。缺点：在映射过程中还会丢失重要信息。
- 时空信息建模
  - Bo和Mingyi采用了一种平移尺度不变的图像映射策略，首先根据人体的物理结构将每帧中的人体骨骼关节分为五个主要部分，然后将这些部分映射到2D形式。这种方法使得骨骼图像包含了时间信息和空间信息。缺点：将骨骼关节视为孤立点。
  - Yanshan和Rongjie 提出了基于几何代数的形状-运动表示，强调了关节和骨骼的重要性，充分利用了骨骼序列提供的信息。
  - Carlos和Jessica 还提出了一种基于动作信息的新表示方法，名为SkeleMotion，通过明确计算骨骼关节的幅度和方向值来编码时间动态。
    
    ![16945093549391694509354850.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16945093549391694509354850.png)
- 共现特征学习
  - Chao and Qiaoyong 利用了一个端到端的框架来学习共现特征，采用了分层方法，逐渐聚合不同层次的上下文信息。首先，点级信息独立地编码，然后它们被组装成时间域和空间域中的语义表示。

基于CNN的技术还存在一些其他问题，例如模型的大小和速度 ，CNN的架构（两流或三流 ），遮挡、视角变化等 。因此，基于CNN的骨架行为识别仍然是一个待研究者深入探索的开放问题。

#### 基于图卷积网络(GCN)的方法

- 骨骼图构建
  - Sijie和Yuanjun 首先提出了一种新颖的基于骨架的动作识别模型， 即时空图卷积网络（ST-GCN），该模型首次利用关节作为图节点和人体结构和时间中的自然连接性构建了一个时空图。
- 特征提取和关系建模
  - Maosen和Siheng 提出了一种叫作动作结构图卷积网络（AS-GCN）的模型，该模型不仅可以识别人的动作，还可以使用多任务学习策略输出下一个可能的姿态预测。本工作中构建的图能够通过叫作行动链接和结构链接的两个模块捕捉关节之间更丰富的依赖关系。

### 数据集NTU-RGB+D、新版数据集NTU-RGB+D 120

- **排名前十方法对比**

**NTU-RGB+D dataset：**

|Rank|Paper|Year|Accuracy(C-V)|Accuracy(C-Subject)|Method|
|--|:--|:--:|:--:|:--:|:--|
|1|Shi et al. [63]|2019|96.1|89.9|Directed Graph Neural Networks|
|2|Shi et al. [64]|2018|95.1|88.5|Two stream adaptive GCN|
|3|Zhang et al. [65]|2018|95.0|89.2|LSTM based RNN|
|4|Si et al. [66]|2019|95.0|89.2|AGC-LSTM(Joints&Part)|
|5|Hu et al. [67]|2018|94.9|89.1|Non-local S-T + Frequency Attention|
|6|Li et al. [68]|2019|94.2|86.8|Graph Convolutional Networks|
|7|Liang et al. [69]|2019|93.7|88.6|3S-CNN+Multi-Task Ensemble Learning|
|8|Song et al. [70]|2019|93.5|85.9|Richly Activated GCN|
|9|Zhang et al. [71]|2019|93.4|86.6|Semantics Guided GCN|
|10|Xie et al. [46]|2018|93.2|82.7|RNN+CNN+Attention|

**NTU-RGB+D 120 dataset：**

|Rank|Paper|Year|Accuracy(C-Subject)|Accuracy(C-Setting)|Method|
|--|--|--|:--:|:--:|--|
|1|Caetano et al. [72]|2019|67.9|62.8|Tree Structure + CNN|
|2|Caetano et al. [58]|2019|67.7|66.9|SkeleMotion|
|3|Liu et al. [73]|2018|64.6|66.9|Body Pose Evolution Map|
|4|Ke et al. [74]|2018|62.2|61.8|Multi-Task CNN with RotClips|
|5|Liu et al. [75]|2017|61.2|63.3|Two-Stream Attention LSTM|
|6|Liu et al. [2]|2017|60.3|63.2|Skeleton Visualization (Single Stream)|
|7|Jun et al. [76]|2019|59.9|62.4|Online+Dilated CNN|
|8|Ke et al. [77]|2017|58.4|57.9|Multi-Task Learning CNN|
|9|Jun et al. [51]|2017|58.3|59.2|Global Context-Aware Attention LSTM|
|10|Jun et al. [45]|2016|55.7|57.9|Spatio-Temporal LSTM|

### 结论与展望

- 三种深度学习方法对比
  - 本文的研究是第一项以数据驱动方式深入了解基于深度学习的方法，涵盖了基于循环神经网络（RNN）、基于卷积神经网络（CNN）和基于图卷积神经网络（GCN）的最新算法。特别是在RNN和CNN方法中，通过骨骼数据的表示和网络架构的详细设计，解决了时空信息的问题。在GCN方法中，最重要的是如何充分利用关节和骨骼之间的信息和相关性。
- 目前问题和未来方向
  - 长期动作识别、更高效的3D骨骼序列表示、实时操作仍然是开放的问题，而且无监督或弱监督策略以及零样本学习可能也会引领未来。
