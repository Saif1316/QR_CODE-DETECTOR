# QR_CODE-DETECTOR
This Computer vision model uses object Detection to Identify qr_code in the Images


# 1. Introduction

# 1.1 Project Objective

The goal of this project, undertaken as part of the Pixonates Lab Internship, was to develop an object detection model to identify QR codes in images using the YOLOv8 (You Only Look Once) framework by Ultralytics. The model was trained on a custom dataset of 80 images, aiming to achieve high accuracy for QR code localization and classification, with potential applications in automated scanning systems.

# 1.2 Tools and Technologies
Framework: Ultralytics YOLOv8.3.149
Programming Language: Python 3.10.6
Hardware: CPU (AMD Ryzen 5 5600H with Radeon Graphics)
Libraries: ultralytics, sklearn, shutil, pathlib
Environment: Windows, PyCharm, OneDrive-synced project directory
Dataset Directory: C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/data

# 2. Dataset Preparation

# 2.1 Data Collection
# The dataset comprised 80 images containing QR codes, stored in: C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/images-qr-detect/images

Corresponding annotations in YOLO format (.txt files with class ID, normalized bounding box coordinates) were stored in:C:/Users/Saif/OneDrive/Pictures/Desktop/YOLO_Format
Each annotation included two classes:
Class 0: qr_code

# 2.2 Data spliting
The dataset was split into training (70%), validation (15%), and test (15%) sets using train_val_test_split.py (artifact version ID df8bc057-ee50-46b6-911a-de42f30a1f96):
Train: 56 images
Val: 12 images
Test: 12 images
The script:
1.Loaded images from .../images-qr-detect/images and labels from .../YOLO_Format.
2.Used sklearn.model_selection.train_test_split with random_state=42 for reproducibility.
3.Created directories:C:/Users/Saif/OneDrive/Pictures/Desktop/Pixonates lab Internship project/data/
├── Images/
│   ├── train/ (56 .jpg)
│   ├── val/   (12 .jpg)
│   ├── test/  (12 .jpg)
├── Labels/
│   ├── train/ (56 .txt)
│   ├── val/   (12 .txt)
│   ├── test/  (12 .txt)
4.Copied images and .txt files to respective splits, ensuring matching filenames.

# 2.3 Data Configuration
A data.yaml was created to configure the dataset for YOLOv8:
# path: C:\Users\Saif\OneDrive\Pictures\Desktop\Pixonates lab Internship project\data
# train: Images\train
# val: Images\val
# test: Images\test
# nc: 2
# names:
#  0: qr_code

# 3. Model Training
  # 3.1 Model Selection
  The YOLOv8 nano model (yolov8n.pt) was chosen for its balance of speed and accuracy, suitable for CPU-based training on a small dataset. The model was loaded with pre-trained weights from Ultralytics.

  # 3.2 Training Script
  The training was performed using model.py
  # Configuration:
    data: .../data/data.yaml
    epochs: 50
    imgsz: 640
    batch: 8
    name: qr_code_train
  # Steps:
  Verified dataset structure (56/12/12 images and labels). 
  Trained model for 50 epochs.
  Evaluated on validation and test sets).

  # 3.3 Training environment
  # Hardware: CPU (AMD Ryzen 5 5600H), no GPU acceleration.
  # Software: Python 3.10.6, Ultralytics 8.3.149, torch 2.7.0+cpu.
  # Output: Results saved to runs/detect/qr_code_train73.

# 4. Model Evaluation
  # 4.1 Metrics
  The model was evaluated on the test set (12 images) using the following metrics:
  # a. Mean Average Precision (mAP)
  Test mAP@0.5:0.95: 0.5679 (56.79%)
  Description: mAP measures the average precision across IoU thresholds (0.5 to 0.95), reflecting both detection accuracy and bounding box localization. Precision = TP / (TP + FP), Recall = TP / (TP + FN). For qr_code, mAP = AP of QR       code detection.
  Interpretation: A test mAP of 56.79% indicates moderate performance. The model detects QR codes in ~57% of cases with reasonable localization but may miss some QR codes or detect false positives. The small dataset size (80 images) and    CPU training with yolov8n.pt limit accuracy.
  # b. Speed Metrics
  Preprocess: 4.7ms per image (resizing, normalization)
  Inference: 106.4ms per image (~9.4 FPS)
  Postprocess: 14.2ms per image (NMS, bounding box filtering)
  Total: 125.3ms per image (~8 FPS)
  Description: Inference speed measures the time to process an image. Preprocess prepares images, inference runs the model, and postprocess filters predictions.
  Interpretation: ~8 FPS is suitable for offline processing but too slow for real-time QR code scanning (ideal: 30 FPS). CPU limitations and imgsz=640 contribute to the speed.

# 5.Conclusion
The project successfully implemented a YOLOv8-based QR code detection model, achieving a test mAP of 56.79% and a processing speed of ~8 FPS on a CPU. Despite challenges with dataset paths and small data size, the model demonstrates moderate performance suitable for offline processing. Future work includes expanding the dataset,class, and optimizing for real-time applications.
