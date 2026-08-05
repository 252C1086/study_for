import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, in_channels):
        super(ResidualBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, in_channels, kernel_size=3, padding=1)
        self.bn = nn.BatchNorm2d(in_channels)
        self.relu = nn.ReLU()

    def forward(self, x):
        identity = x
        out = self.conv(x)
        out = self.bn(out)

        out += identity

        out = self.relu(out)
        return out

x = torch.randn(2, 3, 64, 64)

block = ResidualBlock(in_channels=3)
y = block(x)

print("入力サイズ:", x.shape)
print("出力サイズ:", y.shape)