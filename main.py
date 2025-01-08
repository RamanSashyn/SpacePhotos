import requests
import os
from pathlib import Path
from urllib.parse import urlparse


"""def get_links(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    picture_urls = response.json().get('links', {}).get('flickr', {}).get('original', [])

    if picture_urls:
        print(picture_urls)
    else:
        print("Фотографии отсутствуют")
    return picture_urls
"""



def download_image():
    picture_url = input('Введите url картинки: ')
    folder_path_input = input("Введите путь к папке для сохранения (например, D:/Images): ")
    picture_name = input('Введите имя картинки: ')

    folder_path = Path(folder_path_input)

    folder_path.mkdir(parents=True, exist_ok=True)

    picture_path = folder_path / picture_name

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(picture_url, headers=headers)
    response.raise_for_status()

    with open(picture_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    folder_path = Path(r"D:\Py\SpacePhotos\images")
    folder_path.mkdir(parents=True, exist_ok=True)

    picture_urls = response.json().get('links', {}).get('flickr', {}).get('original', [])
    if not picture_urls:
        print("Фотографии отсутствуют.")
        return

    for index, picture_url in enumerate(picture_urls):
        picture_name = f'spacex_{index}.jpg'
        picture_path = folder_path / picture_name

        picture_response = requests.get(picture_url)
        picture_response.raise_for_status()

        with open(picture_path, 'wb') as file:
            file.write(picture_response.content)





launch_id = "5eb87d42ffd86e000604b384"
fetch_spacex_last_launch(launch_id)