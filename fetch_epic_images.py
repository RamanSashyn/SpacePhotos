import requests
from pathlib import Path
from dotenv import load_dotenv
import os
from datetime import datetime
from download_image import download_image


def main():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        print('Ошибка: API ключ не найден.')
        return

    params = {'api_key': api_key,}
    epic_api_url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(epic_api_url, params=params)
    response.raise_for_status()

    epic_data = response.json()
    if not epic_data:
        print('Фотографии отсутствуют.')
        return

    folder_path = Path('./images/nasa_epic')
    for index, epic_photo in enumerate(epic_data[:5]):
        image_name = epic_photo.get('image')
        date = epic_photo.get('date')

        try:
            date_obj = datetime.fromisoformat(date)
            formatted_date = date_obj.strftime("%Y/%m/%d")
        except ValueError as e:
            print(f'Ошибка в преобразовании {date}: {e}')
            continue

        year, month, day = formatted_date.split('/')
        photo_url = (
            f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/"
            f"{image_name}.png?api_key={api_key}"
        )

        picture_name = f"epic_photo_{index}.png"
        download_image(photo_url, folder_path, picture_name)


if __name__ == '__main__':
    main()