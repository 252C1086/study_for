import torch
import torch.nn as nn

torch.manual_seed(42)

N = 4       #データ数
D_in = 3    #入力次元
D_out = 2   #出力次元

X = torch.randn(N, D_in)    #4*3行列の入力データ

#nn.linearによる計算
linear_layer = nn.Linear(in_features=D_in, out_features=D_out)
relu = nn.ReLU()

#順伝播, 線形変換してからReLUを通す
y_pytorch = relu(linear_layer(X))

#行列計算の手動バージョン
W = linear_layer.weight.T
b = linear_layer.bias

y_manual = torch.matmul(X, W) + b

#ReLU処理の手動化(0より小さい要素を0に統一)
y_manual_relu = torch.maximum(y_manual, torch.tensor(0.0))


print("--- PyTorch API (nn.Linear + ReLU) による実行結果 ---")
print(y_pytorch)

print("\n--- 手動の行列計算(XW + b) + 手動ReLU による実行結果")
print(y_manual_relu)

print("\n両者は完全に一致しているか？:", torch.allclose(y_pytorch, y_manual_relu))