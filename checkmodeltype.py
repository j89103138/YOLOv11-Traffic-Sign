from ultralytics import YOLO

if __name__ == '__main__':
    # load your .pt model
    model = YOLO("runs/detect/train/weights/best.pt")  # example: best.pt 

    # check model type
    print(type(model.model))
