<div align="center">

# 计算机视觉第一次作业

李波

21307110183



</div>

## 任务描述：

手工搭建三层神经网络分类器，在数据集[Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist)上进行训练以实现图像分类。

## 准备:

因为download_use_data.py代码会自动前往https://github.com/zalandoresearch/fashion-mnist下载数据集，所以不需要提前下载数据集。
我们只需要下载.py文件和result文件夹内的best_model文件夹内的模型权重和保存的loss，accuracy文件就可以正常完成模型的训练和测试部分。其中，模型权重我还存放到了网盘https://drive.google.com/drive/folders/1EkDHokPg4ViE_z0RDXWBO-efSWoAT9Pt?usp=drive_link，需要可以自行下载

## 文件存放:

2. 使用列表项来表示每个文件或目录：

```plaintext
- Para_seeking.py
- readme.md
- report.pdf
- router.py
- 可视化.ipynb
- MNIST
  - param.npz
  - plotinfo.npz
  - record.txt
  - testset.npz
  - trainset.npz
- package
  - draw.py
  - net.py
  - parameter.py
  - __init__.py
  - layers
    - activation.py
    - batchnorm.py
    - dropout.py
    - layer.py
    - linear.py
    - __init__.py
  - loss
    - celoss.py
    - mseloss.py
    - __init__.py
  - optim
    - momentum.py
    - rmsprop.py
    - sgd.py
    - __init__.py


## 模型训练部分：
我实现了一个具有两层隐藏层的三层神经网络

运行easy_train可以进行简单的训练，可以自定义隐藏层大小(hidden_layers)、激活函数类型(activation)，学习率(learningrate)，正则化强度(lambda1)，除此之外，还有一些其他的参数可以自定义，比如batch_size等等。运行后产生的模型权重,loss,accuracy会自动保存到easy_train_model文件夹内

## 参数查找部分：

运行find_best_model.py文件可以在候选的一些学习率、隐藏层大小、正则化强度超参数中进行训练，找到各自最好的值。

## 测试部分：

下载好文件夹best_model以及里面存放的文件模型权重部分(model.npy)，训练集loss(trainloss.json)，验证集loss(validlosses.json)，以及验证集的准确率(val_accuracy.json)，并将best_model文件夹放到result文件夹里面，最后运行test1.py就可以得到训练集准确率，验证集准确率和测试集准确率。

