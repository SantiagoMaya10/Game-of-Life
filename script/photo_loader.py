import cv2

def load_photo(file_path):
    # Load the photo from the file system
    photo = cv2.imread(file_path)

    if photo is None:
        print(f"Error: Unable to load photo from {file_path}")
        raise Exception("Could not load photo from resource path")
    else:
        return photo

