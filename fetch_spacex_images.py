import requests
from pathlib import Path
from download_image import download_image
import argparse


def fetch_spacex_images(launch_info, folder_path):
    picture_urls = (
        launch_info.get("links", {}).get("flickr", {}).get("original", [])
    )
    if not picture_urls:
        print("Фотографии отсутствуют.")
        return

    for index, picture_url in enumerate(picture_urls):
        picture_name = f"spacex_{index}.jpg"
        download_image(picture_url, folder_path, picture_name)


def main():
    parser = argparse.ArgumentParser(description="Скачивание фото SpaceX")
    parser.add_argument(
        "--launch_id",
        type=str,
        default='latest',
        help="ID запуска SpaceX (по умолчанию используется последний запуск)",
    )
    args = parser.parse_args()

    url = f"https://api.spacexdata.com/v5/launches/{args.launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    launch_info = response.json()

    folder_path = Path("./images")
    fetch_spacex_images(launch_info, folder_path)


if __name__ == "__main__":
    main()
