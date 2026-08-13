import math
import time
from collections import deque
import cv2
import numpy as np
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector

# 1. Initialize Camera
cap = cv2.VideoCapture(0)

# 2. Initialize Hand Detector and AI Classifier
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# 3. Settings
offset = 20
imgSize = 300
confidenceThreshold = 0.70  # Requires 70% confidence to confirm gesture

# 4. Gesture Labels
labels = ["Hello", "I love you", "No", "Okay", "Please", "Thank you", "Yes"]

# 5. Prediction History (Smooths last 7 frames to stop text flickering)
prediction_history = deque(maxlen=7)

# 6. FPS Calculation Variable
prev_time = 0

while True:
    success, img = cap.read()
    if not success:
        print("Camera feed unavailable.")
        break

    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    # Calculate and Display Live FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
    prev_time = current_time
    cv2.putText(imgOutput, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Get frame boundaries to safely crop without crashes
        imgHeight, imgWidth, _ = img.shape
        y1 = max(0, y - offset)
        y2 = min(imgHeight, y + h + offset)
        x1 = max(0, x - offset)
        x2 = min(imgWidth, x + w + offset)

        imgCrop = img[y1:y2, x1:x2]

        if imgCrop.size != 0:
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            aspectRatio = h / w

            # Resize and center cropped hand on white canvas
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            # Predict gesture class
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            confidence = prediction[index]

            # Store confident predictions in history queue
            if confidence >= confidenceThreshold:
                prediction_history.append(index)

            # Display result if stable prediction exists
            if len(prediction_history) > 0:
                most_frequent_index = max(set(prediction_history), key=prediction_history.count)
                display_text = f"{labels[most_frequent_index]} ({int(confidence * 100)}%)"

                # Draw Green Box & Text Label
                cv2.rectangle(imgOutput, (x1, y1 - 45), (x1 + 280, y1), (0, 255, 0), cv2.FILLED)
                cv2.putText(imgOutput, display_text, (x1 + 10, y1 - 12), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
                cv2.rectangle(imgOutput, (x1, y1), (x2, y2), (0, 255, 0), 3)
            else:
                # Searching State (Orange box when confidence < 70%)
                cv2.rectangle(imgOutput, (x1, y1), (x2, y2), (0, 165, 255), 2)
                cv2.putText(imgOutput, "Scanning Gesture...", (x1, y1 - 12), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 165, 255), 2)

            # Show cropped hand windows
            cv2.imshow('Hand Crop', imgCrop)
            cv2.imshow('Processed White Input', imgWhite)

    # Main Output Display
    cv2.imshow('Sign Language Detector', imgOutput)

    # Press 'q' or 'Esc' to exit cleanly
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()