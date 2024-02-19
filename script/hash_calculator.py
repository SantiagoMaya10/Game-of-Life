import hashlib
import cv2
import photo_taker
import photo_loader

def calculate_frame_hash(frame):
    # Convert the frame object to bytes
    frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()

    # Compute the SHA-256 hash of the frame bytes
    hash_object = hashlib.sha256(frame_bytes)
    frame_hash = hash_object.hexdigest()
    frame_hash_decimal = int(frame_hash, 16)


    return frame_hash_decimal

