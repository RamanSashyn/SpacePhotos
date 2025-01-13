import time
import argparse
import random
import os
from dotenv import load_dotenv
from get_picture_from_directory import get_picture_from_directory
from send_photo_to_telegram import send_photo_to_telegram


def send_photos_in_loop(bot_token, chat_id, photos, interval_hours):
    while True:
        for photo in photos:
            send_photo_to_telegram(bot_token, chat_id, photo)
            time.sleep(interval_hours * 3600)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Публикует фотографии в Telegram-канал."
    )
    parser.add_argument(
        "photo_directory", type=str, help="Путь к директории с фотографиями."
    )
    return parser.parse_args()


def main():
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    interval = os.getenv("TELEGRAM_INTERVAL")
    if not bot_token or not chat_id:
        raise EnvironmentError(
            "Не найдены переменные окружения TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID."
        )

    try:
        interval = float(interval)
    except ValueError:
        raise ValueError(
            "Переменная окружения TELEGRAM_INTERVAL должна быть числом (в часах)."
        )

    args = parse_args()

    photos = get_picture_from_directory(args.photo_directory)
    if not photos:
        raise ValueError("Не найдено изображений в указанной директории.")
    random.shuffle(photos)

    send_photos_in_loop(bot_token, chat_id, photos, interval)


if __name__ == "__main__":
    main()
