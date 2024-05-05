# YOLOv8 Webcam Object Detection

## Repository Name: yolov8-webcam-object-detection

## Description

This repository contains a Python script for real-time object detection using YOLOv8 with a webcam. The script captures live video from the webcam or Intel RealSense Computer Vision, detects objects in the video stream using the YOLOv8 model, and overlays bounding boxes and labels on the detected objects in real-time. Additionally, it provides functionality to save snapshots with detected objects.

The script is designed to be easy to use and customizable, making it suitable for beginners and those interested in experimenting with object detection using YOLOv8.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3
- OpenCV (`pip install opencv-python`)
- Ultralytics (`pip install ultralytics`)
- Pre-trained YOLOv8 model (provide your model path in the script)
- PyRealSense2 (`pip install pyrealsense2`) (optional, for working with RealSense cameras)
- [PyRealSense2](https://github.com/IntelRealSense/librealsense) (optional, for working with RealSense cameras)

## Usage

1. Clone the repository or download the script `app.py`.
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

## Additional Resources

- For training YOLOv8 on a custom dataset, you can use the [Roboflow platform](https://roboflow.com/).
- To learn how to train YOLOv8 on a custom dataset using a Google Colab notebook, refer to [this Colab notebook](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=D2YkphuiaE7_).
- Models: https://docs.ultralytics.com/tasks/detect/#models
## Acknowledgments

- This script is based on Ultralytics' YOLOv5 repository.
- Special thanks to the Ultralytics team for their excellent work on YOLOv8 and other object detection models.
