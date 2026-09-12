import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights

from dataset import PartsDataset

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    print("Loading dataset...")

    dataset = PartsDataset(root_dir="dataset")
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=0)
    print(f"Total images: {len(dataset)}, classes: {dataset.class_names}")

    print("Loading MobileNetV3...")
    weights = MobileNet_V3_Small_Weights.DEFAULT
    model = mobilenet_v3_small(weights=weights)

    num_classes = len(dataset.class_names)
    num_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features=num_features, out_features=num_classes)

    model = model.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.0005)

    num_epochs = 10

    print("Starting training...")
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0

        for inputs, labels in dataloader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * inputs.size(0)

        epoch_loss = running_loss / len(dataset)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}")

    print("Saving model weights...")
    torch.save(model.state_dict(), "parts_classifier_weights.pth")
    print("Done!")

if __name__ == "__main__":
    main()