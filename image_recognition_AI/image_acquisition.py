import os
import time
import cv2

class_map = {
    ord('1'): "stm32",
    ord('2'): "razupai",
    ord('3'): "arduino"
}

for class_name in class_map.values():
    os.makedirs(f"dataset/{class_name}", exist_ok=True)

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Window", frame)
    key = cv2.waitKey(1) & 0xFF
    current_time = (time.time() * 1000)
    if key in class_map:
        class_name = class_map[key]
        filename = f"dataset/{class_name}/save_{current_time}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    elif key == ord('q'):
        print("Quit")
        break

cap.release()
cv2.destroyAllWindows()