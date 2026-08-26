import torch
w = torch.tensor(10.0, requires_grad=True)

#Learning Rate(学習率)
lr = 0.5

print("---学習開始---")
for epoch in range(10):
    loss = w**2

    loss.backward()
    grad = w.grad

    with torch.no_grad():
        w -= lr * grad

    print(f"Epoch {epoch+1} | 勾配: {grad.item():.2f} | 更新後の重み w: {w.item():2f} | 損失 Loss: {loss.item():.2f}")

    w.grad.zero_()