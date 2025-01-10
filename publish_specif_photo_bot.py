import argparse
import random
import os
from dotenv import load_dotenv
from get_picture_from_directory import get_picture_from_directory
from send_photo_to_telegram import send_photo_to_telegram


def publish_photo(bot_token, chat_id, photo_directory, specific_photo=None):
    if specific_photo:
        photo_path = os.path.join(photo_directory, specific_photo)
        if not os.path.isfile(photo_path):
            raise FileNotFoundError(f"Указанный файл '{specific_photo}' не найден в директории '{photo_directory}'.")
    else:
        photos = get_picture_from_directory(photo_directory)
        if not photos:
            raise ValueError("В указанной директории нет подходящих изображений.")
        photo_path = random.choice(photos)

    send_photo_to_telegram(bot_token, chat_id, photo_path)


def parse_args():
    parser = argparse.ArgumentParser(description="Публикует фотографию в Telegram-канал.")
    parser.add_argument(
        "photo_directory",
        type=str,
        help="Путь к директории с фотографиями."
    )
    parser.add_argument(
        "--photo",
        type=str,
        default=None,
        help="Имя файла фотографии для публикации (по умолчанию выбрана случайная)."
    )
    return parser.parse_args()


def main():
    load_dotenv()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if not bot_token or not chat_id:
        raise EnvironmentError("Не найдены переменные окружения TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID.")

    args = parse_args()
    publish_photo(bot_token, chat_id, args.photo_directory, args.photo)


if __name__ == '__main__':
    main()