import cv2
import torch
import torch.nn as nn
from torchvision.models import mobilenet_v3_small
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    class_names = ['arduino', 'razupai', 'stm32']

    print("Loading model...")
    model = mobilenet_v3_small(weights=None)
    num_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(num_features, len(class_names))

    model.load_state_dict(torch.load("parts_classifier_weights.pth", map_location=device, weights_only=True))
    model.to(device)
    model.eval()

    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])

    ])

    cap = cv2.VideoCapture(1)

    print("Starting real-time inference...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        input_tensor = transform(rgb_frame)
        input_batch = input_tensor.unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = model(input_batch)

            probabilities = F.softmax(outputs, dim=1)
            max_prob, predicted_idx = torch.max(probabilities, 1)
            confidence = max_prob.item()
            pred_class = class_names[predicted_idx.item()]

        threshold = 0.80
        if confidence >= threshold:
            display_text = f"Detected: {pred_class} ({confidence*100:.1f}%)"
            print(confidence)
            text_color = (0, 255, 0)
        else:
            display_text = "Detected: Unknown"
            text_color = (0, 0, 255)

        cv2.putText(frame, display_text, (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, text_color, 3, cv2.LINE_AA)

        cv2.imshow("Parts Recognition AI", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()