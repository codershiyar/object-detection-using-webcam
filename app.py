import cv2
import numpy as np
import os
from datetime import datetime
from ultralytics import YOLO

# Function to initialize webcam
def initialize_webcam():
    return cv2.VideoCapture(0)


# Load YOLOv8 model with options
def load_model():
    return YOLO('model_buckets_with_handlesv14n.pt')

    
# Function to detect objects using YOLOv8
def detect_objects(model, image):
    # Example options (adjust as needed)
    options = {
        'conf': 0.5,          # Confidence threshold
        'iou': 0.4,           # NMS threshold
        'imgsz': 640,      # Model input resolution
    }
    results = model.track(image, **options)

    return results

# Function to save image
def save_image(image, directory='captures'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '_detected.jpg'
    filepath = os.path.join(directory, filename)
    cv2.imwrite(filepath, image)
    print("Image saved as:", filepath)

# Main function
def main():
    # Load YOLOv8 model
    yolo_model = load_model()

    # Initialize webcam
    webcam = initialize_webcam()

    # Main loop
    while True:
        # Capture frame from webcam
        ret, frame = webcam.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Detect objects in the frame
        results = detect_objects(yolo_model, frame)

        # Draw bounding boxes and labels
        for result in results:
                cv2.putText(frame, f"Total:{len(result.boxes)}" , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('YOLOv8 Object Detection', results[0].plot())

        # Check for user input
        key = cv2.waitKey(1)
        if key == ord('s'):
            save_image(frame)  # Save image when 's' key is pressed
        elif key == 27:  # ESC key
            break

    # Release resources
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()







# try:
#     # Try to initialize RealSense Camera
#     camera = initialize_realsense()
#     get_frame = get_frame_realsense
# except Exception as e:
#     print("RealSense camera not found, using default webcam.")
#     camera = initialize_webcam()
#     get_frame = get_frame_webcam

# Function to get frames from RealSense
# def get_frame_realsense(pipeline):
#     import pyrealsense2 as rs
#     frames = pipeline.wait_for_frames()
#     depth_frame = frames.get_depth_frame()
#     color_frame = frames.get_color_frame()
#     if not depth_frame or not color_frame:
#         return None, None
#     depth_image = np.asanyarray(depth_frame.get_data())
#     color_image = np.asanyarray(color_frame.get_data())
#     return depth_image, color_image

# # Function to get frame from webcam
# def get_frame_webcam(cap):
#     ret, frame = cap.read()
#     return None, frame if ret else None