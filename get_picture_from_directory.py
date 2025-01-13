import os


def get_pictures_from_directory(directory_path):
    picture_extensions = ["jpg", "jpeg", "png", "gif"]
    pictures = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in [
                f".{ext}" for ext in picture_extensions
            ]:
                pictures.append(os.path.join(root, file))
    return pictures
