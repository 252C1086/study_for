import torch

x = torch.tensor([[0, 1, 2], [3, 4, 5]])

print("元の形状:", x.shape)
print("元のStride:", x.stride())

y = x.T

print("転置後の形状:", y.shape)
print("転置後のStride", y.stride())