import requests
from pathlib import Path
from download_image import download_image
import argparse


def get_latest_launch_id():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    return launch_data.get('id')


def fetch_spacex_images(launch_id, folder_path):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    picture_urls = response.json().get('links', {}).get('flickr', {}).get('original', [])
    if not picture_urls:
        print("Фотографии отсутствуют.")
        return

    for index, picture_url in enumerate(picture_urls):
        picture_name = f"spacex_{index}.jpg"
        download_image(picture_url, folder_path, picture_name)


def main():
    parser = argparse.ArgumentParser(description="Скачивание фото SpaceX")
    parser.add_argument("--launch_id", type=str, help="ID запуска SpaceX (если не указан, используется последний)")
    args = parser.parse_args()

    if args.launch_id is None:
        launch_id = get_latest_launch_id()
        print(f"Используем ID последнего запуска: {launch_id}")
    else:
        launch_id = args.launch_id

    folder_path = Path("./images/spacex")
    fetch_spacex_images(launch_id, folder_path)

if __name__ == "__main__":
    main()
