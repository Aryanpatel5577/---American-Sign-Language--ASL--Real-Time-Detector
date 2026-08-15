💻🎥🧠CODE EXPLANATION OF MY PROJECT💻🎥🧠 -------------->>>>>>>>>>
💻🎥🧠DEMO OF MY PROJECT💻🎥🧠 -------------->>>>>>>>>>

# 🤟 American Sign Language (ASL) Real-Time Detector

> **An AI-powered computer vision system that recognizes American Sign Language (ASL) gestures in real time using a standard webcam.**

This project combines **computer vision, hand tracking, image preprocessing, and deep learning** to recognize hand gestures and display the predicted sign instantly on screen.

---

## 🚀 Project Highlights

* 🤖 **Real-Time AI Recognition** — Detects and classifies ASL gestures directly from a live webcam feed.
* ✋ **21-Point Hand Tracking** — Uses MediaPipe to identify and track hand landmarks.
* 🎯 **Custom Dataset Pipeline** — Includes a dedicated tool for collecting and organizing training images.
* 🧠 **Deep Learning Classification** — Uses a TensorFlow/Keras neural network for gesture classification.
* 📊 **Confidence Filtering** — Displays predictions only when the model reaches the required confidence level.
* 🔄 **Prediction Smoothing** — Uses a 7-frame history buffer to reduce flickering and unstable predictions.
* ⚡ **Live Performance Monitoring** — Displays real-time FPS and prediction confidence.
* 🛡️ **Edge-Safe Processing** — Handles hand movements near camera boundaries without causing cropping errors.

---

## 📌 Project Overview

Communication between signing and non-signing individuals can sometimes be challenging. This project explores how **AI and computer vision can be used to create a lightweight, real-time sign language recognition system**.

The application follows a complete computer vision pipeline:

**Webcam → Hand Detection → Cropping & Preprocessing → Deep Learning Model → Prediction Filtering → Display**

The system detects a hand from the camera feed, prepares the image in a standardized format, sends it through the trained model, and displays the recognized gesture along with its confidence score.

---

## 🎯 Project Objectives

The main objectives of the project were to:

* Build a lightweight real-time computer vision application.
* Recognize common ASL gestures using a deep learning model.
* Create a custom dataset collection workflow.
* Standardize hand images before model inference.
* Reduce prediction instability in live video.
* Monitor model confidence and application performance in real time.

---

## ✨ Key Features

### 📸 Interactive Data Collection Studio

A custom data collection tool makes it easier to build and expand the dataset.

Features include:

* Automatic gesture folder management
* On-screen dataset counters
* Single-image capture
* Auto-capture burst mode
* Keyboard-based gesture selection
* Live camera preview

### 🧠 Real-Time Gesture Recognition

The application processes the webcam stream continuously and predicts the detected gesture while displaying:

* Recognized gesture
* Prediction confidence
* Current FPS

### 🔄 Anti-Flicker Prediction System

Live camera predictions can change rapidly between frames.

To improve stability, the project maintains a **7-frame prediction history** and uses the recent predictions to produce more consistent on-screen results.

### 🛡️ Safe Image Cropping

The preprocessing pipeline accounts for situations where the detected hand moves close to the edge of the camera frame, helping prevent invalid image-cropping operations.

---

## 🧰 Technologies Used

| Technology          | Purpose                                  |
| ------------------- | ---------------------------------------- |
| **Python 3.10**     | Core programming language                |
| **OpenCV**          | Webcam processing and computer vision    |
| **MediaPipe**       | Hand landmark detection                  |
| **CVZone**          | Simplified computer vision utilities     |
| **TensorFlow 2.15** | Deep learning framework                  |
| **Keras 2.15**      | Neural network implementation            |
| **NumPy**           | Numerical and image operations           |
| **Math**            | Geometric and preprocessing calculations |

---

## 📊 Dataset

A custom dataset was created for **7 commonly used gestures**:

| Gesture | Class      |
| ------- | ---------- |
| 👋      | Hello      |
| ❤️      | I Love You |
| ❌       | No         |
| 👌      | Okay       |
| 🙏      | Please     |
| 🤝      | Thank You  |
| 👍      | Yes        |

### Dataset Characteristics

* **7 gesture classes**
* **200+ images per gesture**
* **300 × 300 pixel** standardized images
* Images collected under different lighting conditions and hand orientations
* Hand images centered on a clean white background

The dataset collection tool was designed so that additional gestures can be added without significantly changing the overall pipeline.

---

## 🔬 How the System Works

### 1️⃣ Detection

OpenCV captures the live webcam stream while MediaPipe identifies the hand and its **21 landmarks**.

### 2️⃣ Preprocessing

The detected hand is:

* Cropped from the camera frame
* Rescaled while preserving its aspect ratio
* Centered on a **300 × 300 white canvas**
* Prepared for model inference

### 3️⃣ Classification

The processed image is passed to a trained **TensorFlow/Keras neural network**, which predicts the most likely gesture.

### 4️⃣ Confidence Filtering

Predictions below the selected confidence threshold are not immediately displayed, helping reduce unreliable outputs.

### 5️⃣ Prediction Smoothing

Recent predictions are stored in a **7-frame buffer** to reduce rapid label changes caused by natural hand movement.

### 6️⃣ Live Display

The final prediction, confidence percentage, and FPS are displayed directly on the webcam feed.

---

## ⚙️ Installation

### Prerequisites

* Python **3.10**
* Working webcam
* Git *(optional)*

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1 — Collect Custom Data *(Optional)*

To add new gestures or expand the dataset:

```bash
python datacollection.py
```

### Controls

| Key     | Action                         |
| ------- | ------------------------------ |
| `S`     | Save a single image            |
| `SPACE` | Toggle auto-capture burst mode |
| `N`     | Move to the next gesture       |
| `1 - 7` | Select a gesture directly      |
| `Q`     | Exit                           |

---

### Step 2 — Start Real-Time Detection

Run:

```bash
python test.py
```

The webcam window will open and begin recognizing the supported gestures.

Press **Q** or **ESC** to close the application.

---

## 📈 Results

The trained system successfully recognizes the supported gestures in real time.

### Observed Performance

* ⚡ Real-time webcam processing at approximately **30 FPS**
* 🎯 **90%+ accuracy** observed on the trained gesture classes
* 📊 Live prediction confidence
* 🔄 More stable predictions through frame smoothing
* 🖥️ Immediate visual feedback

> Performance can vary depending on lighting, camera quality, hand positioning, and the conditions under which the model was trained.

---

## 💡 Key Technical Insights

### Resolution Consistency Matters

The image resolution used during dataset creation needs to remain consistent with the resolution used during inference.

Using different preprocessing dimensions can introduce geometric distortions and negatively affect predictions.

### Prediction Smoothing Improves User Experience

Individual video frames can produce slightly different predictions even when the hand gesture remains the same.

Using a **7-frame prediction buffer** significantly reduces visual jitter and makes the system feel more stable during real-time use.

### Preprocessing Is as Important as the Model

Accurate classification depends not only on the neural network but also on how consistently the hand image is detected, cropped, scaled, and positioned before inference.

---

## 🧠 What I Learned

Through this project, I gained practical experience with:

* Building real-time computer vision pipelines
* Working with OpenCV and MediaPipe
* Detecting and tracking hand landmarks
* Preparing image data for neural networks
* Maintaining aspect ratios during preprocessing
* Implementing prediction smoothing
* Working with TensorFlow and Keras
* Managing Python package compatibility
* Designing tools for custom dataset collection
* Monitoring real-time application performance

---

## 🔮 Future Improvements

The current system recognizes a limited vocabulary. Possible future improvements include:

### 🔤 Expand the Vocabulary

Extend the dataset to support:

* Full A–Z ASL alphabet
* Numbers
* Additional everyday signs
* Larger gesture vocabulary

### 🔊 Text-to-Speech

Convert recognized gestures into spoken audio to provide another form of communication.

### 📝 Sentence Formation

Develop temporal gesture recognition so individual signs can be combined into meaningful sentences rather than being treated as isolated predictions.

### 🌐 Larger-Scale Recognition

With a larger and more diverse dataset, the system could be extended toward recognizing a much broader range of signing patterns and users.

---

## 📁 Project Structure

```text
ASL-Real-Time-Detector/
│
├── datacollection.py       # Custom dataset collection tool
├── test.py                 # Real-time ASL detection
├── requirements.txt        # Python dependencies
├── model/                  # Trained model files
├── data/                   # Gesture dataset
└── README.md               # Project documentation
```

---

## 🙌 Credits & Acknowledgements

This project makes use of:

* **MediaPipe** — Hand landmark detection
* **CVZone** — Computer vision utilities
* **OpenCV** — Image and video processing
* **TensorFlow / Keras** — Deep learning framework
* **Google Teachable Machine** — Model development/training workflow

---

## 👨‍💻 Author

### Aryan Patel

Computer Science Student | AI & Machine Learning Enthusiast

Interested in building practical applications using **Artificial Intelligence, Machine Learning, and Computer Vision**.

---

## ⭐ Project Summary

> **This project demonstrates how computer vision and deep learning can be combined to create a practical, real-time ASL gesture recognition system — from custom dataset collection and image preprocessing to model inference and prediction stabilization.**
