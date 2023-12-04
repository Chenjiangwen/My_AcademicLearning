# GPT-Academic Report

# GNN 论文列表

我们选择了100篇最具影响力的GNN论文和100篇最新的SOTA GNN论文，涵盖了10个不同的主题。

## [目录](#目录)

<table>
<tr><td><a href="#gnn-architecture">1. GNN架构</a></td></tr> 
<tr><td><a href="#large-scale-training">2. 大规模训练</a></td></tr>
<tr><td><a href="#self-supervised-learning-and-pre-training">3. 自监督学习和预训练</a></td></tr>
<tr><td><a href="#oversmoothing-and-deep-gnns">4. 过平滑和深度GNN</a></td></tr>
<tr><td><a href="#graph-robustness">5. 图的鲁棒性</a></td></tr>
<tr><td><a href="#explainability">6. 可解释性</a></td></tr>
<tr><td><a href="#expressiveness-and-generalisability">7. 表达能力和泛化能力</a></td></tr>
<tr><td><a href="#heterogeneous-gnns">8. 异构GNN</a></td></tr>
<tr><td><a href="#gnns-for-recommendation">9. 用于推荐的GNN</a></td></tr>
<tr><td><a href="#chemistry-and-biology">10. 化学和生物</a></td></tr>
</table>

## [GNN架构](#目录)

### 最具影响力的论文

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-1.md

1. **带图卷积的半监督分类**。Thomas N. Kipf，Max Welling。NeuIPS'17。[论文](https://arxiv.org/abs/1609.02907)
2. **图注意力网络**。Petar Veličković，Guillem Cucurull，Arantxa Casanova，Adriana Romero，Pietro Liò，Yoshua Bengio。ICLR'18。[论文](https://arxiv.org/abs/1710.10903)
3. **在图上使用快速局部谱滤波的卷积神经网络**。NeuIPS'16。[论文](https://arxiv.org/abs/1606.09375)
4. **先预测再传播：图神经网络遇见个性化的PageRank**。Johannes Klicpera，Aleksandar Bojchevski，Stephan Günnemann。ICLR'19。[论文](https://arxiv.org/abs/1810.05997)
5. **门控图序列神经网络**。Li, Yujia N，Tarlow, Daniel，Brockschmidt, Marc，Zemel, Richard。ICLR'16。[论文](https://arxiv.org/abs/1511.05493)
6. **大规模图上的归纳表示学习**。William L. Hamilton，Rex Ying，Jure Leskovec。NeuIPS'17。[论文](https://arxiv.org/abs/1706.02216)
7. **深度图Infomax**。Petar Veličković，William Fedus，William L. Hamilton，Pietro Liò，Yoshua Bengio，R Devon Hjelm。ICLR'19。[论文](https://openreview.net/pdf?id=rklz9iAcKQ)
8. **在图上进行知识传递网络的表示学习**。Keyulu Xu，Chengtao Li，Yonglong Tian，Tomohiro Sonobe，Ken-ichi Kawarabayashi，Stefanie Jegelka。ICML'18。[论文](https://arxiv.org/abs/1806.03536)
9. **DeepGCN：GCN能像CNN一样深入吗？**。Guohao Li，Matthias Müller，Ali Thabet，Bernard Ghanem。ICCV'19。[论文](https://arxiv.org/abs/1904.03751)
10. **DropEdge：用于节点分类的深度图卷积网络**。Yu Rong，Wenbing Huang，Tingyang Xu，Junzhou Huang。ICLR'20。[论文](https://arxiv.org/abs/1907.10903)

### 最新的SOTA

1. **使用1000层图神经网络进行训练**。Guohao Li，Matthias Müller，Bernard Ghanem，Vladlen Koltun。ICML'21。[论文](https://arxiv.org/abs/2106.07476)
2. **用于图的半监督学习的图随机神经网络**。Wenzheng Feng，Jie Zhang，Yuxiao Dong，Yu Han，Huanbo Luan，Qian Xu，Qiang Yang，Evgeny Kharlamov，Jie Tang。NeuIPS'20。[论文](https://arxiv.org/abs/2005.11079)
3. **简单而深入的图卷积网络**。Ming Chen，Zhewei Wei，Zengfeng Huang，Bolin Ding，Yaliang Li。ICML'20。[论文](https://arxiv.org/abs/2007.02133)
4. **将标签传播和简单模型相结合优于图神经网络**。Qian Huang，Horace He，Abhay Singh，Ser-Nam Lim，Austin R. Benson。ICLR'21。[论文](https://arxiv.org/abs/2010.13993)
5. **图注意力多层感知器**。Wentao Zhang，Ziqi Yin，Zeang Sheng，Wen Ouyang，Xiaosen Li，Yangyu Tao，Zhi Yang，Bin Cui。[论文](https://arxiv.org/abs/2108.10097)
6. **如何找到您友好的邻居：自我监督图注意力设计**。Dongkwan Kim，Alice Oh。ICLR'21。[论文](https://openreview.net/forum?id=Wi5KUNlqWty)
7. **迈向更深的图神经网络**。Meng Liu，Hongyang Gao，Shuiwang Ji。KDD'20。[论文](https://arxiv.org/abs/2007.09296)
8. **使用张量函数的图遍历：一种可扩展学习的元算法**。Elan Markowitz，Keshav Balasubramanian，Mehrnoosh Mirtaheri，Sami Abu-El-Haija，Bryan Perozzi，Greg Ver Steeg，Aram Galstyan。ICLR'21。[论文](https://arxiv.org/abs/2102.04350)
9. **MixHop：通过稀疏化邻域混合的高阶图卷积架构**。Sami Abu-El-Haija，Bryan Perozzi，Amol Kapoor，Nazanin Alipourfard，Kristina Lerman，Hrayr Harutyunyan，Greg Ver Steeg，Aram Galstyan。ICML'19。[论文](https://arxiv.org/abs/1905.00067)
10. **扩散改进图学习**。Johannes Klicpera，Stefan Weißenberger，Stephan Günnemann。NeuIPS'19。[论文](https://arxiv.org/abs/1911.05485)

## [大规模训练](#content)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-2.md

### 最有影响力的论文

1. **大规模图上的归纳表示学习**. William L. Hamilton, Rex Ying, Jure Leskovec. NeuIPS'17. [论文](https://arxiv.org/abs/1706.02216)
2. **FastGCN: 通过重要性采样实现快速图卷积网络学习**. Jie Chen, Tengfei Ma, Cao Xiao. ICLR'18. [论文](https://arxiv.org/abs/1801.10247)
3. **Cluster-GCN: 一种高效训练深度和大型图卷积网络的算法**. Wei-Lin Chiang, Xuanqing Liu, Si Si, Yang Li, Samy Bengio, Cho-Jui Hsieh. KDD'19. [论文](https://arxiv.org/abs/1905.07953)
4. **GraphSAINT: 基于图采样的归纳学习方法**. Hanqing Zeng, Hongkuan Zhou, Ajitesh Srivastava, Rajgopal Kannan, Viktor Prasanna. ICLR'20. [论文](https://arxiv.org/abs/1907.04931)
5. **GNNAutoScale: 借助历史嵌入实现可扩展和表达丰富的图神经网络**. Matthias Fey, Jan E. Lenssen, Frank Weichert, Jure Leskovec. ICML'21. [论文](https://arxiv.org/abs/2106.05609)
6. **利用近似PageRank扩展图神经网络规模**. Aleksandar Bojchevski, Johannes Klicpera, Bryan Perozzi, Amol Kapoor, Martin Blais, Benedek Rózemberczki, Michal Lukasik, Stephan Günnemann. KDD'20. [论文](https://arxiv.org/abs/2007.01570)
7. **具有方差减少的图卷积网络的随机训练**. *简飞，朱军和宋乐* ICML'18. [论文](https://arxiv.org/abs/1710.10568)
8. **自适应采样：快速图表示学习**. Wenbing Huang, Tong Zhang, Yu Rong和Junzhou Huang. NeuIPS'18. [论文](https://papers.nips.cc/paper/2018/file/01eee509ee2f68dc6014898c309e86bf-Paper.pdf)
9. **SIGN: 可扩展的Inception图神经网络**. Fabrizio Frasca, Emanuele Rossi, Davide Eynard, Ben Chamberlain, Michael Bronstein, Federico Monti. [论文](https://arxiv.org/abs/2004.11198)
10. **简化图卷积网络**. Felix Wu, Tianyi Zhang, Amauri Holanda de Souza Jr., Christopher Fifty, Tao Yu, Kilian Q. Weinberger. ICML'19. [论文](https://arxiv.org/abs/1902.07153)

### 最新的SOTA

1. **GraphSAINT: 基于图采样的归纳学习方法**. Hanqing Zeng, Hongkuan Zhou, Ajitesh Srivastava, Rajgopal Kannan, Viktor Prasanna. ICLR'20. [论文](https://arxiv.org/abs/1907.04931)
2. **GNNAutoScale: 借助历史嵌入实现可扩展和表达丰富的图神经网络**. Matthias Fey, Jan E. Lenssen, Frank Weichert, Jure Leskovec. ICML'21. [论文](https://arxiv.org/abs/2106.05609)
3. **深度图神经网络与浅层子图采样器**. Hanqing Zeng, Muhan Zhang, Yinglong Xia, Ajitesh Srivastava, Andrey Malevich, Rajgopal Kannan, Viktor Prasanna, Long Jin, Ren Chen. [论文](https://arxiv.org/abs/2012.01380)
4. **可扩展的图神经网络通过双向传播**. Ming Chen, Zhewei Wei, Bolin Ding, Yaliang Li, Ye Yuan, Xiaoyong Du, Ji-Rong Wen. NeuIPS'20. [论文](https://arxiv.org/abs/2010.15421)
5. **图神经网络的统一中奖假设**. Tianlong Chen, Yongduo Sui, Xuxi Chen, Aston Zhang, Zhangyang Wang. ICML'21. [论文](https://arxiv.org/abs/2102.06790).
6. **利用近似PageRank扩展图神经网络规模**. Aleksandar Bojchevski, Johannes Klicpera, Bryan Perozzi, Amol Kapoor, Martin Blais, Benedek Rózemberczki, Michal Lukasik, Stephan Günnemann. KDD'20. [论文](https://arxiv.org/abs/2007.01570)
7. **具有自标签增强训练的可扩展自适应图神经网络**. Chuxiong Sun, Hongming Gu, Jie Hu. [论文](https://arxiv.org/abs/2104.09376)
8. **Cluster-GCN: 一种高效训练深度和大型图卷积网络的算法**. Wei-Lin Chiang, Xuanqing Liu, Si Si, Yang Li, Samy Bengio, Cho-Jui Hsieh. KDD'19. [论文](https://arxiv.org/abs/1905.07953)
9. **GraphZoom: 一种准确且可扩展的多层谱图嵌入方法**. Chenhui Deng, Zhiqiang Zhao, Yongyu Wang, Zhiru Zhang, Zhuo Feng. ICLR'20. [论文](https://arxiv.org/abs/1910.02370)
10. **用于巨大图的混合CPU-GPU训练的全局邻居采样**.     Jialin Dong, Da Zheng, Lin F. Yang, Geroge Karypis. KDD'21. [论文](https://arxiv.org/abs/2106.06150)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-3.md

## [自监督学习和预训练](#content)

### 最具影响力

1. **图神经网络预训练策略。** *Weihua Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay Pande, Leskovec Jure.* ICLR 2020. [paper](https://openreview.net/forum?id=HJlWWJSFDH)
2. **深度图信息增强模型。** *Velikovi Petar, Fedus William, Hamilton William L, Li Pietro, Bengio Yoshua, Hjelm R Devon.* ICLR 2019. [paper](https://arxiv.org/abs/1809.10341)
3. **大规模图的归纳式表示学习。** *Hamilton Will, Zhitao Ying, Leskovec Jure.* NeurIPS 2017. [paper](https://arxiv.org/abs/1706.02216)
4. **Infograph: 通过最大化互信息的无监督和半监督图级表示学习。** *Sun Fan-Yun, Hoffmann Jordan, Verma Vikas, Tang Jian.* ICLR 2020. [paper](https://arxiv.org/pdf/1908.01000.pdf)
5. **GCC: 图神经网络预训练的图对比编码。** *Jiezhong Qiu, Qibin Chen, Yuxiao Dong, Jing Zhang, Hongxia Yang, Ming Ding, Kuansan Wang, Jie Tang.* KDD 2020. [paper](https://dl.acm.org/doi/pdf/10.1145/3394486.3403168)
6. **基于对比多视图的图表示学习。** *Hassani Kaveh, Khasahmadi Amir Hosein.* ICML 2020. [paper](https://arxiv.org/abs/2006.05582)
7. **具有增强技术的图对比学习。** *Yuning You, Tianlong Chen,  Yongduo Sui, Ting Chen, Zhangyang Wang, Yang Shen.* NeurIPS 2020. [paper](https://arxiv.org/abs/2010.13902)
8. **GPT-GNN: 图神经网络的生成式预训练。** *Ziniu Hu, Yuxiao Dong, Kuansan Wang, Kai-Wei Chang, Yizhou Sun.* KDD 2020. [paper](https://arxiv.org/abs/2006.15437)
9. **自监督何时有助于图卷积网络？** *Yuning You, Tianlong Chen, Zhangyang Wang, Yang Shen.* ICML 2020. [paper](https://arxiv.org/abs/2006.09136)
10. **深度图对比表示学习。** *Yanqiao Zhu, Yichen Xu, Feng Yu, Qiang Liu, Shu Wu, Liang Wang.* GRL+@ICML 2020. [paper](https://arxiv.org/abs/2006.04131)

### 最新 SOTA

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-4.md

1. **图对比学习自动化**。由Yuning You, Tianlong Chen, Yang Shen, Zhangyang Wang撰写。ICML 2021. [论文](https://arxiv.org/abs/2106.07594)
2. **自适应增强的图对比学习**。由Yanqiao Zhu, Yichen Xu, Feng Yu, Qiang Liu, Shu Wu, Liang Wang撰写。WWW 2021. [论文](https://arxiv.org/abs/2010.14945)
3. **使用局部和全局结构进行自监督图级表示学习**。由Minghao Xu, Hang Wang, Bingbing Ni, Hongyu Guo, Jian Tang撰写。ICML 2021. [论文](https://arxiv.org/pdf/2106.04113)
4. **用于对比自监督学习图表示的负采样策略**。由Hakim Hafidi, Mounir Ghogho, Philippe Ciblat, Ananthram Swami撰写。信号处理 2021. [论文](https://www.sciencedirect.com/science/article/pii/S0165168421003479)
5. **图神经网络预训练学习**。由Yuanfu Lu, Xunqiang Jiang, Yuan Fang, Chuan Shi撰写。AAAI 2021. [论文](http://shichuan.org/doc/101.pdf)
6. **通过图互信息最大化进行图表示学习**。由Zhen Peng, Wenbing Huang, Minnan Luo, Qinghua Zheng, Yu Rong, Tingyang Xu, Junzhou Huang撰写。WWW 2020. [论文](https://arxiv.org/abs/2002.01169)
7. **用于异构图对比学习的结构感知硬负采样**。由Yanqiao Zhu, Yichen Xu, Hejie Cui, Carl Yang, Qiang Liu, Shu Wu撰写。arXiv预印本 arXiv:2108.13886 2021. [论文](https://arxiv.org/abs/2108.13886)
8. **通过全局上下文预测进行自监督图表示学习**。由Zhen Peng, Yixiang Dong, Minnan Luo, Xiao-Ming Wu, Qinghua Zheng撰写。arXiv预印本 arXiv:2003.01604 2020. [论文](https://arxiv.org/abs/2003.01604)
9. **CSGNN：用于分子相互作用预测的对比自监督图神经网络**。由Chengshuai Zhao, Shuai Liu, Feng Huang, Shichao Liu, Wen Zhang撰写。IJCAI 2021. [论文](https://www.ijcai.org/proceedings/2021/0517.pdf)
10. **对半图区分：一种用于预训练图神经网络的简单图级自监督策略**。由Pengyong Li, Jun Wang, Ziliang Li, Yixuan Qiao, Xianggen Liu, Fei Ma, Peng Gao, Sen Song, Guotong Xie撰写。IJCAI 2021. [论文](https://www.ijcai.org/proceedings/2021/0371.pdf)

## [过度平滑和深度GNN](#内容)

### 最有影响力的

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-5.md

### 最新SOTA

1. **在图神经网络中实现深度增强学习能力的不同iable组归一化.** *周开雄, 黄潇, 李宇宁, 查导辰, 陈锐, 胡霞.* NeurIPS 2020. [论文](https://papers.nips.cc//paper/2020/hash/33dd6dba1d56e826aac1cbf23cdcca87-Abstract.html)
2. **散射GCN: 克服图卷积网络中的过度平滑问题.** *闵一萌, Frederik Wenkel, Guy Wolf.* NeurIPS 2020. [论文](https://papers.nips.cc//paper/2020/hash/a6b964c0bb675116a15ef1325b01ff45-Abstract.html)
3. **通过渐变提升和应用到多尺度图神经网络的转导优化和泛化分析.** *太地境, 铃木泰治.* NeurIPS 2020. [论文](https://papers.nips.cc//paper/2020/hash/dab49080d80c724aad5ebf158d63df41-Abstract.html)
4. **图神经网络的瓶颈及其实际影响.** *Uri Alon, Eran Yahav.* ICLR 2021. [论文](https://openreview.net/forum?id=i80OPhOCVH2)
5. **简单谱图卷积.** *朱浩, Piotr Koniusz.* ICLR 2021. [论文](https://openreview.net/forum?id=CYO5T-YjWZV)
6. **用1000层训练图神经网络.** *李国豪, Matthias Müller, Bernard Ghanem, Vladlen Koltun.* ICML 2021. [论文](http://proceedings.mlr.press/v139/li21o.html)
7. **图神经网络的优化: 跳连接和更深层隐式加速.** *Keyulu Xu, Mozhi Zhang, Stefanie Jegelka, Kenji Kawaguchi.* ICML 2021. [论文](http://proceedings.mlr.press/v139/xu21k.html)
8. **GRAND: 图神经扩散.** *Ben Chamberlain, James Rowbottom, Maria I Gorinova, Michael Bronstein, Stefan Webb, Emanuele Rossi.* ICML 2021. [论文](http://proceedings.mlr.press/v139/chamberlain21a.html)
9. **方向性图网络.** *Dominique Beani, Saro Passaro, Vincent Létourneau, Will Hamilton, Gabriele Corso, Pietro Lió.* ICML 2021. [论文](http://proceedings.mlr.press/v139/beani21a.html)
10. **改善图神经网络中的宽度反向传播有助于学习长程依赖性.** *Denis Lukovnikov, Asja Fischer.* ICML 2021. [论文](http://proceedings.mlr.press/v139/lukovnikov21a.html)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-6.md

## [图鲁棒性](#content)

### 最具影响力

1. **对图数据上的神经网络的对抗攻击**。*Zügner Daniel, Akbarnejad Amir, Günnemann Stephan*。KDD 2018. [文章链接](https://arxiv.org/abs/1805.07984) [源代码链接](https://github.com/danielzuegner/nettack)
2. **对图结构数据的对抗攻击**。*Dai Hanjun, Li Hui, Tian Tian, Huang Xin, Wang Lin, Zhu Jun, Song Le*。ICML 2018. [文章链接](https://arxiv.org/abs/1806.02371) [源代码链接](https://github.com/Hanjun-Dai/graph_adversarial_attack)
3. **通过元学习对图神经网络进行对抗攻击**。*Zügner Daniel, Günnemann Stephan*。ICLR 2019. [文章链接](https://arxiv.org/abs/1902.08412) [源代码链接](https://github.com/danielzuegner/gnn-meta-attack)
4. **抵御对抗攻击的鲁棒图卷积网络**。*Zhu Dingyuan, Zhang Ziwei, Cui Peng, Zhu Wenwu*。KDD 2019. [文章链接](https://dl.acm.org/doi/abs/10.1145/3292500.3330851?casa_token=cCf7RRIzp60AAAAA:CQRAqGd--EvKBZfUenQ0StGA9JwoyY0ZBVhZ0R6OF4n8Za3N0wopLpev6se5r6YT5BopGE8oj0fUfhc) [源代码链接](https://github.com/ZW-ZHANG/RobustGCN)
5. **通过图污染对节点嵌入进行对抗攻击**。*Bojchevski Aleksandar, Günnemann Stephan*。ICML 2019. [文章链接](https://arxiv.org/abs/1809.01093) [源代码链接](https://github.com/abojchevski/node_embedding_attack)
6. **图神经网络的拓扑攻击与防御：基于优化视角**。*Xu Kaidi, Chen Hongge, Liu Sijia, Chen Pin-Yu, Weng Tsui-Wei, Hong Mingyi, Lin Xue*。IJCAI 2019. [文章链接](https://arxiv.org/abs/1906.04214)
7. **图数据上的对抗样本：攻击与防御的深入洞察**。*Wu Huijun, Wang Chen, Tyshetskiy Yuriy, Docherty Andrew, Lu Kai, Zhu Liming*。IJCAI 2019. [文章链接](https://arxiv.org/abs/1903.01610)
8. **图卷积网络的可证实鲁棒性和鲁棒训练**。*Zügner Daniel, Günnemann Stephan*。KDD 2019. [文章链接](https://dl.acm.org/doi/abs/10.1145/3292500.3330905?casa_token=RKxopFEgP4MAAAAA:WPC4t9R_rTVRu2179sw3PlVLl5TzSDfYALMqw5cNSz53hiL4jSmT8_gQiQ8kn0N47GzWiJkXSo-FAzk)
9. **基于图结构动态规范化的图对抗训练**。*Feng Fuli, He Xiangnan, Tang Jie, Chua Tat-Seng*。TKDE 2019. [文章链接](https://ieeexplore.ieee.org/abstract/document/8924766/?casa_token=H51wrycvI6UAAAAA:-q7RBGcyWMUiSjJhonyV1zoIGDgVkVndSZ4E3B77XFmiGS31msJuoa-leKhW3aTuGV-XLfTi504)
10. **图数据的对抗攻击与防御：一项综述**。*Sun Lichao, Dou Yingtong, Yang Carl, Wang Ji, Yu Philip S, He Lifang, Li Bo*。arXiv预印本arXiv:1812.10528 2018. [文章链接](https://arxiv.org/abs/1812.10528)

### 最新最好方法 (SOTA)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-7.md

1. **TDGIA: 有效的图神经网络注入攻击**。*邹旭，郑勤凯，董宇啸，关心禹，Kharlamov Evgeny，陆嘉梁，唐杰*。KDD 2021。[论文](https://arxiv.org/abs/2106.06663) [代码](https://github.com/THUDM/tdgia/)
2. **Gnnguard: 防御图神经网络对抗攻击**。*张翔，Zitnik Marinka*。NeurIPS 2020。[论文](https://arxiv.org/abs/2006.08149)
3. 在规模上攻击图神经网络。Geisler Simon，Zügner Daniel，Bojchevski Aleksandar，Günnemann Stephan。AAAI workshop 2021. 论文
4. 用于图上半监督学习的图随机神经网络。冯文正，张杰，董宇晓，韩宇，栾焕波，徐倩，杨强，Kharlamov Evgeny，唐杰。NeurIPS 2020. 论文代码
5. Graph information bottleneck. Wu Tailin, Ren Hongyu, Li Pan, Leskovec Jure. NeurIPS 2020. paper code
6. Graph Neural Networks的信息混淆。廖培元，赵涵，徐科宇，Jaakkola Tommi，Gordon Geoffrey J，Jegelka Stefanie，Salakhutdinov Ruslan。ICML 2021. 论文
7. 理解图卷积网络中的结构脆弱性。陈亮，李金堂，彭启彪，刘阳，郑子斌，杨卡尔。IJCAI 2021. 论文代码
8. 图神经网络对抗结构扰动的认证鲁棒性。王炳辉，贾金源，曹晓宇，龚Neil Zhenqiang。KDD 2021. 论文代码
9. 针对对抗攻击的鲁棒多图学习的表达力1-Lipschitz神经网络。赵鑫，张泽如，张子杰，吴凌飞，金佳音，周阳，金若明，窦德静，严达。ICML 2021. 论文
10. 通过鲁棒聚合实现可靠的图神经网络。Geisler Simon，Zügner Daniel，Günnemann Stephan。NeurIPS 2020. 论文代码

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-8.md

### 最近的最先进技术

1. **计算病理学中图神经网络的解释量化**。*Jaume Guillaume, Pati Pushpak, Bozorgtabar Behzad, Foncubierta Antonio, Anniciello Anna Maria, Feroce Florinda, Rau Tilman, Thiran Jean-Philippe, Gabrani Maria, Goksel Orcun*。计算机视觉与模式识别会议CVPR 2021。[论文](https://arxiv.org/pdf/2011.12646.pdf)
2. **用于可解释医疗记录诊断的反事实支持事实提取方法基于图网络**。*Wu Haoran, Chen Wei, Xu Shuang, Xu Bo*。NAACL 2021。[论文](https://aclanthology.org/2021.naacl-main.156.pdf)
3. **比较与地面真实结果时的错误：评价图神经网络解释方法**。*Faber Lukas, K. Moghaddam Amin, Wattenhofer Roger*。KDD 2021。[论文](https://dl.acm.org/doi/10.1145/3447548.3467283)
4. **用于可解释脑网络分类的反事实图**。*Abrate Carlo, Bonchi Francesco*。知识发现与数据挖掘会议KDD 2021。[论文](https://arxiv.org/pdf/2106.08640.pdf)
5. **基于子图推理的时间知识图预测的可解释性**。*Zhen Han, Peng Chen, Yunpu Ma, Volker Tresp*。国际学习表示会议ICLR 2021。[论文](https://iclr.cc/virtual/2021/poster/3378)
6. **生成因果解释的图神经网络**。*Lin Wanyu, Lan Hao, Li Baochun*。国际机器学习会议ICML 2021。[论文](https://arxiv.org/pdf/2104.06643.pdf)
7. **通过正交化和诱导稀疏性改进分子图神经网络的可解释性**。*Henderson Ryan, Clevert Djork-Arné, Montanari Floriane*。国际机器学习会议ICML 2021。[论文](https://arxiv.org/pdf/2105.04854.pdf)
8. **用超参数重要性进行可解释的自动图表示学习**。*Wang Xin, Fan Shuyi, Kuang Kun, Zhu Wenwu*。国际机器学习会议ICML 2021。[论文](http://proceedings.mlr.press/v139/wang21f/wang21f.pdf)
9. **通过相关行走的图神经网络的高阶解释**。*Schnake Thomas, Eberle Oliver, Lederer Jonas, Nakajima Shinichi, Schütt Kristof T, Müller Klaus-Robert, Montavon Grégoire*。arXiv预印本arXiv:2006.`03589 2020。[论文](https://arxiv.org/pdf/2006.03589.pdf)
10. **HENIN：学习用于社交媒体上可解释的网络霸凌检测的异构神经交互网络**。*Chen, Hsin-Yu and Li, Cheng-Te*。EMNLP 2020。[论文](https://www.aclweb.org/anthology/2020.emnlp-main.200/)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-9.md

## [表达能力和泛化能力](#content)

### 最具影响力的论文

1. **图神经网络的威力有多大？** *Keyulu Xu, Weihua Hu, Jure Leskovec, Stefanie Jegelka.* ICLR 2019. [论文](https://arxiv.org/abs/1810.00826)
2. **不变和等变图网络。** *Haggai Maron, Heli Ben-Hamu, Nadav Shamir, Yaron Lipman.* ICLR 2019. [论文](https://openreview.net/forum?id=Syx72jC9tm)
3. **理解图神经网络中的注意力和泛化性能。** *Boris Knyazev, Graham W. Taylor, Mohamed R. Amer.* NeurIPS 2019. [论文](https://arxiv.org/abs/1905.02850) 
4. **可证明强大的图网络。** *Haggai Maron, Heli Ben-Hamu, Hadar Serviansky, Yaron Lipman.* NeurIPS 2019. [论文](http://papers.nips.cc/paper/by-source-2019-1275)
5. **理解图神经网络在学习图拓扑中的表示能力。** *Nima Dehmamy, Albert-Laszlo Barabasi, Rose Yu.* NeurIPS 2019. [论文](http://papers.nips.cc/paper/by-source-2019-8876)
6. **图同构测试与GNN中的函数逼近之间的等价性。** *Zhengdao Chen, Soledad Villar, Lei Chen, Joan Bruna.* NeurIPS 2019. [论文](https://proceedings.neurips.cc/paper/2019/hash/71ee911dd06428a96c143a0b135041a4-Abstract.html)
7. **通用的不变和等变图神经网络。** *Nicolas Keriven, Gabriel Peyré.* NeurIPS 2019. [论文](https://proceedings.neurips.cc/paper/2019/hash/ea9268cb43f55d1d12380fb6ea5bf572-Abstract.html)
8. **图卷积神经网络的稳定性和泛化性能。** *Saurabh Verma和Zhi-Li Zhang.* KDD 2019. [论文](https://dl.acm.org/doi/10.1145/3292500.3330956)
9. **图神经网络在节点分类中的表达能力指数下降。** *Kenta Oono, Taiji Suzuki.* ICLR 2020. [论文](https://openreview.net/pdf?id=S1ldO2EFPr)
10. **图神经网络的泛化和表示限制。** *Vikas Garg, Stefanie Jegelka, Tommi Jaakkola.* ICML 2020. [论文](https://www.mit.edu/~vgarg/GNN_CameraReady.pdf)

### 最新SOTA(最佳结果)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-10.md

## [异构图神经网络](#content)

### 最具影响力的研究论文

1. **基于PAC-Bayesian方法的图神经网络泛化界限研究.** *Renjie Liao, Raquel Urtasun, Richard Zemel.* ICLR 2021. [论文](https://openreview.net/forum?id=TR-Nj6nFx42)
2. **用谱角度分析图神经网络的表达能力.** *Muhammet Balcilar, Guillaume Renton, Pierre Héroux, Benoit Gaüzère, Sébastien Adam, Paul Honeine.* ICLR 2021. [论文](https://openreview.net/forum?id=-qh0M9XWxnv)
3. **图神经网络与图增强型MLP的比较.** *Lei Chen, Zhengdao Chen, Joan Bruna.* ICLR 2021. [论文](https://openreview.net/forum?id=tiqI7w64JG2)
4. **低秩可学习局部滤波的图卷积网络.** *Xiuyuan Cheng, Zichen Miao, Qiang Qiu.* ICLR 2021. [论文](https://openreview.net/forum?id=9OHFhefeB86)
5. **从局部结构到图神经网络中的尺寸泛化.** *Gilad Yehudai, Ethan Fetaya, Eli Meirom, Gal Chechik, Haggai Maron.* ICML 2021. [论文](https://arxiv.org/abs/2010.08853)
6. **提升图神经网络表达能力的集体学习框架.** *Mengyue Hang, Jennifer Neville, Bruno Ribeiro.* ICML 2021. [论文](http://proceedings.mlr.press/v139/hang21a.html)
7. **Weisfeiler和Lehman 把拓扑学引入: 信息传递的单纯网络.** *Cristian Bodnar, Fabrizio Frasca, Yu Guang Wang, Nina Otter, Guido Montúfar, Pietro Liò, Michael Bronstein.* ICML 2021. [论文](https://arxiv.org/abs/2103.03212)
8. **突破信息传递图神经网络的极限.** *Muhammet Balcilar, Pierre Heroux, Benoit Gauzere, Pascal Vasseur, Sebastien Adam, Paul Honeine.* *ICML 2021.* [论文](http://proceedings.mlr.press/v139/balcilar21a.html)
9. **在信息传递框架中比较图卷积网络之间的最大程度一致到度的方法.** *Floris Geerts, Filip Mazowiecki, Guillermo A. Pérez.* ICML 2021. [论文](https://arxiv.org/abs/2004.02593)
10. **用于半监督分类的图卷积网络：改进的线性可分性和超出分布的泛化.** *Aseem Baranwal, Kimon Fountoulakis, Aukosh Jagannath.* ICML 2021. [论文](http://proceedings.mlr.press/v139/baranwal21a.html)

## [异构GNNs](#content)

### 最具影响力的研究论文

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-11.md

1. **异构图注意力网络**。*Xiao Wang, Houye Ji, Chuan Shi, Bai Wang, Peng Cui, P. Yu, Yanfang Ye* WWW 2019. [论文](https://arxiv.org/pdf/1903.07293.pdf) [代码](https://github.com/taishan1994/pytorch_HAN)
2. **属性多重异构网络的表示学习**。*Yukuo Cen, Xu Zou, Jianwei Zhang, Hongxia Yang, Jingren Zhou, Jie Tang* KDD 2019 [论文](https://arxiv.org/pdf/1905.01669.pdf) [代码](https://github.com/THUDM/GATNE)
3. **ActiveHNE: 主动的异构网络嵌入** *Xia Chen, Guoxian Yu, Jun Wang, Carlotta Domeniconi, Zhao Li, Xiangliang Zhang* IJCAI 2019 [论文](https://arxiv.org/pdf/1905.05659.pdf) 
4. **超图神经网络** *Yifan Feng, Haoxuan You, Zizhao Zhang, Rongrong Ji, Yue Gao*. AAAI 2019 [论文](https://arxiv.org/pdf/1809.09401.pdf) [代码](https://github.com/iMoonLab/HGNN)
5. **动态超图神经网络** *Jianwen Jiang, Yuxuan Wei, Yifan Feng, Jingxuan Cao, Yue Gao* IJCAI 2019 [论文](https://www.ijcai.org/proceedings/2019/0366.pdf) [代码](https://github.com/iMoonLab/DHGNN)
6. **HyperGCN: 在超图上训练图卷积网络的新方法** *Naganand Yadati, Madhav Nimishakavi, Prateek Yadav, Vikram Nitin, Anand Louis, Partha Talukdar* [论文](https://proceedings.neurips.cc/paper/2019/file/1efa39bcaec6f3900149160693694536-Paper.pdf) [代码](https://github.com/malllabiisc/HyperGCN)
7. **基于图注意网络的异构网络类型感知锚链接预测** *Xiaoxue Li, Yanmin Shang, Yanan Cao, Yangxi Li, Jianlong Tan, Yanbing Liu.* AAAI 2020 [论文](https://ojs.aaai.org/index.php/AAAI/article/download/5345/5201)
8. **基于组合的多关系图卷积网络** *Shikhar Vashishth, Soumya Sanyal, Vikram Nitin, Partha Talukdar.* ICLR 2020 [论文](https://openreview.net/pdf?id=BylA_C4tPr) [代码](https://github.com/malllabiisc/CompGCN)
9. **Hyper-SAGNN: 基于自注意力的超图神经网络** *Ruochi Zhang, Yuesong Zou, Jian Ma.* ICLR 2020 [论文](https://openreview.net/pdf?id=ryeHuJBtPH) [代码](https://github.com/ma-compbio/Hyper-SAGNN)
10. **异构图变换器** *Hu, Ziniu, Yuxiao Dong, Kuansan Wang, and Yizhou Sun* WWW 2020 [论文](https://dl.acm.org/doi/pdf/10.1145/3366423.3380027) [代码](https://github.com/acbull/pyHGT)

### 最近的SOTA (State-of-the-Art)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-12.md

## [GNNs用于推荐系统](#content)

### 最具影响力的论文

1. **用于异构结构学习的基于注意力的图神经网络** *Huiting Hong, Hantao Guo, Yu-Cheng Lin, Xiaoqing Yang, Zang Li, Jieping Ye* AAAI 2020 [论文](http://shichuan.org/hin/topic/2020.An%20Attention-Based%20Graph%20Neural%20Network%20for%20Heterogeneous%20Structural%20Learning.pdf) [代码](https://github.com/didi/hetsann)
2. **异构深度图信息增益** *Ren, Yuxiang, Bo Liu, Chao Huang, Peng Dai, Liefeng Bo, and Jiawei Zhang* AAAI 2020 workshop [论文](https://arxiv.org/abs/1911.08538) [代码](https://github.com/YuxiangRen/Heterogeneous-Deep-Graph-Infomax)
3. **大规模异构信息网络中的非局部注意力学习** *Xiao, Yuxin, Zecheng Zhang, Carl Yang, and Chengxiang Zhai.* IEEE BigData 2019 [论文](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1hJrR2Z6qmA/pdf) [代码](https://github.com/xiaoyuxin1002/NLAH)
4. **基于贝叶斯排序非线性嵌入的多关系分类** *Rashed, Ahmed, Josif Grabocka, and Lars Schmidt-Thieme.* KDD 2019 [论文](https://dl.acm.org/doi/pdf/10.1145/3292500.3330863) [代码](https://github.com/ahmedrashed-ml/BRNLE)
5. **RUnimp: KDDCUP 2021 MAG240M-LSC的解决方案** *Yunsheng Shi, Zhengjie Huang, Weibin Li , Weiyue Su, Shikun Feng* KDD CUP 2021 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_BD-PGL.pdf) [代码](https://github.com/PaddlePaddle/PGL/tree/main/examples/kddcup2021/MAG240M/r_unimp)
6. **使用自助法进行大规模节点分类** *Petar Velickovic, Peter Battaglia, Jonathan Godwin, Alvaro Sanchez, David Budden, Shantanu Thakoor, Jacklynn Stott, Ravichandra Addanki, Thomas Keck, Andreea Deac* KDD CUP 2021 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Academic.pdf) [代码](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc/mag)
7. **SYNERISE在KDD CUP 2021中的节点分类：海量异构图中的节点分类** *Michal Daniluk, Jacek Dabrowski, Konrad Goluchowski, Barbara Rychalska* KDD CUP 2021 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_SyneriseAI.pdf) [代码](https://github.com/Synerise/kdd-cup-2021)
8. **基于元路径的大规模异构图标签传播** *Qiuying Peng, Wencai Cao, Zheng Pan* KDD CUP 2021 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Topology_mag.pdf) [代码](https://github.com/qypeng-ustc/mplp)
9. **KDD CUP 2021 MAG240M-LSC团队Passages获胜解决方案** *Bole Ai, Xiang Long, Kaiyuan Li, Quan Lin, Xiaofan Liu, Pengfei Wang, Mingdao Wang, Zhichao Feng, Kun Zhao* KDD CUP 2021 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_passages.pdf) [代码](https://github.com/passages-kddcup2021/KDDCUP2021_OGB_LSC_MAG240M)
10. **更深更大更好：KDD CUP 2020 OGB-LSC** *Guohao Li, Hesham Mostafa, Jesus Alejandro Zarzar Torano, Sami Abu-El-Haija, Marcel Nassar, Daniel Cummings, Sohil Shah, Matthias Mueller, Bernard Ghanem* KDD CUP 2020 [论文](https://ogb.stanford.edu/paper/kddcup2021/mag240m_DeeperBiggerBetter.pdf) [代码](https://github.com/zarzarj/DeeperBiggerBetter_KDDCup)

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-13.md

# 最新状态-of-the-art（SOTA）

1. **图卷积矩阵补全**。*Rianne van den Berg, Thomas N. Kipf, Max Welling*。KDD 2018. [论文](https://arxiv.org/abs/1706.02263v2) [代码](https://github.com/riannevdberg/gc-mc)
2. **基于图神经网络的基于会话的推荐**。*Shu Wu, Yuyuan Tang, Yanqiao Zhu, Xing Xie, Liang Wang, Tieniu Tan*。AAAI 2019. [论文](https://arxiv.org/abs/1811.00855v1) [代码](https://github.com/CRIPAC-DIG/SR-GNN#paper-data-and-code)
3. **神经图协同过滤**。*Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, Tat-Seng Chua*。SIGIR 2019. [论文](https://arxiv.org/abs/1905.08108v1) [代码](https://github.com/xiangwang1223/neural_graph_collaborative_filtering)
4. **社交推荐的图神经网络**。*Wenqi Fan, Yao Ma, Qing Li, Yuan He, Eric Zhao, Jiliang Tang, Dawei Yin*。WWW 2019. [论文](https://export.arxiv.org/pdf/1902.00724) [代码](https://github.com/wenqifan03/GraphRec-WWW19)
5. **KGAT：用于推荐的知识图注意网络**。*Xiang Wang, Xiangnan He, Yixin Cao, Meng Liu, Tat-Seng Chua*。KDD 2019. [论文](https://arxiv.org/abs/1905.07854v1) [代码](https://github.com/xiangwang1223/knowledge_graph_attention_network)
6. **Fi-GNN：通过图神经网络对特征交互进行建模以用于CTR预测**。*Zekun Li, Zeyu Cui, Shu Wu, Xiaoyu Zhang, Liang Wang*。WWW 2019. [论文](https://arxiv.org/pdf/1910.05552.pdf) [代码](https://github.com/CRIPAC-DIG/Fi_GNN)
7. **LightGCN：简化和推动用于推荐的图卷积网络**。*Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, Meng Wang*。SIGIR 2020. [论文](https://arxiv.org/abs/2002.02126v1) [代码](https://github.com/kuandeng/LightGCN)
8. **重温基于图的协同过滤：线性残差图卷积网络方法**。*Lei Chen, Richang Hong, Kun Zhang, Meng Wang*。AAAI 2020. [论文](https://export.arxiv.org/pdf/2001.10167) [代码](https://github.com/newlei/LRGCCF)
9. **TAGNN：面向基于会话的推荐的目标注意力图神经网络**。*Feng Yu, Yanqiao Zhu, Qiang Liu, Shu Wu, Liang Wang, Tieniu Tan*。SIGIR 2020. [论文](https://arxiv.org/pdf/2005.02844.pdf) [代码](https://github.com/johnny12150/TA-GNN)
10. **基于图卷积网络的多行为推荐**。*Jin, Bowen and Gao, Chen and He, Xiangnan and Jin, Depeng and Li, Yong*。SIGIR 2020. [论文](http://staff.ustc.edu.cn/~hexn/papers/sigir20-MBGCN.pdf) [代码]()

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-14.md

## 化学和生物学

### 最有影响力的推荐论文

1. **基于贝叶斯图卷积神经网络的准确和多样化项目推荐框架**。作者：孙佳宁，郭伟，张登城，张颖学，瑞格尔·弗洛伦斯，胡耀晨，郭惠锋，唐睿明，袁涵，何修强，马克·科茨。会议：KDD 2020。[论文](https://dl.acm.org/doi/pdf/10.1145/3394486.3403254) [代码]()
2. **MixGCF：基于图神经网络的推荐系统的改进训练方法**。作者：黄庭霖，董雨霄，丁鸣，杨臻，冯文政，王欣宇，唐杰。会议：KDD 2021。[论文](https://dl.acm.org/doi/pdf/10.1145/3447548.3467408) [代码](https://github.com/huangtinglin/MixGCF)
3. **预训练图神经网络用于冷启动用户和项目表示**。作者：郝博文，张婧，尹洪志，李翠平，陈洪。会议：WSDM 2021。[论文](https://arxiv.org/pdf/2012.07064v1.pdf) [代码](https://github.com/jerryhao66/Pretrain-Recsys)
4. **用于推荐的自监督图学习**。作者：吴建灿，王翔，冯福利，何向南，陈亮，连建勋，谢兴。会议：SIGIR 2021。[论文](https://arxiv.org/abs/2010.10783v4) [代码](https://github.com/wujcan/SGL)
5. **面向兴趣的消息传递GCN用于推荐**。作者：刘凡，程志勇，朱磊，高赞，聂立强。会议：WWW 2021。[论文](https://arxiv.org/abs/2102.10044) [代码](https://github.com/liufancs/IMP_GCN)
6. **基于神经图匹配的协同过滤推荐**。作者：苏逸欣，张蕊，Sarah Erfani，干俊昊。会议：SIGIR 2021。[论文](https://arxiv.org/abs/2105.04067) [代码](https://github.com/ruizhang-ai/GMCF_Neural_Graph_Matching_based_Collaborative_Filtering)
7. **图卷积网络的顺序推荐**。作者：常建新，高晨，郑煜，惠奕群，牛亚楠，宋阳，金德朋，李勇。会议：SIGIR 2021。[论文](https://arxiv.org/abs/2106.14226) [代码]()
8. **使用随机掩码的结构化图卷积网络用于推荐系统**。作者：陈慧媛，王岚，林玉三，叶青嘉迈克尔，王飞，杨浩。会议：SIGIR 2021。[论文](https://dl.acm.org/doi/10.1145/3404835.3462868) [代码]()
9. **自监督图共训练用于基于会话的推荐**。作者：夏新，尹洪志，余君亮，邵颖霞，崔利珍。会议：CIKM 2021。[论文](https://arxiv.org/abs/2108.10560) [代码](https://github.com/xiaxin1998/cotrec)
10. **通过知识图谱上的伪标记缓解推荐中的冷启动问题**。作者：戸樫理久，大谷真由，佐藤真一。会议：WSDM 2021。[论文](https://arxiv.org/pdf/2011.05061.pdf) [代码]()

## 翻译 D:\mydata\Py_project\GPT_Academic\gpt_academic_3.5\gpt_log\default\批量Markdown翻译/raw-readme-2023-10-30-18-34-18.md.part-15.md

1. **图形 U-Net**. *高洪洋，纪水旺*。机器学习国际会议 2019。[论文](http://proceedings.mlr.press/v97/gao19a.html)
2. **MoleculeNet: 分子机器学习的基准**。*吴振琴，Ramsundar Bharath，Feinberg Evan N，Gomes Joseph，Geniesse Caleb，Pappu Aneesh S，Leswing Karl，Pande Vijay*。化学科学 2018。[论文](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a)
3. **用于图分类的端到端深度学习架构**。*张牧涵，崔志诚，Neumann Marion，陈一心*。第 32 届 AAAI 人工智能国际会议 2018。[论文](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17146)
4. **具有可微分池化的分层图表示学习**。*应瑞克斯，尤佳煊，莫里斯·克里斯托弗，任翔，汉密尔顿·威廉姆·L，雷斯科维克·尤雷*。arXiv 预印本 arXiv:1806.08804 2018。[论文](https://arxiv.org/abs/1806.08804)
5. **图神经网络有多强大？**。*许可天，胡伟华，雷斯科维克·尤雷，Jegelka Stefanie*。arXiv 预印本 arXiv:1810.00826 2018。[论文](https://arxiv.org/abs/1810.00826)
6. **使用结构注意力进行图分类**。*李约翰·波亚兹，Rossi Ryan，孔祥楠*。第三十届 ACM SIGKDD 国际知识发现与数据挖掘会议论文集 2018。[论文](https://dl.acm.org/doi/abs/10.1145/3219819.3219980)
7. **量子化学的神经信息传递**。*Gilmer Justin，Schoenholz Samuel S，Riley Patrick F，Vinyals Oriol，Dahl George E*。机器学习国际会议 2017。[论文](http://proceedings.mlr.press/v70/gilmer17a)
8. **学习用于图的卷积神经网络**。*Niepert Mathias，Ahmed Mohamed，Kutzkov Konstantin*。机器学习国际会议 2016。[论文](http://proceedings.mlr.press/v48/niepert16)
9. **基于图结构数据的深度卷积网络**。*Henaff Mikael，Bruna Joan，LeCun Yann*。arXiv 预印本 arXiv:1506.05163 2015。[论文](https://arxiv.org/abs/1506.05163)
10. **用于学习分子指纹的图卷积网络**。*Duvenaud David，Maclaurin Dougal，Aguilera-Iparraguirre Jorge，Gómez-Bombarelli Rafael，Hirzel Timothy，Aspuru-Guzik Alán，Adams Ryan P*。arXiv 预印本 arXiv:1509.09292 2015。[论文](https://arxiv.org/abs/1509.09292)

### 最近的 SOTA

1. **使用深度学习进行生物网络分析**。*Muzio Giulia，O'Bray Leslie，Borgwardt Karsten*。简明生物信息学 2021。[论文](https://academic.oup.com/bib/article/22/2/1515/5964185?login=true)
2. **变压器在图表示上真的表现不佳吗？**。*Ying Chengxuan，Cai Tianle，Luo Shengjie，Zheng Shuxin，Ke Guolin，He Di，Shen Yanming，Liu Tie-Yan*。arXiv 预印本 arXiv:2106.05234 2021。[论文](https://arxiv.org/abs/2106.05234)
3. **有向无环图神经网络**。*Thost Veronika，陈杰*。arXiv 预印本 arXiv:2101.07965 2021。[论文](https://arxiv.org/abs/2101.07965)
4. **方向图网络**。*Beani Dominique，Passaro Saro，Létourneau Vincent，Hamilton Will，Corso Gabriele，Liò Pietro*。机器学习国际会议 2021。[论文](http://proceedings.mlr.press/v139/beani21a.html)
5. **基准化图神经网络**。*Dwivedi Vijay Prakash，Joshi Chaitanya K，Laurent Thomas，Bengio Yoshua，Bresson Xavier*。arXiv 预印本 arXiv:2003.00982 2020。[论文](https://arxiv.org/abs/2003.00982)
6. **Structpool：通过条件随机场进行结构化图池化**。*Yuan Hao，Ji Shuiwang*。第七届国际学习表示会议论文集 2020。[论文](https://par.nsf.gov/servlets/purl/10159731)
7. **抗生素发现的深度学习方法**。*Stokes Jonathan M，Yang Kevin，Swanson Kyle，Jin Wengong，Cubillos-Ruiz Andres，Donghia Nina M，MacNair Craig R，French Shawn，Carfrae Lindsey A，Bloom-Ackermann Zohar，等*。细胞 2020。[论文](https://www.sciencedirect.com/science/article/pii/S0092867420301021)
8. **主要邻域聚合图网络**。*Corso Gabriele，Cavalleri Luca，Beaini Dominique，Liò Pietro，Veličković Petar*。arXiv 预印本 arXiv:2004.05718 2020。[论文](https://arxiv.org/abs/2004.05718)
9. **用于图分类的图神经网络的公平比较**。*Errica Federico，Podda Marco，Bacciu Davide，Micheli Alessio*。arXiv 预印本 arXiv:1912.09893 2019。[论文](https://arxiv.org/abs/1912.09893)
10. **具有特征池化的图卷积网络**。*Ma Yao，Wang Suhang，Aggarwal Charu C，Tang Jiliang*。第 25 届 ACM SIGKDD 国际知识发现与数据挖掘会议论文集 2019。[论文](https://dl.acm.org/doi/abs/10.1145/3292500.3330982)

---

会议:

ICLR: International Conference on Learning Representations
ICML: International Conference on Machine Learning																A
NeurIPS: Conference on Neural Information Processing Systems												A
SIGKDD: ACM SIGKDD Conference on Knowledge Discovery and Data Mining						A						
WWW: International World Wide Web Conference																	A
AAAI: AAAI Conference on Artificial Intelligence																		A						
IJCAIJ: International Joint Conference on Artificial Intelligence													A


期刊:

arXiv preprint
Chemical science
Briefings in bioinformatics																											B
ACM Transactions on Knowledge Discovery from Data (TKDE)													B
IEEE Transactions on Knowledge and Data Engineering (IEEE TKDE)											A

