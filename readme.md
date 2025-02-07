# 🚀 YOLOv11: Local Training on Traffic Sign Dataset with CUDA Acceleration  

High-performance and accurate **traffic sign detection** using **YOLOv11**, supporting **real-time image & video processing** with **CUDA acceleration**. Train locally using **Kaggle's Traffic Sign dataset** and **fine-tune with YOLOv11s.pt pre-trained model**.  

![YOLOv11 Detection](https://github.com/yourusername/yourproject/raw/main/demo.gif)

---

## ✨ Features  
✔️ **Train & Test on Traffic Sign Dataset** (Kaggle)  
✔️ **Real-time Image & Video Detection**  
✔️ **CUDA Accelerated Inference**  
✔️ **AMP (Automatic Mixed Precision) Enabled**  
✔️ **TensorRT Optimization (In Development 🚧)**  

---

## 📦 Installation  

Ensure you have **Python 3.8+**, **PyTorch**, and **CUDA 11.0+** installed.  

```sh
# Clone the repository
git clone https://github.com/yourusername/yourproject.git
cd yourproject

# Install dependencies
pip install -r requirements.txt
```

---

## 🔧 Usage  

### 🏋️ Train a New Model  
If you want to train the model from scratch using the **Traffic Sign Dataset**, run:  

```sh
python train.py --data dataset.yaml --cfg yolov11.yaml --weights yolov11s.pt --device 0
```

### 📊 Validate Model Performance  
To evaluate the trained model on the validation dataset, run:  

```sh
python val.py --weights runs/train/exp/weights/best.pt --data dataset.yaml
```

### 🎥 Image & Video Detection  
Run YOLOv11 on images or videos:  

```sh
python detect.py --source sample.jpg --weights best.pt --conf 0.5 --device 0
```

For **live webcam detection**, use:  

```sh
python webcam.py --weights best.pt --conf 0.5 --device 0
```

---

## ⚙️ Project Structure  

```
📂 YOLOv11-Traffic-Sign
 ┣ 📂 models/           # YOLO model config
 ┣ 📂 datasets/         # Traffic sign dataset
 ┣ 📂 utils/            # Utility functions
 ┣ 📄 train.py          # Training script
 ┣ 📄 val.py            # Validation script
 ┣ 📄 detect.py         # Inference on images/videos
 ┣ 📄 webcam.py         # Live webcam detection
 ┣ 📄 README.md         # Project documentation
 ┗ 📄 LICENSE           # MIT License
```

---

## 🤝 Contributing  

We welcome contributions! To contribute, follow these steps:  

1. **Fork the repo**  
2. **Create a new branch** (`git checkout -b feature-xxx`)  
3. **Commit changes** (`git commit -m "Add new feature"`)  
4. **Push to GitHub** (`git push origin feature-xxx`)  
5. **Submit a Pull Request**  

---

## 📜 License  

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## 📬 Contact  

📧 Email: [j89103138@gmail.com](mailto:j89103138@gmail.com)  
🌐 GitHub: [github.com/j89103138](https://github.com/j89103138)  
```