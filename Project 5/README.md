<div align="center">

# 😊 Real-Time Emotion Detection System

### Computer Vision · Deep Learning · OpenCV · Keras

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![Keras](https://img.shields.io/badge/Keras-TF_Backend-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> A real-time facial emotion recognition system that detects faces via webcam and classifies emotions live — **no DeepFace**, no cloud API, runs 100% offline.

</div>

---

## 📸 Demo

| Feature | Detail |
|---|---|
| 🎥 Input | Live webcam feed |
| 🧠 Model | Custom CNN (`emotion_model.hdf5`) |
| 👤 Face Detection | Haar Cascade Classifier (OpenCV) |
| 😀 Emotions Detected | 7 classes |
| ⚡ Inference | Real-time, runs on CPU |
| 🖥️ Platform | Windows / macOS / Linux |

---

## 🎭 Emotion Classes

The model classifies faces into **7 emotion categories:**

| # | Emotion | Emoji |
|---|---|---|
| 0 | Angry | 😠 |
| 1 | Disgust | 🤢 |
| 2 | Fear | 😨 |
| 3 | Happy | 😄 |
| 4 | Sad | 😢 |
| 5 | Surprise | 😲 |
| 6 | Neutral | 😐 |

---

## 🗂️ Project Structure

```
emotion-detection/
│
├── emotion_detection.py                 ← Main script (webcam + inference loop)
├── emotion_model.hdf5                   ← Pre-trained CNN emotion model
├── haarcascade_frontalface_default.xml  ← OpenCV Haar Cascade face detector
└── README.md
```

---

## ⚙️ How It Works

```
Webcam Frame
     │
     ▼
Convert to Grayscale  →  cv2.cvtColor(frame, COLOR_BGR2GRAY)
     │
     ▼
Detect Faces  →  Haar Cascade detectMultiScale()
     │
     ▼
Crop & Resize Face ROI  →  64 × 64 px
     │
     ▼
Normalize Pixels  →  ÷ 255.0
     │
     ▼
Reshape Array  →  (1, 64, 64, 1)
     │
     ▼
CNN Prediction  →  emotion_model.hdf5
     │
     ▼
np.argmax()  →  Emotion Label
     │
     ▼
Draw Bounding Box + Label on Live Frame
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `opencv-python` | Webcam capture, frame processing, drawing |
| `opencv-contrib-python` | Extended OpenCV with Haar cascade data |
| `keras` / `tensorflow` | Loading and running the `.hdf5` CNN model |
| `numpy` | Array reshaping and pixel normalization |

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/developer-paramita/emotion-detection.git
cd emotion-detection
```

### 2. Install dependencies

**Windows (PowerShell):**
```powershell
python -m pip install opencv-python opencv-contrib-python tensorflow numpy
```

**macOS / Linux:**
```bash
pip install opencv-python opencv-contrib-python tensorflow numpy
```

> ⚠️ **Windows tip:** If `pip` is not recognized, always use `python -m pip install ...`
> Make sure Python was installed with **"Add Python to PATH"** checked.

### 3. Verify all required files are in the same folder
```
✅ emotion_detection.py
✅ emotion_model.hdf5
✅ haarcascade_frontalface_default.xml
```

### 4. Run the project
```bash
python emotion_detection.py
```

---

## 🎮 Controls

| Key | Action |
|---|---|
| `q` | Quit the application |

---

## 🖥️ Platform Compatibility

The script uses `cv2.CAP_AVFOUNDATION` which is optimized for **macOS**. If you're on **Windows or Linux**, change this line in `emotion_detection.py`:

```python
# macOS (default in this script)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Windows / Linux — replace with:
cap = cv2.VideoCapture(0)
```

---

## 📦 Requirements File

```txt
opencv-python>=4.5.0
opencv-contrib-python>=4.5.0
tensorflow>=2.6.0
numpy>=1.21.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🧠 Model Details

| Property | Value |
|---|---|
| File | `emotion_model.hdf5` |
| Input Shape | `(1, 64, 64, 1)` — single-channel grayscale |
| Output | Softmax probabilities over 7 emotion classes |
| Architecture | Convolutional Neural Network (CNN) |
| Reference Dataset | FER-2013 (Facial Expression Recognition) |

---

## 🐛 Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `pip is not recognized` | Python not in PATH | Use `python -m pip install ...` |
| `Error: cannot access webcam` | Webcam blocked | Check system webcam permissions |
| `Failed to grab frame` | Webcam in use elsewhere | Close other apps using the camera |
| `FileNotFoundError: emotion_model.hdf5` | File in wrong folder | Place `.hdf5` in the **same directory** as the script |
| `haarcascade XML not found` | Missing file | Place XML in the **same directory** as the script |
| `ModuleNotFoundError: keras` | Not installed | Run `pip install tensorflow` |

---

## 🔮 Future Improvements

- [ ] Add real-time FPS counter on the video feed
- [ ] Save detected emotion snapshots by pressing `s`
- [ ] Display emotion confidence scores as a progress bar
- [ ] Support detection of multiple faces simultaneously
- [ ] Export emotion log to a CSV file

---

## 👩‍💻 Author

**Paramita Bera** — B.Sc Computer Science Student, Haldia Institute of Management

[![GitHub](https://img.shields.io/badge/GitHub-developer--paramita-181717?style=flat-square&logo=github)](https://github.com/developer-paramita)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Paramita_Bera-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/paramita-bera-804a9a339/)

> Mentored by **SK Sahil** — AI Developer & Tutor ([@code_scholar_eu](https://www.instagram.com/code_scholar_eu/))

---

## 🙏 Acknowledgements

- [OpenCV](https://opencv.org/) — Haar Cascade face detection
- [FER-2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013) — facial expression benchmark
- [Keras / TensorFlow](https://keras.io/) — deep learning framework

---

<div align="center">

*Built with ❤️ using Python, OpenCV & Keras · © 2025 Paramita Bera*

</div>

