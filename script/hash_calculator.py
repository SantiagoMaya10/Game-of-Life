import hashlib
import cv2
import photo_loader
import photo_taker

def calculate_frame_hash(frame):

    # Convert the frame object to bytes
    frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()

    # Compute the SHA-256 hash of the frame bytes
    hash_object = hashlib.sha256(frame_bytes)
    frame_hash = hash_object.hexdigest()
    
    # COnvert hex base to decimal base
    frame_hash_decimal = int(frame_hash, 16)

    return frame_hash_decimal

def infinite_ring(hash):
    # Convert the number to a string for easy iteration over its digits
    number_str = str(hash)

    # Generate an infinite loop
    while True:
        # Iterate over each digit of the number
        for digit in number_str:
            yield int(digit)
