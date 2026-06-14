from ultralytics import YOLO
import cv2

# 1. Load the "Brain"
model = YOLO('yolov8n.pt')

# 2. Open the video
cap = cv2.VideoCapture(r"C:\Users\chinm\OneDrive\Desktop\CivicEye\test_video.mp4.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 3. AI Inference: The "Brain" looks at the frame
    results = model(frame)

    # 4. Logic: Check the 80% threshold
    for r in results:
        boxes = r.boxes
        for box in boxes:
            confidence = box.conf[0]
            if confidence > 0.8:
                print("ALERT: Object detected with high confidence!")
                # This print statement will appear in your terminal!

    # 5. Show the video with the boxes drawn by the AI
    annotated_frame = results[0].plot()
    cv2.imshow("Civic Eye Monitor", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

