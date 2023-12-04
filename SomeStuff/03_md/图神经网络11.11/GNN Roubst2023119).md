## GNN Roubst

### GPT-Academic Report

相关工作 图神经网络（Graph Neural Networks, GNNs）近年来因其在图结构数据中建模关系依赖性的能力而引起了广泛关注。然而，与任何机器学习模型一样，GNNs容易受到对抗攻击和输入扰动的影响，这可能会损害它们的可靠性和性能。因此，越来越多的人对开发能够抵御各种形式的攻击和输入数据中的噪声的强健性GNN模型产生了浓厚的兴趣。在本节中，我们将讨论与GNN强健性相关的一些重要研究工作。

增强GNNs鲁棒性的一种方法是通过学习图结构。Jin等人（2020）提出了一种名为Pro-GNN的框架，将学习结构图与强健图神经网络相结合。作者们证明了与神经网络架构一起学习图结构可以提高模型对抗攻击的鲁棒性。

另一方面的研究侧重于无监督结构细化，以加强GNN模型中的防御。Li等人（2022）引入了一种无监督方法来细化图结构，从而增强GNNs的鲁棒性。他们表明，在GNN模型中具有可靠的表示可以提高对抗攻击的防御能力。

了解GNNs对结构噪声的鲁棒性是另一个重要方面。Fox和Rajamanickam（2019）对GNNs对结构噪声的鲁棒性进行了研究，并显示GNN模型可以达到近乎完美的准确性。这项研究揭示了GNN鲁棒性的限制和理解。

为了保护GNNs免受污染攻击，Tang等人（2020）提出了一种通过利用与目标污染图相似的清洁图来传递鲁棒性的方法。他们引入了一种监督知识，可以检测对抗性边缘，并提高GNNs对污染攻击的鲁棒性。

在训练方法方面，Zhu等人（2021）对用于鲁棒表示的深度图结构学习进行了调查。他们讨论了大多数GNN方法对图结构质量的敏感性以及学习鲁棒表示对实际应用的重要性。

其他研究工作探索了不同的策略来增强GNN的鲁棒性。其中包括通过抵抗局部化训练数据限制的位移鲁棒GNN（Zhu等人，20xx）、使用鲁棒统计方法进行鲁棒聚合（Geisler和Zügner，20xx）、用于GNN的可证明鲁棒性和鲁棒训练方法（Zügner和Günnemann，20xx）以及利用加权图拉普拉斯矩阵的鲁棒GNNs（Runwal和Kumar，20xx）。

总之，对GNN鲁棒性的研究旨在开发能够提高GNN模型对抗攻击、结构噪声和输入数据其他形式扰动的可靠性和韧性的技术。提到的工作为实现鲁棒的GNN提供了宝贵的洞察和解决方案，为该领域的进一步发展开辟了机会。

## 第1批

|英文题目|中文题目翻译|作者|arxiv公开|引用数量|中文摘要翻译|
|--|--|--|--|--|--|
|[Graph structure learning for robust graph neural networks](https://dl.acm.org/doi/pdf/10.1145/3394486.3403049)|鲁棒图神经网络的图结构学习|W Jin, Y Ma, X Liu, X Tang, S Wang… - Proceedings of the 26th…, 2020 - dl.acm.org|False|424|…因此，开发抵御对抗性攻击的稳健算法具有重大意义。本文提出了一种名为Pro-GNN的框架，可以联合学习结构图和稳健图神经网络…|
|Reliable representations make a stronger defender: Unsupervised structure refinement for robust gnn|可靠的表示增强了防御者：稳健图神经网络的无监督结构优化|K Li, Y Liu, X Ao, J Chi, J Feng, H Yang… - Proceedings of the 28th…, 2022 - dl.acm.org|False|19|…由监督GNN学习的表示可能受到…大幅增强了原始GCN的鲁棒性…鲁棒的表示可能是GNN的鲁棒性的关键…|
|How robust are graph neural networks to structural noise?|图神经网络对结构噪声的鲁棒性如何？|J Fox, S Rajamanickam - arXiv preprint arXiv:1912.10206, 2019 - arxiv.org|False|23|…然而，对于图神经网络的鲁棒性还不够理解。在…GNN模型 可以实现近乎完美的准确性。同时，我们还展示了相同的GNN模型在…|
|Transferring robustness for graph neural network against poisoning attacks|图神经网络抵御毒化攻击的鲁棒性转移|X Tang, Y Li, Y Sun, H Yao, P Mitra… - Proceedings of the 13th…, 2020 - dl.acm.org|True|128|…图神经网络（GNNs）广泛应用于许多应用中。然而，它们对抵抗对抗性攻击的鲁棒性受到批评。先前的研究表明，对图拓扑或节点特征进行微不可察觉的修改可以显著降低GNN的性能。设计鲁棒的图神经网络来抵御毒化攻击非常具有挑战性，并且已经进行了一些努力。现有的工作仅通过受毒化图中的毒化边缘减少负面影响，这是次优的，因为它们无法将对抗性边缘与正常边缘区分开来。另一方面，在现实世界中，通常可以获得类似目标毒化图的干净图。通过扰动这些干净图，我们创建有监督的知识以训练检测对抗性边缘的能力，从而提高GNN的鲁棒性。然而，现有工作忽视了这些干净图的潜力。因此，我们研究了通过探索干净图来提高GNN抵御毒化攻击的鲁棒性的新问题。具体而言，我们提出了PA-GNN，它依靠一种惩罚聚集机制，通过将较低的注意系数分配给对抗性边缘来直接限制负面影响。为了优化暴露在毒化图中的PA-GNN，我们设计了一个元优化算法，通过使用干净图及其对抗性对应物来训练PA-GNN，惩罚扰动，并将此能力转移，从而提高PA-GNN在毒化图上的鲁棒性。在四个真实数据集上的实验结果展示了PA-GNN在图上抵抗毒化攻击的鲁棒性。代码和数据可在此处找到：https://github.com/tangxianfeng/PA-GNN。|
|Deep graph structure learning for robust representations: A survey|鲁棒表示的深度图结构学习：一项调查|Y Zhu, W Xu, J Zhang, Q Liu, S Wu… - arXiv preprint arXiv…, 2021 - researchgate.net|False|116|…大多数GNN方法对图结构的质量非常敏感，并且通常学习鲁棒的表示来解决实际问题。为了提高GNN模型的鲁棒性…|

## 第2批

|英文题目|中文题目翻译|作者|arxiv公开|引用数量|中文摘要翻译|
|--|--|--|--|--|--|
|Shift-robust gnns: Overcoming the limitations of localized graph training data|具有移位鲁棒性的GNN：克服本地图训练数据的限制|Q Zhu, N Ponomareva, J Han…|False|55|...设计了一种鲁棒的GNN（SR-GNN），旨在解决偏见训练数据与图的真实推理分布之间的分布差异。SR-GNN适应GNN...|
|Reliable graph neural networks via robust aggregation|通过鲁棒聚合实现可靠的图神经网络|S Geisler, D Zügner…|True|60|...本研究受到这样一个观察的启发：对图结构进行干扰已被证明极大地降低了图神经网络（GNN）的性能，而传统的防御方法如对抗训练似乎不能提高鲁棒性。我们的方法提出了一种受鲁棒统计学方法启发的鲁棒聚合函数。我们的方法具有最大的中断点，即0.5，这意味着只要节点的对抗边的比例小于50％，聚合的偏差就受到限制。我们的新型聚合函数，Soft Medoid，是Medoid的全可微化推广，非常适合端到端深度学习。通过使用我们的聚合来装备GNN，我们在Cora ML上的结构扰动鲁棒性提升了3倍（Citeseer上提高了5.5倍），对于低度节点的提升达到了8倍。|
|Certifiable robustness and robust training for graph convolutional networks|图卷积网络的可验证鲁棒性和鲁棒训练|D Zügner, S Günnemann|True|140|...最新研究表明，图神经网络（GNN）在图结构和节点属性的对抗攻击方面具有很高的非鲁棒性，使其结果不可靠。我们首次提出了图卷积网络在节点属性扰动方面的可证明（非）鲁棒性方法。我们考虑二元节点属性（例如词袋）的情况以及L<sub>0</sub>有界的扰动。如果使用我们的方法对节点进行了认证，那么在给定攻击模型下，它在任何可能的扰动情况下都可以保持鲁棒性。同样，我们可以证明非鲁棒性。最后，我们提出了一种鲁棒的半监督训练过程，将标记节点和未标记节点一起处理。根据我们的实验评估，我们的方法在显著提高GNN的鲁棒性的同时，对预测准确性的影响很小。|
|Robust graph neural networks using weighted graph laplacian|使用加权图拉普拉斯的鲁棒图神经网络|B Runwal, S Kumar|False|2|...然而，GNN易受输入数据中的噪音和对抗攻击的影响。提出了一种名为加权Laplacian GNN（RWL-GNN）的增强GNN鲁棒性的框架。...|
|Robust optimization as data augmentation for large-scale graphs|强健的优化作为大规模图的数据增强|K Kong, G Li, M Ding, Z Wu, C Zhu|True|34|...数据增强通过扩大训练集来帮助神经网络更好地进行泛化，但如何有效地增强图数据以提高GNN（图神经网络）的性能仍然是一个待解决的问题。虽然大多数现有的图正则化方法都专注于通过添加/删除边来操纵图的拓扑结构，但我们提出了一种通过操纵节点特征以获得更好性能的方法。我们提出了FLAG（Graph上的自由大规模对抗增强），该方法在训练过程中使用基于梯度的对抗扰动迭代地增强节点特征。通过使模型对输入数据的小波动不变，我们的方法有助于模型泛化到分布外样本，并在测试时提升模型性能。FLAG是一种通用的图数据方法，在节点分类、链接预测和图分类任务中都能普遍适用。FLAG还具有高度的灵活性和可扩展性，并且可在任意GNN骨干和大规模数据集上部署。我们通过大量实验和消融研究证明了我们方法的有效性和稳定性。我们还提供了直观的观察结果，以更深入地理解我们方法。|
