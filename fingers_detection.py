import threading

def capture_input():
    global key_pressed
    while True:
        key_pressed = input().strip().lower()

key_pressed = None
threading.Thread(target=capture_input, daemon=True).start()
