import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Handsq
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to detect numbers from hand gestures
def detect_number(hand_landmarks):
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    extended_fingers = []

    # Thumb (Check if it's extended using x-coordinates)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        extended_fingers.append("Thumb")

    # Other fingers (Check if tip is above the middle joint)
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            extended_fingers.append(tip)

    # Number detection based on extended fingers
    num_fingers = len(extended_fingers)
    return num_fingers if num_fingers <= 5 else 0  # Only 1-5 for simplicity

# Function to detect operators from hand gestures
def detect_operator(hand_landmarks):
    num_fingers = len([finger for finger in [8, 12, 16, 20] if hand_landmarks.landmark[finger].y < hand_landmarks.landmark[finger - 2].y])

    if num_fingers == 5:
        return "+"
    elif num_fingers == 0:
        return "-"
    elif num_fingers == 2:
        return "*"
    elif num_fingers == 3:
        return "/"
    return None

# Calculator variables
state = "num1"
num1 = None
operator = None
num2 = None
start_time = time.time()
result_val = None

# Start capturing video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not received.")
            break

        # Flip frame and process
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        current_value = None
        detected_operator = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if state in ["num1", "num2"]:
                    current_value = detect_number(hand_landmarks)
                elif state == "operator":
                    detected_operator = detect_operator(hand_landmarks)

        # Display instruction based on state
        instruction = ""
        if state == "num1":
            instruction = "Show FIRST NUMBER"
        elif state == "operator":
            instruction = "Show OPERATOR"
        elif state == "num2":
            instruction = "Show SECOND NUMBER"
        elif state == "result":
            instruction = f"Result: {result_val}. Restarting..."

        # Show countdown timer
        elapsed_time = int(time.time() - start_time)
        countdown = max(10 - elapsed_time, 0)
        cv2.putText(frame, f"{instruction} (Capturing in {countdown}s)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # Show detected values
        if current_value is not None:
            cv2.putText(frame, f"Detected: {current_value}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        if detected_operator is not None:
            cv2.putText(frame, f"Operator: {detected_operator}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Auto-capture input every 10 seconds
        if countdown == 0:
            if state == "num1" and current_value is not None:
                num1 = current_value
                state = "operator"
                start_time = time.time()
                print(f"Captured first number: {num1}")

            elif state == "operator" and detected_operator is not None:
                operator = detected_operator
                state = "num2"
                start_time = time.time()
                print(f"Captured operator: {operator}")

            elif state == "num2" and current_value is not None:
                num2 = current_value
                state = "result"
                start_time = time.time()
                print(f"Captured second number: {num2}")

                # Calculate the result
                expression = f"{num1} {operator} {num2}"
                try:
                    result_val = eval(expression) if operator != '/' or num2 != 0 else "Error: Div0"
                except Exception:
                    result_val = "Error"
                print(f"Result: {expression} = {result_val}")

        # Show result when ready
        if state == "result":
            expression = f"{num1} {operator} {num2} = {result_val}"
            cv2.putText(frame, expression, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)

            # Reset after 5 seconds
            if elapsed_time >= 5:
                state = "num1"
                num1, operator, num2 = None, None, None
                result_val = None
                start_time = time.time()
                print("Calculator reset.")

        # **SHOW VIDEO WINDOW**
        cv2.imshow("Hand Gesture Calculator", frame)

        # Keep window responsive
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
