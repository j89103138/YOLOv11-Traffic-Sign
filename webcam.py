import cv2
from ultralytics import YOLO
import torch

print("CUDA available:", torch.cuda.is_available())  # check GPU CUDA available
print("GPU Name:", torch.cuda.get_device_name(0))   # show GPU name

cap = cv2.VideoCapture(0)  # 0= computer webcam
model = YOLO("yolo11s.pt")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, show=True,device="cuda")  # show results in real time
    if cv2.waitKey(1) & 0xFF == ord('q'):  # you can hold Q to quit
        break

cap.release()
cv2.destroyAllWindows()
