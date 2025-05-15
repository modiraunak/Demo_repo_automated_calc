import cv2
import mediapipe as mp
import time

# Initializeing  Mediapipe 
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to detect the number of fingers shown by the user 
def detect_number(hand_landmarks):
    # Finger tips landmarks
    tips = [4, 8, 12, 16, 20]
    extended_fingers = []

    # Check if the thumb is shown or not by the user
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        extended_fingers.append("Thumb")

    # Check how many fingers are shown by the user 
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            extended_fingers.append(tip)

    # Return the number of extended fingers (max 5)
    return len(extended_fingers) if len(extended_fingers) <= 5 else 0

# Function to detect the operator from hand gestures
def detect_operator(hand_landmarks):
    # Count how many fingers are extended
    num_fingers = len([finger for finger in [8, 12, 16, 20]
                       if hand_landmarks.landmark[finger].y < hand_landmarks.landmark[finger - 2].y])

    # Return the operator based on the number of fingers extended(made with simple if - else statements)
    if num_fingers == 5:
        return "+"
    elif num_fingers == 0:
        return "-"
    elif num_fingers == 2:
        return "*"
    elif num_fingers == 3:
        return "/"
    else:
        return None

# Creating calculator states and initializing variables
state = "num1"
num1 = None
operator = None
num2 = None
start_time = time.time()
result_val = None
current_expression = ""

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize Mediapipe hands
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # flip the camera for better view 
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # detect the value 
        current_value = None
        detected_operator = None

        # Check for hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Detect number  based on the finger or thumb shown by the user 
                if state == "num1" or state == "num2":
                    current_value = detect_number(hand_landmarks)
                elif state == "operator":
                    detected_operator = detect_operator(hand_landmarks)

        # Show statements for the calculator display 
        if state == "num1":
            instruction = "Show FIRST NUMBER"
        elif state == "operator":
            instruction = "Show OPERATOR (+, -, *, /)"
        elif state == "num2":
            instruction = "Show SECOND NUMBER"
        elif state == "result":
            instruction = f"Result: {result_val}. Restarting..."

        # start the timmer of thye calculator 
        elapsed_time = int(time.time() - start_time)
        countdown = max(10 - elapsed_time, 0)
        cv2.putText(frame, f"{instruction} (Capturing in {countdown}s)",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # create a real time dashboard 
        cv2.putText(frame, f"Expression: {current_expression}", 
                    (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # detect the number and reset the calculator using countdoqn function (made with simple if else)
        if countdown == 0:
            if state == "num1" and current_value is not None:
                num1 = current_value
                current_expression = str(num1)
                state = "operator"
                start_time = time.time()
                print(f"First Number Captured: {num1}")

            elif state == "operator" and detected_operator is not None:
                operator = detected_operator
                current_expression += f" {operator} "
                state = "num2"
                start_time = time.time()
                print(f"Operator Captured: {operator}")

            elif state == "num2" and current_value is not None:
                num2 = current_value
                current_expression += str(num2)
                state = "result"
                start_time = time.time()
                print(f"Second Number Captured: {num2}")

                # now performs the calculation detected by hand gestures shown by the user  
                expression = f"{num1} {operator} {num2}"
                try:
                    result_val = eval(expression) if operator != '/' or num2 != 0 
                else "Error: Division by 0"
                except Exception:
                    result_val = "Error"
                print(f"Result: {expression} = {result_val}")

        # show the output of the calculations made 
        if state == "result":
            cv2.putText(frame, f"{num1} {operator} {num2} = {result_val}", 
                        (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)

            # reset the calculator after every  8 seconds
            if elapsed_time >= 8:
                state = "num1"
                num1, operator, num2 = None, None, None
                result_val = None
                current_expression = ""
                start_time = time.time()
                print("Calculator reset.")

        # Display the video in the compiler (VS Code Recommended)
        cv2.imshow("Hand Gesture Calculator", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
