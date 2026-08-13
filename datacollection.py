import math
import os
import time
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# 1. Camera & Hand Detector Setup
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

# 2. Configuration Settings
offset = 20
imgSize = 300  # Matches test.py (300x300)
target_count = 200  # Recommended target images per gesture

# 3. Gestures List
gestures = ["Hello", "I love you", "No", "Okay", "Please", "Thank you", "Yes"]
current_index = 0

# Create root Data folder & subfolders automatically
base_folder = "Data"
os.makedirs(base_folder, exist_ok=True)
for gesture in gestures:
    os.makedirs(os.path.join(base_folder, gesture), exist_ok=True)

# State variables
auto_capture = False
last_capture_time = 0
capture_interval = 0.15  # Auto-captures 1 photo every 0.15s in Auto Mode

print("=" * 50)
print("       SIGN LANGUAGE DATA COLLECTION STUDIO       ")
print("=" * 50)
print(" CONTROLS:")
print("   [S]       : Save single image")
print("   [SPACE]   : Toggle Auto-Capture Mode")
print("   [N]       : Switch to Next Gesture")
print("   [1 - 7]   : Jump directly to Gesture 1-7")
print("   [Q / ESC] : Quit Studio")
print("=" * 50)

while True:
    success, img = cap.read()
    if not success:
        print("Camera feed unavailable.")
        break

    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    # Active Gesture & Save Directory
    current_gesture = gestures[current_index]
    save_directory = os.path.join(base_folder, current_gesture)
    saved_count = len(os.listdir(save_directory))

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Safe border boundaries to avoid out-of-frame crashes
        imgHeight, imgWidth, _ = img.shape
        y1 = max(0, y - offset)
        y2 = min(imgHeight, y + h + offset)
        x1 = max(0, x - offset)
        x2 = min(imgWidth, x + w + offset)

        imgCrop = img[y1:y2, x1:x2]

        if imgCrop.size != 0:
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            aspectRatio = h / w

            # Resize & Center Hand on White Canvas
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

            cv2.imshow('Crop View', imgCrop)
            cv2.imshow('Processed White Canvas', imgWhite)

            # Auto-Capture Trigger Logic
            if auto_capture and (time.time() - last_capture_time) >= capture_interval:
                file_path = os.path.join(save_directory, f'Image_{time.time()}.jpg')
                cv2.imwrite(file_path, imgWhite)
                last_capture_time = time.time()

    # Draw Top Dashboard HUD Header
    cv2.rectangle(imgOutput, (0, 0), (imgOutput.shape[1], 75), (30, 30, 30), cv2.FILLED)

    # Active Gesture Label & Index
    cv2.putText(imgOutput, f"Active Sign: {current_gesture} [{current_index + 1}/{len(gestures)}]", 
                (20, 32), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)

    # Image Saved Progress Counter
    counter_color = (0, 255, 0) if saved_count >= target_count else (255, 255, 255)
    cv2.putText(imgOutput, f"Saved Images: {saved_count}/{target_count}", 
                (20, 62), cv2.FONT_HERSHEY_COMPLEX, 0.6, counter_color, 1)

    # Auto Recording Status Indicator
    if auto_capture:
        cv2.putText(imgOutput, "[AUTO RECORDING ON]", (imgOutput.shape[1] - 260, 45), 
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)
    else:
        cv2.putText(imgOutput, "Press SPACE for Auto", (imgOutput.shape[1] - 260, 45), 
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (180, 180, 180), 1)

    cv2.imshow('Data Collection Studio', imgOutput)

    # Keyboard Controls
    key = cv2.waitKey(1)

    # Save single image on 'S' key
    if key == ord("s") and hands:
        file_path = os.path.join(save_directory, f'Image_{time.time()}.jpg')
        cv2.imwrite(file_path, imgWhite)
        print(f"[{current_gesture}] Saved image #{saved_count + 1}")

    # Toggle Auto-Capture on SPACEBAR
    elif key == 32:
        auto_capture = not auto_capture
        print(f"Auto-Capture Mode: {'ENABLED' if auto_capture else 'DISABLED'}")

    # Next gesture on 'N' key
    elif key == ord("n"):
        current_index = (current_index + 1) % len(gestures)
        auto_capture = False
        print(f"Switched to Gesture: {gestures[current_index]}")

    # Number Keys 1-7 to select gesture directly
    elif ord('1') <= key <= ord('7'):
        selected_num = key - ord('1')
        if selected_num < len(gestures):
            current_index = selected_num
            auto_capture = False
            print(f"Switched to Gesture: {gestures[current_index]}")

    # Exit Studio on 'Q' or ESC key
    elif key == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()