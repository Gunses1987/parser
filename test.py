import requests
from bs4 import BeautifulSoup

URL = 'https://themeforest.net/category/wordpress/blog-magazine/personal?sort=date'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 'accept':'*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
        pass
    else:
        print('Error')


parse()