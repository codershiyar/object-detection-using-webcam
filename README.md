# YOLOv8 Webcam Object Detection

## Repository Name: yolov8-webcam-object-detection

## Description

This repository contains a Python script for real-time object detection using YOLOv8 with a webcam. The script captures live video from the webcam, detects objects in the video stream using the YOLOv8 model, and overlays bounding boxes and labels on the detected objects in real-time. Additionally, it provides functionality to save snapshots with detected objects.

The script is designed to be easy to use and customizable, making it suitable for beginners and those interested in experimenting with object detection using YOLOv8.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3
- OpenCV (`pip install opencv-python`)
- Ultralytics (`pip install ultralytics`)
- Pre-trained YOLOv8 model (provide your model path in the script)

## Usage

1. Clone the repository or download the script `yolov8.py`.
2. Install the required dependencies.
3. Make sure you have a pre-trained YOLOv8 model (`.pt` file) and provide its path in the script.
4. Run the script using the following command:
python yolov8.py

5. The webcam will activate, and you'll see live video with object detection overlays.
6. Press 's' to save a snapshot with detected objects.
7. Press 'ESC' to exit the program.

## Customization

- You can adjust the confidence threshold, NMS threshold, and input resolution in the `load_model()` function.
- Modify the `save_image()` function to customize the save directory or filename format.

## Acknowledgments

- This script is based on Ultralytics' YOLOv8 repository.
- Special thanks to the Ultralytics team for their excellent work on YOLOv8 and other object detection models.
