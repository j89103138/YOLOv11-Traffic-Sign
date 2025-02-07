import pandas as pd

df = pd.read_csv("runs/detect/train2/results.csv")

def print_final_epoch():
    final_result = df.iloc[-1]
    print("\nFinal Epoch:")
    print(f"Precision: {final_result['metrics/precision(B)']:.4f}")
    print(f"Recall: {final_result['metrics/recall(B)']:.4f}")
    print(f"mAP@50: {final_result['metrics/mAP50(B)']:.4f}")
    print(f"mAP@50-95: {final_result['metrics/mAP50-95(B)']:.4f}")

def print_best_epoch():
    best_epoch = df["metrics/mAP50-95(B)"].idxmax()  # best epoch
    best_result = df.iloc[best_epoch]  
    print("\nBest Epoch:")
    print(f"Epoch: {best_epoch}")
    print(f"Precision: {best_result['metrics/precision(B)']:.4f}")
    print(f"Recall: {best_result['metrics/recall(B)']:.4f}")
    print(f"mAP@50: {best_result['metrics/mAP50(B)']:.4f}")
    print(f"mAP@50-95: {best_result['metrics/mAP50-95(B)']:.4f}")

def print_summary():
    print_final_epoch()
    print_best_epoch()

#choose
if __name__ == "__main__":
    print_summary()  
    # print_final_epoch()  
    # print_best_epoch()  
