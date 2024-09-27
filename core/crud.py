import json
import os
from config import Config


def load_urls():
    if not os.path.exists(Config.URLS_JSON_PATH):
        return {}

    with open(Config.URLS_JSON_PATH, 'r') as file:
        return json.load(file)


def save_urls(urls):
    with open(Config.URLS_JSON_PATH, 'w') as file:
        json.dump(urls, file, indent=4)


def save_url(short_url, long_url):
    mapped_urls = load_urls()

    new_mapped_url = {
        "short_url": short_url,
        "long_url": long_url
    }

    mapped_urls['mapped_urls'].append(new_mapped_url)
    save_urls(mapped_urls)


def exists(long_url):
    mapped_urls = load_urls()
    for existing_mapped_url in mapped_urls['mapped_urls']:
        if existing_mapped_url['long_url'] == long_url:
            return existing_mapped_url['short_url']

    return None


def get_long_url(short_url):
    mapped_urls = load_urls()
    for existing_mapped_url in mapped_urls['mapped_urls']:
        if existing_mapped_url['short_url'] == short_url:
            return existing_mapped_url['long_url']

    return {'msg': 'No link found'}
