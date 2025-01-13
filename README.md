# Space Photos Telegram Bot

Этот проект предоставляет набор скриптов для работы с фотографиями из различных источников (SpaceX, NASA, EPIC) и их публикации в Telegram-канал.

## Скрипты

1. **space_photos_bot.py**
   Автоматически публикует все фотографии из указанной директории в Telegram-канал с заданным интервалом.

2. **publish_specific_photo_bot.py**
   Публикует указанную фотографию в Telegram-канал или случайную фотографию из директории.

3. **fetch_epic_images.py**
   Скачивает фотографии с камеры EPIC (NASA).

4. **fetch_nasa_apod_images.py**
   Скачивает фотографии с сервиса NASA APOD (Astronomy Picture of the Day).

5. **fetch_spacex_images.py**
   Скачивает фотографии последнего запуска SpaceX (или указанного запуска).

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your-username/SpacePhotos.git
    cd SpacePhotos
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

    Активируйте виртуальное окружение:

    - **Linux/MacOS**:
        ```bash
        source venv/bin/activate
        ```
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` и добавьте в него необходимые ключи и настройки:

    ```plaintext
    TELEGRAM_BOT_TOKEN=<ваш_токен>
    TELEGRAM_CHAT_ID=<ваш_чат_ID>
    TELEGRAM_INTERVAL=4  # Интервал публикации (в часах)
    NASA_API_KEY=<ваш_ключ_API_от_NASA>
    ```

## Примеры запуска

### 1. Автоматическая публикация фотографий

Скрипт публикует все фотографии из указанной директории в случайном порядке раз в заданный интервал времени:

```bash
python space_photos_bot.py <путь_к_директории>
```

Пример:

```bash
python space_photos_bot.py ./images
```

### 2. Публикация конкретной фотографии или случайной

Скрипт публикует указанную фотографию или случайную из директории:

- Для публикации конкретной фотографии:

    ```bash
    python publish_specific_photo_bot.py <путь_к_директории> --photo <имя_файла>
    ```

    Пример:

    ```bash
    python publish_specific_photo_bot.py ./images --photo example.jpg
    ```

- Для публикации случайной фотографии:

    ```bash
    python publish_specific_photo_bot.py <путь_к_директории>
    ```

    Пример:

    ```bash
    python publish_specific_photo_bot.py ./images
    ```

### 3. Скачивание фотографий NASA EPIC

Скрипт скачивает фотографии NASA EPIC в директорию `./images`:

```bash
python fetch_epic_images.py
```

### 4. Скачивание фотографий NASA APOD

Скрипт скачивает до 30 случайных фотографий NASA APOD в директорию `./images`:

```bash
python fetch_nasa_apod_images.py
```

### 5. Скачивание фотографий SpaceX

- Для скачивания фотографий последнего запуска SpaceX:

    ```bash
    python fetch_spacex_images.py
    ```

- Для скачивания фотографий конкретного запуска по ID:

    ```bash
    python fetch_spacex_images.py --launch_id <ID_запуска>
    ```

    Пример:

    ```bash
    python fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
    ```

## Требования

- Python 3.9 или выше.
- Установленные зависимости из `requirements.txt`.

## Лицензия

MIT License

Copyright (c) 2025 Raman Sashyn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

