# Created by Coder Shiyar | https://github.com/codershiyar | https://codershiyar.com

import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO('yolov8n.pt')

# Initialize webcam
webcam = cv2.VideoCapture(0)

while True:
    # Capture frame from webcam
    ret, frame = webcam.read()

    # Check if frame is captured successfully
    if not ret:
        print("Failed to capture frame")
        break

    # Detect objects in the frame
    results = model.track(frame, conf=0.5, imgsz=480, classes=0)

    # Display total number of detected objects and bounding boxes
    for result in results:
        cv2.putText(frame, f"Total: {len(result.boxes)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('YOLOv8 Object Detection', result.plot())

    # Exit loop if ESC key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release webcam and close OpenCV windows
webcam.release()
cv2.destroyAllWindows()





# For Realsense camera
   # def initialize_realsense():
    #    import pyrealsense2 as rs
    #    pipeline = rs.pipeline()
     #   camera_aconfig = rs.config()
      #  camera_aconfig.enable_stream(rs.stream.depth, *config.DEPTH_CAMERA_RESOLUTION, rs.format.z16, config.DEPTH_CAMERA_FPS)
     #   camera_aconfig.enable_stream(rs.stream.color, *config.COLOR_CAMERA_RESOLUTION, rs.format.bgr8, config.COLOR_CAMERA_FPS)
     #   pipeline.start(camera_aconfig)
      #  return pipeline
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
