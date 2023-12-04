[https://arxiv.org/pdf/1901.00596.pdf](https://arxiv.org/pdf/1901.00596.pdf)

题目：[ A Comprehensive Survey on Graph Neural Networks](https://ieeexplore.ieee.org/document/9046288)

期刊： IEEE Transactions on Neural Networks and learning systems(TNNLS)

![16942279072711694227906491.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16942279072711694227906491.png)

# 图神经网络综述

## 1. 综述结构和贡献

### 1.1 提出新的GNN分类法

### 1.2 对每类GNN进行全面介绍

### 1.3 收集丰富资源

- 数据集
- 开源代码

### 1.4 探讨GNN理论基础

- 分析现有方法局限性
- 提出四个未来研究方向
  - 模型深度
  - 可扩展性
  - 异构性
  - 动态性

***

## 2. 背景知识

### 2.1 GNN发展历史

### 2.2 GNN与网络嵌入、图核方法关系 

### 2.3 定义图表示和相关概念

## 3. GNN分类和框架

### 3.1 四类GNN概述

- 循环图神经网络(RecGNN)
- 卷积图神经网络(ConvGNN)  
- 图自编码器(GAE)
- 时空图神经网络(STGNN)
  
  ##### 图神经网络（GNNs）的分类和代表性出版物:

|Category|Publications|
|:--|:--|
|Recurrent Graph Neural Networks (RecGNNs)|                                     [15], [16], [17], [18]|
|Convolutional Graph Neural Networks (ConvGNNs)|Spectral methods：     [19], [20], [21], [22], [23], [40], [41]<br/>------------------------------------------------------------<br/>Spatial methods:          [24], [25], [26], [27], [42], [43], [44]<br/>								     [45], [46], [47], [48], [49], [50], [51]<br/>                                     [52], [53], [54], [55], [56], [57], [58]|
|Graph Autoencoders (GAEs)|Network Embedding：[59], [60], [61], [62], [63], [64] <br/>----------------------------------------------------------<br/>Graph Generation：     [65], [66], [67], [68], [69], [70]|
|Spatial-temporal Graph Neural Networks (STGNNs)|                                      [71], [72], [73], [74], [75], [76], [77]|

<br/>

### 3.2 GNN任务类型

- 节点级任务
- 边级任务  
- 图级任务

### 3.3 GNN训练框架

- 半监督学习
- 监督学习
- 无监督学习

## 4. 循环图神经网络

## 5. 卷积图神经网络

### 5.1 频谱方法

### 5.2 空间方法

## 6. 图自编码器

### 6.1 网络嵌入

### 6.2 图生成

## 7. 时空图神经网络

许多实际应用中的图是动态的，既在图结构上动态变化，又在图输入上动态变化。空时图神经网络(STGNNs)在捕捉图的动态性方面占据重要地位。该类方法旨在对动态节点输入进行建模，并假设连接节点之间存在相互依赖关系。例如，一个交通网络由放置在道路上的速度传感器组成，边的权重由传感器对之间的距离决定。由于一条道路的交通状况可能取决于其相邻道路的状况，因此在进行交通速度预测时必须考虑空间依赖关系。

STGNNs同时捕捉图的空间和时间依赖关系。STGNNs的任务可以是预测未来节点的值或标签，或者预测空时图的标签。STGNNs有两个方向，基于循环神经网络(RNN)的方法和基于卷积神经网络(CNN)的方法。

## 8. 应用

- 计算机视觉
- 自然语言处理
- 交通
- 推荐系统
- 化学
- 其他

## 9. 未来方向

- 模型深度
- 可扩展性
- 异构性
- 动态性

## 10. 总结

## 11. 附录

- 标准数据集

- 模型开源代码

 A Summary of Open-source Implementations Model Framework Github Link

|Model|Framework|Github Link|
|--|--|--|
|GGNN|torch|[github.com/yujiali/ggnn](https://github.com/yujiali/ggnn)|
|SSE|c|[github.com/Hanjun-Dai/steady-state-embedding](https://github.com/Hanjun-Dai/steady-state-embedding)|
|ChebNet|tensorflow|[github.com/mdeff/cnn-graph](https://github.com/mdeff/cnn-graph)|
|GCN|tensorflow|[github.com/tkipf/gcn](https://github.com/tkipf/gcn)|
|CayleyNet|tensorflow|[github.com/amoliu/CayleyNet](https://github.com/amoliu/CayleyNet)|
|DualGCN|theano|[github.com/ZhuangCY/DGCN](https://github.com/ZhuangCY/DGCN)|
|GraphSage|tensorflow|[github.com/williamleif/GraphSAGE](https://github.com/williamleif/GraphSAGE)|
|GAT|tensorflow|[github.com/PetarV-/GAT](https://github.com/PetarV-/GAT)|
|LGCN|tensorflow|[github.com/divelab/lgcn](https://github.com/divelab/lgcn)|
|PGC-DGCNN|pytorch|[github.com/dinhinfotech/PGC-DGCNN](https://github.com/dinhinfotech/PGC-DGCNN)|
|FastGCN|tensorflow|[github.com/matenure/FastGCN](https://github.com/matenure/FastGCN)|
|StoGCN|tensorflow|[github.com/thu-ml/stochastic-gcn](https://github.com/thu-ml/stochastic-gcn)|
|DGCNN|torch|[github.com/muhanzhang/DGCNN](https://github.com/muhanzhang/DGCNN)|
|DiffPool|pytorch|[github.com/RexYing/diffpool](https://github.com/RexYing/diffpool)|
|DGI|pytorch|[github.com/PetarV-/DGI](https://github.com/PetarV-/DGI)|
|GIN|pytorch|[github.com/weihua916/powerful-gnns](https://github.com/weihua916/powerful-gnns)|
|Cluster-GCN|pytorch|[github.com/benedekrozemberczki/ClusterGCN](https://github.com/benedekrozemberczki/ClusterGCN)|
|DNGR|matlab|[github.com/ShelsonCao/DNGR](https://github.com/ShelsonCao/DNGR)|
|SDNE|tensorflow|[github.com/suanrong/SDNE](https://github.com/suanrong/SDNE)|
|GAE|tensorflow|[github.com/limaosen0/Variational-Graph-Auto-Encoders](https://github.com/limaosen0/Variational-Graph-Auto-Encoders)|
|ARVGA|tensorflow|[github.com/Ruiqi-Hu/ARGA](https://github.com/Ruiqi-Hu/ARGA)|
|DRNE|tensorflow|[github.com/tadpole/DRNE](https://github.com/tadpole/DRNE)|
|GraphRNN|tensorflow|[github.com/snap-stanford/GraphRNN](https://github.com/snap-stanford/GraphRNN)|
|MolGAN|tensorflow|[github.com/nicola-decao/MolGAN](https://github.com/nicola-decao/MolGAN)|
|NetGAN|tensorflow|[github.com/danielzuegner/netgan](https://github.com/danielzuegner/netgan)|
|GCRN|tensorflow|[github.com/youngjoo-epfl/gconvRNN](https://github.com/youngjoo-epfl/gconvRNN)|
|DCRNN|tensorflow|[github.com/liyaguang/DCRNN](https://github.com/liyaguang/DCRNN)|
|Structural RNN|theano|[github.com/asheshjain399/RNNexp](https://github.com/asheshjain399/RNNexp)|
|CGCN|tensorflow|[github.com/VeritasYin/STGCN-IJCAI-18](https://github.com/VeritasYin/STGCN-IJCAI-18)|
|ST-GCN|pytorch|[github.com/yysijie/st-gcn](https://github.com/yysijie/st-gcn)|
|GraphWaveNet|pytorch|[github.com/nnzhan/Graph-WaveNet](https://github.com/nnzhan/Graph-WaveNet)|
|ASTGCN|mxnet|[github.com/Davidham3/ASTGCN](https://github.com/Davidham3/ASTGCN)|

- 实验结果汇总

对五个常用数据集进行了节点分类的实验结果的报告。Cora、Citeseer和Pubmed通过分类准确度进行评估。PPI和Reddit通过微平均的F1值进行评估。

![16942524261751694252425650.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16942524261751694252425650.png)
