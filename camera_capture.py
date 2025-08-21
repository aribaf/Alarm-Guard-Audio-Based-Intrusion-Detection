import cv2

def capture_image(filename="image.jpg"):
    """Captures an image using the system's camera."""
    print("Opening camera...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image captured: {filename}")
    else:
        print("Failed to capture image.")
    cap.release()
    return filename
