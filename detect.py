from ultralytics import YOLO
import torch

if __name__ == '__main__':

    print("CUDA available:", torch.cuda.is_available())  # check GPU available
    print("GPU Name:", torch.cuda.get_device_name(0))   # show GPU name

    # pretrained YOLOv11 model (s, m, l, x)
    model = YOLO("runs/detect/train3/weights/best.pt").to("cuda")  


# image
#results = model("sample.jpg", show=True , save=True)  


# video
results = model("archive/video.mp4", save=True,device="cuda",stream = True) #stream=true to prevent "Out Of Memory"

# Need these for stream=true feature.Otherwise you can delete it.
for r in results:
   boxes = r.boxes  
   masks = r.masks  
   probs = r.probs  
