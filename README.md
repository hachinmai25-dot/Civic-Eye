# CivicEye: AI-Powered Smart Urban Surveillance

## 🚀 Project Overview
**CivicEye** is an intelligent, real-time computer vision system designed to monitor public infrastructure autonomously. By leveraging edge AI, the system detects objects (such as vehicles, pedestrians, or waste) in video feeds and triggers automated alerts when predefined confidence thresholds are met. This solution is designed to reduce the need for manual surveillance and improve urban maintenance efficiency.

## 🛠 Technical Stack
* **Language:** Python 3.x
* **AI Model:** YOLOv8 (Ultralytics) - Chosen for its high accuracy-to-speed ratio, making it ideal for real-time applications.
* **Computer Vision:** OpenCV (cv2) for frame processing and visualization.
* **Logic Architecture:** Real-time inference pipeline with an 80% confidence thresholding mechanism.

## 🔑 Key Features
* **Real-time Inference:** Processes video streams to identify objects on the fly.
* **Automated Alerting:** Logs high-confidence detections directly to the system terminal, providing a digital audit trail of events.
* **Edge-Ready:** Built with a lightweight model (`yolov8n`), ensuring the system can be deployed on low-power hardware like a Raspberry Pi or other IoT edge devices.
* **Visual Verification:** Generates annotated video output with bounding boxes, allowing for immediate visual verification of detections.

## 🚀 How to Run
1. **Clone this repository:**
```bash
   git clone [https://github.com/hachinmai25-dot/Civic-Eye.git](https://github.com/hachinmai25-dot/Civic-Eye.git)
   cd Civic-Eye
2. **Install dependencies**
```Ensure you have Python installed, then run the following command to install the required AI and Vision libraries:
   Bash
   pip install ultralytics opencv-python
3. **Run the system**
   Make sure your yolov8n.pt model file and test_video.mp4 file are in the project folder, then execute:
```bash
   python civic_eye.py



```Bash
   python civic_eye.py
