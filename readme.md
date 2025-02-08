# 🚀 YOLOv11: Local Training on Traffic Sign Dataset with CUDA Acceleration  

High-performance and accurate **traffic sign detection** using **YOLOv11**, supporting **real-time image & video processing** with **CUDA acceleration**. Train locally using **Kaggle's Traffic Sign dataset** and **fine-tune with YOLOv11s.pt pre-trained model**.  

![Traffic Sign Detection Gif](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/demo.gif)
![Traffic Sign Detection img](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/demo.jpg)

---

## ✨ Features  
✔️ **Train & Test on Traffic Sign Dataset** (Kaggle)  
✔️ **Real-time Image & Video Detection**  
✔️ **CUDA Accelerated Inference**  
✔️ **AMP (Automatic Mixed Precision) Enabled**  
🚧 **TensorRT Optimization (In Development)**  

---

## 📦 Installation  

Ensure you have **Python**, **PyTorch**, and **CUDA** installed.  
My testing platform : Python 3.10+ , torch 2.6.0+cu126, CUDA 12.8

```sh
# Clone the repository
git clone https://github.com/j89103138/YOLOv11-Traffic-Sign.git
cd YOLOv11-Traffic-Sign

# Install dependencies
pip install -r requirements.txt
```
You can find dataset to download here on Kaggle: 
https://www.kaggle.com/datasets/pkdarabi/cardetection/data

---

## 🔧 Usage  

### 🏋️ Train a New Model  
If you want to train the model from using pretrained yolo model, using the **Traffic Sign Dataset**, run:  

```sh
python train.py
#you have to set some path manually
```

### 📊 Validate Model Performance  
To evaluate the trained model on the validation dataset, run:  

```sh
python val.py
#you have to set some path manually
```

### 🎥 Image & Video Detection  
Run YOLOv11 on images or videos:  

```sh
python detect.py
#you have to set some path manually
```

For **live webcam detection**, use:  

```sh
python webcam.py
#you have to set some path manually
```

---

## ⚙️ Project Structure  

```
📂 YOLOv11-Traffic-Sign
 ┣ 📂 archive              # special thanks Kaggle:pkdarabi 's dataset
 ┣ 📂 assets               #gif and images
 ┣ 📄 train.py             # Training model
 ┣ 📄 val.py               # Validation model
 ┣ 📄 detect.py            # Inference on images/videos
 ┣ 📄 webcam.py            # Live webcam detection
 ┣ 📄 checkmodeltype.py    # check model type ( would be useful if you're on different type of model)
 ┣ 📄 read_results.py      # use pandas for easy summarize model performance
 ┣ 📄 benchmark.py         # for benchmarking by epochs and times
 ┣ 📄 README.md            # Project documentation
 ┗ 📄 LICENSE.md           # License
```

---

## 🔍  Performance Metrics 

![labels](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/labels.jpg)
![F1 curve](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/F1_curve.png)
![PR curve](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/PR_curve.png)
![confusion matrix](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/confusion_matrix.png)
![results](https://github.com/j89103138/YOLOv11-Traffic-Sign/raw/main/assets/results.png)

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

This project is licensed under the **CC BY 4.0 LICENSE**. See [LICENSE](LICENSE.md) for details.  

```
Creative Commons Attribution 4.0 International (CC BY 4.0)

2025 Shawn Liu 

This work is licensed under the Creative Commons Attribution 4.0 International License.
You are free to:
- Share — copy and redistribute the material in any medium or format.
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For more details, see https://creativecommons.org/licenses/by/4.0/
```

---

## 📬 Contact  

📧 Email: [j89103138@gmail.com](mailto:j89103138@gmail.com)  
🌐 GitHub: [github.com/j89103138](https://github.com/j89103138)  
```
