# 🤚 Hand Gesture Calculator — Calculator Controlled by Hand Gestures

**A real-time computer vision project that uses hand gestures to perform basic arithmetic (addition, subtraction, multiplication, division) without touching any device.**

This interface leverages **OpenCV** and **MediaPipe** to recognize hand gestures and convert them into numbers or operators, enabling a touch-free calculator experience. ([GitHub][1])

---

## 🚀 Project Summary

In automation and human-computer interaction, gesture control provides a natural, intuitive way to operate systems. This project implements a **gesture-based calculator** that:

✔ Detects fingers shown as numbers
✔ Interprets hand gestures as operator commands
✔ Performs calculations in real time
✔ Displays results on screen automatically ([GitHub][1])

---

## 🔍 Key Features

* 🎯 **Hand Gesture Recognition** using MediaPipe
* 📈 **Real-time video processing** with OpenCV
* 🔢 **Number & operator detection** based on hand shape
* ➕➖✖️➗ Perform arithmetic operations without keyboard input
* ⏱️ Automatic reset after each calculation cycle ([GitHub][1])

---

## 🛠️ Tech Stack

| Layer           | Technology      |
| --------------- | --------------- |
| Language        | Python          |
| Computer Vision | OpenCV          |
| Hand Tracking   | MediaPipe       |
| Input           | Webcam          |
| Environment     | Local execution |

**Libraries used:**

```bash
opencv-python mediapipe
```

---

## 📦 Project Structure

```
hand_gesture_calculator/
├── detect_hand_gestures.py     # Detects hand and key points
├── fingers_detection.py        # Counts fingers and detects gesture states
├── final_calculator.py         # Main program logic for calculator operation
├── hand_calculator.py          # Entry point for running the calculator
├── video_capture.py            # Video feed setup
├── test*.py                   # Testing and helper scripts
├── video_final.mp4             # Demo video
├── README.md                   # This documentation
└── Requirements/ environment/
```

---

## 📥 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/modiraunak/hand_gesture_calculator.git
   cd hand_gesture_calculator
   ```

2. **Create a Python environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install opencv-python mediapipe
   ```

---

## ▶️ Usage

1. **Connect your webcam.**
2. **Run the calculator script:**

   ```bash
   python hand_calculator.py
   ```
3. **Use gestures to input:**

   * Show **1–5 fingers** to represent the first number
   * Wait → show **a gesture for operator** (e.g., fist for `-`, five fingers for `+`)
   * Show **1–5 fingers** for the second number
   * Result displays automatically and resets after a few seconds 

---

## 🧠 How It Works (High-Level)

1. **Hand Tracking:** MediaPipe detects hand landmarks from webcam video frames.
2. **Gesture Interpretation:** Based on finger count & positions, gestures are mapped to digits/operators.
3. **Calculation Engine:** Recognized input is processed into an arithmetic expression and evaluated.
4. **Display Logic:** The result is shown on screen, followed by an automatic reset.

---

## 📷 Screenshot / Demo

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/0bedf798-c3b5-43b6-afa7-c1834eaf2819" />

---

## 🧠 Learning Outcomes

* Applied **computer vision** for gesture detection
* Used **MediaPipe** for hand landmark extraction
* Integrated real-time video feed with **OpenCV**
* Built a touchless interactive application

---

## 🏆 Future Enhancements

* ✨ Support for more operators (e.g., exponent, mod)
* 🧠 ML-based gesture classification for robustness
* 📱 Web or mobile interface with streaming support
* 🔊 Audio feedback for accessibility

---

## 👨‍💻 Author

**Raunak Kumar Modi**
B.Tech Computer Science Engineering — VIT Bhopal
GitHub: [https://github.com/modiraunak](https://github.com/modiraunak)

---

## ⭐ A Note to Recruiters & Developers

This project demonstrates:

* Practical computer vision implementation
* Real-time human-computer interaction
* Project structuring, documentation, and live input handling

Feel free to star or contribute! 🚀

---






Thank You Everyone For Watching :-)
