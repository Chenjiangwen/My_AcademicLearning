# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch_geometric.nn import MessagePassing
# from torch_geometric.utils import softmax, add_remaining_self_loops
#
#
# class GATConv(MessagePassing):
#     def __init__(self, in_feats, out_feats, alpha, drop_prob=0.0):
#         super().__init__(aggr="add")
#         self.drop_prob = drop_prob
#         self.lin = nn.Linear(in_feats, out_feats, bias=False)
#         self.a = nn.Parameter(torch.zeros(size=(2*out_feats, 1)))
#         self.leakrelu = nn.LeakyReLU(alpha)
#         nn.init.xavier_uniform_(self.a)
#
#     def forward(self, x, edge_index):
#         edge_index, _ = add_remaining_self_loops(edge_index)
#         # 计算 Wh
#         h = self.lin(x)
#         # 启动消息传播
#         h_prime = self.propagate(edge_index, x=h)
#         return h_prime
#
#     def message(self, x_i, x_j, edge_index_i):
#         # 计算a(Wh_i || wh_j)
#         e = torch.matmul((torch.cat([x_i, x_j], dim=-1)), self.a)
#         e = self.leakrelu(e)
#         alpha = softmax(e, edge_index_i)
#         alpha = F.dropout(alpha, self.drop_prob, self.training)
#         return x_j * alpha
#
#
# if __name__ == "__main__":
#     conv = GATConv(in_feats=3, out_feats=3, alpha=0.2)
#     x = torch.rand(4, 3)
#     edge_index = torch.tensor(
#         [[0, 1, 1, 2, 0, 2, 0, 3], [1, 0, 2, 1, 2, 0, 3, 0]], dtype=torch.long)
#     x = conv(x, edge_index)
#     print(x.shape)

# import torch
# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Visualization function for NX graph or PyTorch tensor
# def visualize(h, color, epoch=None, loss=None):
#     plt.figure(figsize=(7,7))
#     plt.xticks([])
#     plt.yticks([])
#
#     if torch.is_tensor(h):
#         h = h.detach().cpu().numpy()
#         plt.scatter(h[:, 0], h[:, 1], s=140, c=color, cmap="Set2")
#         if epoch is not None and loss is not None:
#             plt.xlabel(f'Epoch: {epoch}, Loss: {loss.item():.4f}', fontsize=16)
#     else:
#         nx.draw_networkx(G, pos=nx.spring_layout(G, seed=42), with_labels=False,
#                          node_color=color, cmap="Set2")
#     plt.show()
#
# # 导入空手道俱乐部数据集
# from torch_geometric.datasets import KarateClub
# dataset = KarateClub()
# print("================================================")
# print(f'Dataset: {dataset}:')
# print('======================')
# print(f'Number of graphs: {len(dataset)}')
# print(f'Number of features: {dataset.num_features}')
# print(f'Number of classes: {dataset.num_classes}')
# print("================================================")
#
# data = dataset[0]  # Get the first graph object.
#
# print(data)
# print('==============================================================')
#
# # Gather some statistics about the graph.
# print(f'Number of nodes: {data.num_nodes}') # 节点的个数
# print(f'Number of edges: {data.num_edges}') # 边的个属于
# print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}') # 节点的度平均数
# print(f'Number of training nodes: {data.train_mask.sum()}')
# print(f'Training node label rate: {int(data.train_mask.sum()) / data.num_nodes:.2f}')
# print(f'Contains isolated nodes: {data.contains_isolated_nodes()}')
# print(f'Contains self-loops: {data.contains_self_loops()}')
# print(f'Is undirected: {data.is_undirected()}')
#
# edge_index = data.edge_index
# # 打印节点
# # print(edge_index.t())
#
# from torch_geometric.utils import to_networkx
#
# G = to_networkx(data, to_undirected=True)
# visualize(G, color=data.y)

import numpy as np
import matplotlib.pyplot as plt

data = {
    'gcm_lm': (0.7140, 65),
    'gin': (0.7026, 77),
    'graphsage': (0.7074, 71),
    'rgcn': (0.7089, 156),
    'sgcn': (0.7170, 121),
    'tagcn': (0.7217, 244),
    # 'appnp': (0, 0)  # 将准确率和时间设为NaN
}

accuracies = [data[model][0] for model in data.keys()]
times = [data[model][1]/60 for model in data.keys()]  # 将时间从秒转换为分钟

models = list(data.keys())

fig, ax = plt.subplots()

bar_width = 0.35
index = np.arange(len(models))

rects1 = ax.bar(index, accuracies, bar_width, color='b', label='ACC')
ax.set_ylabel('ACC')
ax.set_xticks(index)
ax.set_xticklabels(models)
ax.legend(['ACC'], loc='upper left')

ax2 = ax.twinx()
rects2 = ax2.bar(index + bar_width, times, bar_width, color='r', alpha=0.6, label='时间')
ax2.set_ylabel('time(h)')
ax2.legend(['time'], loc='upper right')

plt.title('7 representative defense models & time')

max_value = max(accuracies)
# max_value = max(max(accuracies), max(times))
ax.set_ylim(0, 1.6 * max_value)  # 调整y轴范围


plt.xticks(index + bar_width/2, models)
plt.show()

print(np.mean(accuracies),np.sum(times))