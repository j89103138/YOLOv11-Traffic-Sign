import pandas as pd

# Load the CSV file
df = pd.read_csv("runs/detect/train2/results.csv")

def print_epochs():
    total_epochs = len(df)  # Get the number of epochs trained
    print("\n📊 Training Epochs Summary:")
    print(f"✅ Total Epochs Trained: {total_epochs}")

def print_training_time():

    if "epoch" not in df.columns or "time" not in df.columns:
        print("\n⚠️ 'epoch' or 'time' column not found. Please check the CSV structure!")
        return

    total_time = df["time"].iloc[-1]  # Take only the last recorded time
    print("\n⏳ Training Time Summary:")
    print(f"✅ Total Training Time: {total_time:.2f} seconds")
    print(f"✅ Converted to minutes: {total_time / 60:.2f} minutes")
    print(f"✅ Converted to hours: {total_time / 3600:.2f} hours")

def print_benchmark_summary():
    print_epochs()
    print_training_time()

#  Choose which function to call
if __name__ == "__main__":
    print_benchmark_summary()  # Display both 
