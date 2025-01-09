import os
from urllib.parse import urlsplit


def get_file_extension(url):
    split_url = urlsplit(url)
    file_path = split_url.path
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension