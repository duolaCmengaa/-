import download_use_data
import model1
import os

X_train, y_train = download_use_data.load_fashion_mnist('data/fashion', kind='train')
X_test, y_test = download_use_data.load_fashion_mnist('data/fashion', kind='t10k')

# 划分数据集比例
train_ratio = 0.8
validation_ratio = 0.2

# 计算划分的数据数量
total_samples = len(X_train)
train_samples = int(total_samples * train_ratio)

# 划分训练集和验证集
X_train1, y_train1 = X_train[:train_samples], y_train[:train_samples]
X_valid, y_valid = X_train[train_samples:], y_train[train_samples:]


# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构造保存文件的路径（相对于脚本所在的目录）

save_path0 = os.path.join(script_dir, 'result/easy_train_model')
os.makedirs(save_path0, exist_ok=True)

model = model1.Model(hidden_layers=(128, 32), activation=('relu', 'relu', 'softmax'), input_size=784,output_size=10, lambda1=0.0005)

model.train(X_train1, y_train1, X_valid, y_valid, learningrate=0.001, batch_size=32, decay_number=0.999, epochs=7, start_up=200, min_lr=1e-4, save=True, result_dir=save_path0)
