import requests
import os
from pathlib import Path
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_image import download_image
from get_file_extension import get_file_extension


def main():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        print('Ошибка: API ключ не найден.')
        return

    params = {'api_key': api_key, 'count': 30}
    base_url = 'https://api.nasa.gov/planetary/apod'
    url = f'{base_url}?{urlencode(params)}'

    response = requests.get(url)
    response.raise_for_status()

    folder_path = Path("./images/nasa_apod")
    nasa_data = response.json()
    if not nasa_data:
        print("Фотографии отсутствуют.")
        return

    for index, nasa_item in enumerate(nasa_data):
        nasa_url = nasa_item['url']
        if not nasa_url:
            continue

        file_extension = get_file_extension(nasa_url)
        if not file_extension:
            continue

        picture_name = f'nasa_apod_{index}{file_extension}'
        download_image(nasa_url, folder_path, picture_name)


if __name__ == '__main__':
    main()