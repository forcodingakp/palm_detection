# Palm Detection using MediaPipe Hands

This project demonstrates real-time palm and hand landmark detection using OpenCV and MediaPipe Hands.

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- MediaPipe library

Install the required libraries using:
```bash
pip install opencv-python mediapipe
```

## Steps to Run
1. **Initialize MediaPipe Hands**:
   - The `mp.solutions.hands` module detects hands and their landmarks.
   - `mp_drawing` and `mp_drawing_styles` help visualize detected landmarks.

2. **Access Webcam**:
   - Use OpenCV's `cv2.VideoCapture(0)` to access the default webcam.

3. **Process Frames**:
   - Capture frames in BGR format using OpenCV.
   - Convert frames to RGB for compatibility with MediaPipe.
   - Process frames using `hands.process()` to detect hands.

4. **Draw Landmarks**:
   - If hands are detected, landmarks and hand connections are drawn on the frame using `mp_drawing.draw_landmarks`.

5. **Display Output**:
   - Show the processed frames in a window.
   - Press `q` to exit the program.

## How It Works
- MediaPipe Hands detects 21 hand landmarks and connections in real-time.
- The detected hands are visualized using OpenCV.
- The script runs an infinite loop capturing and processing frames until the user presses 'q' to quit.

## Run the Script
Run the script using the command:
```bash
python palm_detection.py
```

## Key Points
- Input: Live webcam video stream.
- Output: Real-time visualization of detected hands with landmarks and connections.

---

Press `q` to close the webcam and exit the program.
