import torch
from torch.utils.data import Dataset, DataLoader

class MyCustomDataset(Dataset):
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        path = self.file_paths[idx]

        img_tensor = torch.randn(3, 224, 224)
        label = 0

        return img_tensor, label

def main():
    dummy_paths = [f"image_{i}.jpg" for i in range(10000)]
    dataset = MyCustomDataset(dummy_paths)
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        shuffle=True,
        num_workers=4
    )
    print("---データ読み込みテスト---")

    for batch_idx, (images, labels) in enumerate(dataloader):
        print(f"Batch {batch_idx+1} | 画像テンソル形状: {images.shape} | ラベル形状: {labels.shape}")

        if batch_idx == 0:
            break

if __name__ == "__main__":
    main()