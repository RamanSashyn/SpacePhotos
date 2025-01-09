import requests
from pathlib import Path


def download_image(picture_url, folder_path, picture_name):
    response = requests.get(picture_url)
    response.raise_for_status()

    folder_path.mkdir(parents=True, exist_ok=True)
    picture_path = folder_path / picture_name

    with open(picture_path, 'wb') as file:
        file.write(response.content)