import telegram
import time
import argparse
import random
import os
from dotenv import load_dotenv


def get_picture_from_directory(directory_path):
    picture_extensions = ['jpg', 'jpeg', 'png', 'gif']
    pictures = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in picture_extensions:
                pictures.append(os.path.join(root, file))
    return pictures


def send_photo_to_telegram(bot_token, chat_id, photo_path):
    bot = telegram.Bot(token=bot_token)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def publish_photos(bot_token, chat_id, photo_directory, interval):
    photos = get_picture_from_directory(photo_directory)
    while True:
        random.shuffle(photos)
        for photo in photos:
            send_photo_to_telegram(bot_token, chat_id, photo)
            time.sleep(interval * 3600)


def parse_args():
    parser = argparse.ArgumentParser(description="Публикует фотографии в Telegram-канал.")
    parser.add_argument("photo_directory", type=str, help="Путь к директории с фотографиями")
    parser.add_argument("--interval", type=int, help="Интервал между публикациями в часах")
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    interval = os.getenv('TELEGRAM_INTERVAL')
    if not bot_token or not chat_id:
        print("Ошибка: не найдены переменные окружения TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID.")
        return
    print(f"Токен: {bot_token}, Chat ID: {chat_id}, Интервал: {interval} часов.")
    args = parse_args()
    print(f"Путь к директории с фотографиями: {args.photo_directory}")
    publish_photos(args.photo_directory, args.interval, bot_token, chat_id)


if __name__ == '__main__':
    main()


