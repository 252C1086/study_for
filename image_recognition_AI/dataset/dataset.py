import os
import glob
import cv2
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
class PartsDataset(Dataset):
    def __init__(self, root_dir):
        self.data_info = []

        self.class_names = sorted(os.listdir(root_dir))

        for label_idx, class_name in enumerate(self.class_names):
            target_path = f"{root_dir}/{class_name}/*.jpg"
            img_paths = glob.glob(target_path)
            for path in img_paths:
                self.data_info.append((path, label_idx))

        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

    def __len__(self):
        return len(self.data_info)

    def __getitem__(self, idx):
        img_path, label = self.data_info[idx]

        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_tensor = self.transform(img)

        return img_tensor, label