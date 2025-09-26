# 🚗 Parking Detection — Vacant Parking Slot Using YOLO

This repository implements a **parking-slot occupancy detection system** using **YOLO (Ultralytics)**.  
The system detects vehicles in a frame and checks if they overlap with predefined parking-slot regions to classify each slot as **Occupied** or **Vacant**.

---

## ✨ Features
- Vehicle detection using YOLO (custom/fine-tuned weights supported).
- Define parking slots using a JSON configuration file.
- Works on **images**, **videos**, or **live streams**.
- Color-coded results:
  - 🟥 Red = Occupied
  - 🟩 Green = Vacant
- Supports Docker for easy deployment.

---

## 📂 Project Structure

Parking-Detection-Vacant-Parking-slot-Using-yolo/
├── images/ # Sample images / inputs
├── best.pt # Trained YOLO weights (add your own)
├── detect.py # Main detection script
├── requirements.txt # Python dependencies
├── parking_slots.json # Parking-slot coordinates
├── Dockerfile # Container build file
└── README.md # Documentation


---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/patilyash948/Parking-Detection-Vacant-Parking-slot-Using-yolo.git
cd Parking-Detection-Vacant-Parking-slot-Using-yolo

pip install -r requirements.txt

