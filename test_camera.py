import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# A simple function to count extended fingers from landmarks
def count_fingers(hand_landmarks):
    # Using landmark indices: Thumb=4, Index=8, Middle=12, Ring=16, Pinky=20
    # For the thumb, we compare x-coordinates (assuming a right hand)
    tips = [4, 8, 12, 16, 20]
    count = 0
    # Thumb: check if thumb tip is to the left of thumb IP joint
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        count += 1
    # Other fingers: compare tip y with pip y
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

# Map detected finger count (operator gesture) to operation
operator_mapping = {
    5: '+',  # Open palm => addition
    0: '-',  # Fist => subtraction
    2: '*',  # Scissors => multiplication
    3: '/'   # Three fingers => division
}

# State machine: "num1" -> "operator" -> "num2" -> "result"
state = "num1"
num1 = None
operator = None
num2 = None

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame (optional) and convert BGR to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        current_value = None
        if results.multi_hand_landmarks:
            # For simplicity, consider the first detected hand
            hand_landmarks = results.multi_hand_landmarks[0]
            current_value = count_fingers(hand_landmarks)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display instructions and state
        instruction = ""
        if state == "num1":
            instruction = "Show FIRST NUMBER and press 'c' to capture"
        elif state == "operator":
            instruction = "Show OPERATOR gesture and press 'c' to capture"
        elif state == "num2":
            instruction = "Show SECOND NUMBER and press 'c' to capture"
        elif state == "result":
            instruction = "Result displayed. Press 'r' to reset."

        cv2.putText(frame, instruction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 0), 2)

        # Show current detected value (if any)
        if current_value is not None:
            cv2.putText(frame, f"Detected: {current_value}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        # If all inputs are captured, show the full expression and result
        if state == "result":
            expression = f"{num1} {operator} {num2}"
            try:
                # Handle division-by-zero gracefully
                result_val = eval(expression) if operator != '/' or num2 != 0 else "Error: Div0"
            except Exception as e:
                result_val = "Error"
            cv2.putText(frame, f"{expression} = {result_val}", (10, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 3)

        cv2.imshow("Gesture-Based Calculator", frame)
        key = cv2.waitKey(1) & 0xFF

        # Capture the current gesture when 'c' is pressed
        if key == ord('c') and current_value is not None:
            if state == "num1":
                num1 = current_value
                state = "operator"
                print(f"Captured first number: {num1}")
            elif state == "operator":
                # Determine operator based on mapping; if no valid operator, prompt user again
                operator = operator_mapping.get(current_value, None)
                if operator is None:
                    print(f"Operator gesture not recognized (detected value: {current_value}). Try again.")
                else:
                    state = "num2"
                    print(f"Captured operator: {operator}")
            elif state == "num2":
                num2 = current_value
                state = "result"
                print(f"Captured second number: {num2}")

        # Reset the calculator with 'r'
        if key == ord('r'):
            state = "num1"
            num1, operator, num2 = None, None, None
            print("Calculator reset.")

        # Exit on pressing 'q'
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
