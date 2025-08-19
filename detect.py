from ultralytics import YOLO
import torch
from ultralytics.nn.tasks import DetectionModel  # Import the class for safe loading
import sys
import os

# Allow YOLO DetectionModel to be safely unpickled
torch.serialization.add_safe_globals([DetectionModel])

# Load trained model (path inside container or local)
model = YOLO("best.pt")

# Get folder path from arguments
if len(sys.argv) < 2:
    print("Usage: python detect.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.isdir(folder_path):
    print(f"Error: Folder '{folder_path}' does not exist.")
    sys.exit(1)

# Run predictions
results = model.predict(source=folder_path, save=True, imgsz=640)
print("Predictions saved in:", results[0].save_dir)
