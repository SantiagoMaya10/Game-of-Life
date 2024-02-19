import cv2
import time

def take_photo():
    # Open the default system camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        raise Exception("Could not open camera")
    
    # Give time to camera to capture ligth
    time.sleep(1)

    # Read a frame from the camera ret is a bool and frame is an array of bytes
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        raise Exception("Could not read frame")
    
    # Save the captured frame as a photo
    photo_file = 'captured_photo.jpg'
    cv2.imwrite(photo_file, frame)
        
    # Release the camera
    cap.release()

    photo = cv2.imread(photo_file)

    return photo
