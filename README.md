<div align="center">

# 计算机视觉第一次作业

李波

21307110183



</div>

## 任务描述：

手工搭建三层神经网络分类器，在数据集[Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist)上进行训练以实现图像分类。

## 准备:

因为download_use_data.py代码会自动前往https://github.com/zalandoresearch/fashion-mnist
下载数据集，所以不需要提前下载数据集。
我们只需要下载.py文件和result文件夹内的best_model文件夹内的模型权重和保存的loss，accuracy，learingrates的json文件就可以正常完成模型的训练，测试绘图部分。其中，模型权重我还存放到了网盘https://drive.google.com/drive/folders/1EkDHokPg4ViE_z0RDXWBO-efSWoAT9Pt?usp=drive_link
，需要可以自行下载

## 文件存放目录结构:

```plaintext
- data
  - fashion
- download_use_data.py
- easy_train.py
- find_best_model.py
- function1.py
- model1.py
- plot_loss_accuracy.py
- test1.py
- visualization_parameters.py
- result
  - best_model
    - model.npy
    - trainloss.json
    - val_accuracy.json
    - validlosses.json
    - learningrates.json
  - easy_train_model
    - model.npy
    - trainloss.json
    - val_accuracy.json
    - validlosses.json
    - learningrates.json
  - pictures
    - find_best_learning_rate.png
    - find_best_regularization_parameter.png
    - find_hidden0_accuracy.png
    - find_hidden1_accuracy.png
    - test_accuracy.png
    - trainloss.png
    - validloss.png
    - learningrates.png
    - orign.png
    - layer1_biases_histogram.png
    - layer1_weights_histogram.png
    - layer1_weights_visualization.png
    - layer2_biases_histogram.png
    - layer2_weights_histogram.png
    - layer3_biases_histogram.png
    - layer3_weights_histogram.png
```

## 模型训练部分：
我实现了一个具有两层隐藏层的三层神经网络

直接运行easy_train可以进行简单的训练，可以自定义隐藏层大小(hidden_layers)、激活函数类型(activation)，学习率(learningrate)，正则化强度(lambda1)，除此之外，还有一些其他的参数可以自定义，比如batch_size等等。运行后产生的模型权重,loss,accuracy,learningrates会自动保存到easy_train_model文件夹内，文件夹会自动生成，不需要手动进行创建，下面同理。

## 参数查找部分：

直接运行find_best_model.py文件可以在候选的一些学习率、两层隐藏层大小、正则化强度，激活函数类型等超参数中进行训练，找到最优的超参数。找到各自的最好的超参数后会自动进行训练，会将权重文件保存到result文件夹内的best_model。

## 测试部分：

下载好文件夹best_model以及里面存放的文件模型权重部分(model.npy)，训练集loss(trainloss.json)，验证集loss(validlosses.json)，记录的学习率(learningrates.json)以及验证集的准确率(val_accuracy.json)，并将best_model文件夹放到result文件夹里面，最后运行test1.py就可以得到训练集准确率，验证集准确率和测试集准确率。

## 绘制loss曲线和accuracy曲线部分：
下载好测试部分所下载的文件，并放到正确的路径，直接运行plot_loss_accuracy.py即可，图片会自动保存到result文件夹内的pictures文件夹内。

## 模型网络参数的可视化部分：
下载好模型权重部分(model.npy),放置到正确的路径，直接运行visualization_parameters.py即可，图片会自动保存到result文件夹内的pictures文件夹内。

## 其他的文件说明：
function1.py包含了定义的一些模型所需要的基本函数

model1.py是模型的基本结构

