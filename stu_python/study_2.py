import torch

matrix = torch.ones(3, 3)

vector = torch.tensor([1.0, 2.0, 3.0])

result = matrix + vector
print(result)