

🤟 American Sign Language (ASL) Real-Time Detector

An AI-powered computer vision application that detects, interprets, and displays
American Sign Language (ASL) hand gestures in real time using a standard webcam.

2. Project Overview

Communication between hearing-impaired individuals and non-signers can often be
challenging. This project aims to solve that problem by providing a real-time
sign language interpreter using artificial intelligence and computer vision.

The system tracks hand movements, crops and centers the hand image, passes it
through a deep learning classification model, and displays the predicted phrase
on screen instantly.

3. Project Objective

  - Build a lightweight, real-time computer vision system capable of recognizing
    sign language gestures.
  - Create a custom dataset collection tool with auto-recording features.
  - Implement prediction smoothing and confidence filtering to eliminate label
    flickering on live camera feeds.

4. Key Features

  - Interactive Data Collection Studio: Automatically manages gesture folders,
    features on-screen HUD counters, and provides auto-capture burst recording.
  - Real-Time Detection: Recognizes gestures at ~30 FPS with live confidence
    scores.
  - Anti-Flicker Prediction Smoothing: Uses a 7-frame history buffer so
    on-screen text stays steady even if your hand shakes.
  - Safe Border Bounds Protection: Automatically handles hand movements near
    screen edges to prevent camera crashes.
  - Live Performance Metrics: Displays real-time FPS (Frames Per Second)
    indicators.

5. Technologies Used

  - Programming Language: Python 3.10
  - Computer Vision: OpenCV (opencv-python)
  - Hand Tracking: MediaPipe & CVZone (cvzone)
  - Deep Learning Framework: TensorFlow 2.15.0 & Keras 2.15.0
  - Data & Image Processing: NumPy & Math

6. Dataset

The project uses a custom dataset collected across 7 common gestures:

  - Classes: "Hello", "I love you", "No", "Okay", "Please", "Thank you", "Yes"
  - Image Resolution: 300x300 pixels (centered on a white canvas)
  - Dataset Size: 200+ images per gesture captured across various lighting
    conditions and hand angles.


1.  Detection: OpenCV reads the video stream, and MediaPipe detects the 21
    keypoints of the hand.
2.  Preprocessing: The hand is cropped, aspect-ratio scaled, and centered on a
    clean 300x300 white background.
3.  Classification: The preprocessed image is fed into a trained
    TensorFlow/Keras neural network.
4.  Display: The system verifies confidence (>70%) and smooths predictions over
    recent frames before displaying the result on screen.


9. Installation

Prerequisites:

  - Installed Python 3.10

AND RUN
    python -m pip install -r requirements.txt

10. How to Run

Step 1: Collect Custom Data (Optional)

To add new signs or expand your dataset, run:

python datacollection.py

  - Controls:
      - S: Save single image
      - SPACE: Toggle Auto-Capture Burst Mode
      - N: Cycle to Next Gesture
      - 1 - 7: Select Gesture directly
      - Q: Exit

Step 2: Run Real-Time Detection

To start live gesture detection:

python test.py

  - Press Q or ESC to close the program.

11. Results / Output

  - Real-time gesture identification with high accuracy (>90% on trained
    gestures).
  - Stable visual feedback displaying the recognized gesture along with live
    prediction confidence percentages.

12. Key Insights / Findings

  - Resolution Matching is Critical: The input resolution used during data
    collection (300x300) must match the inference resolution during testing to
    avoid geometric distortion.
  - Frame Smoothing Improves UX: Averaging predictions over a sliding 7-frame
    buffer drastically improves user experience by preventing label jitter.

13. What I Learned

  - How to build computer vision pipelines using OpenCV and MediaPipe.
  - Preprocessing images for deep learning inference (scaling, aspect-ratio
    preservation, matrix operations).
  - Managing Python environment compatibility (TensorFlow 2.15 vs Keras 3
    deserialization).
  - Building interactive developer tools to streamline dataset creation.

15. Future Improvements

  - Expand Vocabulary: Scale dataset to include the full A-Z ASL alphabet and
    numerical signs.
  - Text-to-Speech (TTS): Integrate audio output so recognized signs are spoken
    aloud.
  - Sentence Formation: Add logic to combine individual gestures into full
    sentences.

16. Credits & Acknowledgements

  - MediaPipe & CVZone: Hand tracking and landmark detection modules.
  - Google Teachable Machine: Deep learning model architecture and training
    framework.


18. Author

  - Aryan Patel

