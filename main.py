import requests
import os
from pathlib import Path
from urllib.parse import urlsplit, urlencode
from dotenv import load_dotenv


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


def get_file_extension():
    url = "https://example.com/txt/hello%20world.txt?v=9#python"

    split_url = urlsplit(url)

    file_path = split_url.path

    file_name, file_extension = os.path.splitext(file_path)

    print(file_extension)


def download_nasa_picture():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    if not api_key:
        print('Ошибка: API ключ не найден.')
        return

    params = {
        'api_key': api_key,
        'count': 30
    }
    base_url = 'https://api.nasa.gov/planetary/apod'
    url = f'{base_url}?{urlencode(params)}'
    response = requests.get(url)
    response.raise_for_status()

    folder_path = Path(r"D:\Py\SpacePhotos\images")
    folder_path.mkdir(parents=True, exist_ok=True)

    nasa_data = response.json()
    if not nasa_data:
        print("Фотографии отсутствуют.")
        return

    for index, nasa_item in enumerate(nasa_data):
        nasa_url = nasa_item.get('url')
        picture_name = f'nasa_apod_{index}.jpg'
        picture_path = folder_path / picture_name

        picture_response = requests.get(nasa_url)
        picture_response.raise_for_status()

        with open(picture_path, 'wb') as file:
            file.write(picture_response.content)


download_nasa_picture()



