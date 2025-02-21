import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_gesture = mp.solutions.gesture_recognizer

#video 
cap = cv2.VideoCapture(0)
with mp_gesture.GestureRecognizer(
    min_detection_confidence=0.8, min_tracking_confidence=0.5) as gesture_recognizer:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = gesture_recognizer.process(rgb_frame)
        if results.hand_landmarks:
            for hand_landmarks, handedness, gesture in zip(
                    results.hand_landmarks, results.handedness, results.gestures)
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                if gesture:
                    gesture_name = gesture[0].category_name
                    cv2.putText(frame, f'Gesture: {gesture_name}',
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
