import torch

x = torch.tensor(2.0, requires_grad=True)

y = 3 * x**2 + 2 * x

print("yの値:", y.item())
print("yの計算ノード(grad_fn):", y.grad_fn)

y.backward()

print("xの勾配(dy/dx):", x.grad.item())