# 数据分析

## 数值特征之间相关性的子图矩阵

<iframe src="https://www.kaggle.com/embed/igorprikhodko/spaceship-titanic?cellId=44&cellIds=44&kernelSessionId=134169474" height="600" style="margin: 0 auto; width: 100%; max-width: 950px;" frameborder="0" scrolling="auto" title="SPACESHIP TITANIC"></iframe>

<br/>

![16908240622051690824056959.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16908240622051690824056959.png)

## 数据特征编码

## **[引用](：https://www.kaggle.com/code/cjwen0427/mine-dt)**

```python
# 特征编码
index = {} # 创建一个空字典用于存储编码
for column in df.columns:
    if df[column].dtype == 'object' or df[column].dtype == 'bool':
        df[column], index[column] = pd.factorize(df[column], sort=True)
        
# 查看编码的映射关系
for column in df.columns:
    if column in index:
        values = index[column]
        mapping = {value: idx for idx, value in enumerate(values)}
        print(f"{column}:")
        for key, value in mapping.items():
            print(f"{key} --> {value}")
        print()
```

## DT_plot

![16883943819091688394381145.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16883943819091688394381145.png)

![16883944529051688394452556.png](https://fastly.jsdelivr.net/gh/Chenjiangwen/ImageHostingService@main/pic/16883944529051688394452556.png)

```python
# 绘制决策树
class_names = c45_model.classes_.astype(str)  # 将整数数组转换为字符串数组
dot_data = tree.export_graphviz(c45_model, out_file=None, feature_names=X.columns, class_names=class_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")  # 将决策树保存为文件，默认为"decision_tree.pdf"
graph.view()  # 在浏览器中查看决策树
graph.view()
```

## 图片合成拼接

[方法一](https://github.com/Chenjiangwen/wen-mywork/blob/main/12_ComputerVision/ComputerVision.ipynb)

[方法二](https://www.douyin.com/video/7252617616676621603)：python中 import  ==stitching==

数据生成器

## 数据生成器在以下情况下非常有用：

内存限制：当数据集过大无法一次性加载到内存中时，使用数据生成器可以将数据按批次动态加载，避免内存溢出的问题。

实时数据增强：数据生成器可以在每个训练批次中对图像进行实时的数据增强操作，如随机旋转、平移、缩放、翻转等操作，增加了数据的多样性，提高了模型的泛化能力。

数据预处理：数据生成器可以在数据输入模型之前对图像进行预处理操作，如缩放到指定大小、归一化、通道转换等，使得数据满足模型的输入要求。

混洗和重复：数据生成器可以对数据进行混洗操作，打乱样本的顺序，降低模型对训练数据的记忆性；还可以设置重复次数，提供多个周期的数据供训练。

多任务学习：如果需要同时处理多个相关任务（如图像分类和目标检测），可以使用数据生成器同时输出多个标签和辅助信息。

<iframe src="https://www.kaggle.com/embed/gpiosenka/efficientnetb0-f1-score-98?cellIds=8&amp;kernelSessionId=132124463" height="500" style="margin: 0 auto; width: 100%; max-width: 950px;" frameborder="0" scrolling="auto" title="EfficientNetB0 F1 score=98%"></iframe>

------

下面创建了两个回调函数`rlronp`和`estop`，并将它们存储在callbacks列表中 

`tf.keras.callbacks.ReduceLROnPlateau：`

- `monitor="val_loss"`：监控的指标是验证集损失（validation loss）。
- `factor=0.4`：学习率调整的因子，当验证集损失停止改善时，当前学习率将乘以该因子。
- `patience=2`：如果在2个训练轮次（epochs）内没有触发学习率调整，则学习率将减小。
- `verbose=1`：打印学习率调整的信息。
  
  这个回调函数会在验证集损失不再改善时降低学习率，以帮助模型更好地收敛到最优解。

`tf.keras.callbacks.EarlyStopping：`

- `monitor="val_loss"`：监控的指标是验证集损失。
- `patience=4`：如果在4个训练轮次内没有触发提前停止条件，则训练将被提前停止。
- `restore_best_weights`=True：当训练提前停止时，回滚到在验证集上得到最佳性能的模型权重。
  
  这个回调函数用于在验证集损失不再改善且超过一定轮次后，提前终止训练，以避免过拟合并保存在验证集上性能最佳的模型权重。

<iframe src="https://www.kaggle.com/embed/gpiosenka/efficientnetb0-f1-score-98?cellIds=10&amp;kernelSessionId=132124463" height="200" style="margin: 0 auto; width: 100%; max-width: 950px;" frameborder="0" scrolling="auto" title="EfficientNetB0 F1 score=98%"></iframe>

<br/>

### 画图

在Jupyter Notebook中希望绘制更大的图形，可以尝试使用%matplotlib inline来设置图形输出为内联模式，并同时调整figure.dpi参数来增加图像的分辨率。这样可以使结果图形更清晰，同时保持与Jupyter Notebook的兼容性。

```python
%matplotlib inline
plt.rcParams['figure.dpi'] = 250
```