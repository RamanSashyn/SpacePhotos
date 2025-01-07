import requests
from pathlib import Path


folder_path = Path(r"D:\Py\SpacePhotos\images")
folder_path.mkdir(parents=True, exist_ok=True)

picture_name = 'hubble.jpeg'
picture_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

picture_path = folder_path / picture_name

response = requests.get(picture_url)
response.raise_for_status()

with open(picture_path, 'wb') as file:
    file.write(response.content)
