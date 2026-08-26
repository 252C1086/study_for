import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

train_x = torch.randn(100, 3, 32, 32)
train_y = torch.randn(0, 2, (100,))
val_x = torch.randn(20, 3, 32, 32)
val_y = torch.randn(0, 2, (20,))

train_loader = DataLoader(TensorDataset(train_x, train_y), batch_size=16, shuffle=True)
val_loader = DataLoader(TensorDataset(val_x, val_y), batch_size=16, shuffle=True)

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, kernel_size=3, padding=1)
        self.bn = nn.BatchNorm2d(8)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2)
        self.fc = nn.Linear(8 * 16 * 16, 2)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(self.relu(self.bn(self.conv(x))))
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        return self.fc(x)

model = SimpleCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=1e-4)

epochs = 5
for epoch in range(epochs):
    model.train()
    train_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    model.eval()
    val_loss = 0.0
    correct = 0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()

val_acc = correct / len(val_loader.dataset) * 100
print(f"Epoch {epoch+1}/{epochs} | Train Loss: {train_loss/len(train_loader):.3f} | Val Loss: {val_loss/len(val_loader):.3f} | Val Acc: {val_acc:.1f}%")