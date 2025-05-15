#HELLO EVERYONE,
In the world of automation, imagine a basic calculator that performs addition, subtraction, multiplication, and division—not with buttons, but using hand gestures! 

This project uses OpenCV and MediaPipe to recognize hand gestures and convert them into numbers and operators, allowing you to perform calculations without touching anything! 

Features
✅ Hand gesture-based number & operator detection
✅ Performs Addition (+), Subtraction (-), Multiplication (*), and Division (/)
✅ Real-time video processing with OpenCV
✅ Auto-detection every 10 seconds (No need to press any keys)
✅ Displays the result on the screen and resets for new calculations

 Setup & Installation
1️. Clone the Repository
bash
Copy
Edit
git clone gh repo clone modiraunak/project1
2️. Install Dependencies
bash
Copy
Edit
pip install opencv-python mediapipe
3️. Run the Script
bash
Copy
Edit
python hand_calculator.py

Tech Stack
Python 
OpenCV (for video processing) 
MediaPipe (for hand tracking) 

👋 How to Use
First Number: Show 1-5 fingers to indicate a number. The system captures after 10 seconds.
Operator: Show hand gestures:
🖐️ (5 fingers) → +
✊ (fist) → -
✌️ (2 fingers) → /
🤟 (3 fingers) → *
Second Number: Show 1-5 fingers again.
Final Result Appears on Screen.
Wait 8 seconds → Auto-reset → Repeat from step 1.
Please ignore the commit log as i was new to git when i created this project 
This is a demo project made my me to know how can make projects and deploy it  
My Main Project will be launched in July 2025 
Thank You Everyone For Watching :-)
