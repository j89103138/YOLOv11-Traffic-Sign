from ultralytics import YOLO


if __name__ == '__main__':
    # load your trained .pt
    model = YOLO("runs/detect/train3/weights/best.pt")

    try:
        # use .pt to find data.yaml
        metrics = model.val()
    except Exception as e:
        print(f"Cannot find data.yaml{e}")
        metrics = model.val(data="dataset.yaml")  # manually set up data.yaml path

    print(metrics)

    metrics = model.val()

#    metrics = model.val(data=data_path, split="test")  # set as test folder


