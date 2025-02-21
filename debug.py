import cv2

print("Starting script...")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Webcam opened successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    print("Frame captured")  # Debug print

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting loop")
        break

cap.release()
cv2.destroyAllWindows()
print("Script ended")
