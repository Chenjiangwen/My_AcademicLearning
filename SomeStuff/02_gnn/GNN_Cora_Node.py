import torch
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
from torch_geometric.nn import GCNConv

'''
Cora数据集是PyG内置的节点分类数据集，代表着学术论文的相关性分类问题（即把每一篇学术论文都看成是节点），
Cora数据集有2708个节点，1433维特征，边数为5429。标签是文献的主题，共计 7 个类别。所以这是一个7分类问题。
'''
#载入数据
dataset = Planetoid(root='~/tmp/Cora', name='Cora')
data = dataset[0]
#定义网络架构
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = GCNConv(dataset.num_features, 16)  #输入=节点特征维度，16是中间隐藏神经元个数
        self.conv2 = GCNConv(16, dataset.num_classes)
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Net().to(device)
data = data.to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
#模型训练
model.train()
for epoch in range(200):
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)    #模型的输入有节点特征还有边特征,使用的是全部数据
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])   #损失仅仅计算的是训练集的损失
    loss.backward()
    optimizer.step()
#测试：
model.eval()
test_predict = model(data.x, data.edge_index)[data.test_mask]
max_index = torch.argmax(test_predict, dim=1)
test_true = data.y[data.test_mask]
correct = 0
for i in range(len(max_index)):
    if max_index[i] == test_true[i]:
        correct += 1
print('测试集准确率为：{}%'.format(correct*100/len(test_true)))

