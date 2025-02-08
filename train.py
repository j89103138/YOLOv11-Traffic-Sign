from ultralytics import YOLO
import torch
from pathlib import Path

if __name__ == '__main__':

    data_path = Path("C:/Path_to_your_dataset/archive/car/data.yaml")

    print("CUDA available:", torch.cuda.is_available())  # check GPU CUDA available
    print("GPU Name:", torch.cuda.get_device_name(0))   # show GPU name

    # pretrained YOLOv11 model (s, m, l, x)
    model = YOLO("yolo11s.pt").to("cuda")  

    # train
    model.train(data=data_path, epochs=50 , batch = 8, amp=True ) # if your system don't support amp features, delete it.

