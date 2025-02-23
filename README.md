Hand Gesture Calculator using OpenCV & MediaPipe
📢 Hello Everyone!
In the world of automation, imagine a basic calculator that performs addition, subtraction, multiplication, and division—not with buttons, but using hand gestures! 🤯

This project uses OpenCV and MediaPipe to recognize hand gestures and convert them into numbers and operators, allowing you to perform calculations without touching anything! 🖐️ ➕ ✋ = 🔢

🚀 Features
✅ Hand gesture-based number & operator detection
✅ Performs Addition (+), Subtraction (-), Multiplication (*), and Division (/)
✅ Real-time video processing with OpenCV
✅ Auto-detection every 10 seconds (No need to press any keys)
✅ Displays the result on the screen and resets for new calculations

📌 How It Works
1️⃣ Show a number using your fingers (1-5).
2️⃣ Show an operator (e.g., all fingers for "+", no fingers for "-").
3️⃣ Show another number for the second operand.
4️⃣ Wait for 10 seconds between each step.
5️⃣ The result appears on the screen!

📌 Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone gh repo clone modiraunak/project1
2️⃣ Install Dependencies
bash
Copy
Edit
pip install opencv-python mediapipe
3️⃣ Run the Script
bash
Copy
Edit
python hand_calculator.py


🛠️ Tech Stack
Python 🐍
OpenCV (for video processing) 🎥
MediaPipe (for hand tracking) ✋

👋 How to Use
First Number: Show 1-5 fingers to indicate a number. The system captures after 10 seconds.
Operator: Show hand gestures:
🖐️ (5 fingers) → +
✊ (fist) → -
✌️ (2 fingers) → /
🤟 (3 fingers) → *
Second Number: Show 1-5 fingers again.
Final Result Appears on Screen.
Wait 5 seconds → Auto-reset → Repeat from step 1.
🤝 Contribute
Feel free to fork, improve, and contribute to this project!
