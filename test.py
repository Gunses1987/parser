from importlib.resources import path
import requests
from bs4 import BeautifulSoup
import csv
# import os

URL = 'https://themeforest.net/category/wordpress'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 'accept':'*/*'}
HOST = 'https://themeforest.net'
BY = 'by: '
SALES = ' Global'
FILE = 'WPsites.csv'


  
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='category-items_block_component__button')
    # if pagination:
    #     return int (pagination[-1].get_text())
    # else:
    #         return 1
    print(pagination)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='shared-item_cards-grid-image_card_component__experimentToggleClickableItemCard')
  

    print(items)

    WPsites= []
    for item in items:
        WPsites.append ( {
            'title': item.find('a', class_='shared-item_cards-item_name_component__itemNameLink').get_text(),
            'link': item.find('a', class_='shared-item_cards-preview_button_with_analytics_component__root').get('href'),
            'price': item.find('div', class_='shared-item_cards-price_component__root').get_text(strip=True),
            'picture': item.find('img', class_='shared-item_cards-preview_image_component__image'),
            'byWho': BY + item.find('a', class_='shared-item_cards-author_category_component__link').get_text(strip=True),
            # 'sales': item.find('div', class_='shared-item_cards-sales_component__root').get_text(strip=True) + SALES,
        } )
    return WPsites
        # print(len(WPsites))
      

def save_file(items, path):
    with open(path, 'w', newline='') as file:
       writer = csv.writer(file, delimiter=',')
       writer.writerow(['title', 'link', 'price', 'picture', 'byWho'])
       for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['picture'], item['byWho']])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # pages_count = get_pages_count(html.text)
        WPsites = get_content(html.text)
        save_file (WPsites, FILE)
        print(f'Gadavparset {len(WPsites)} saitis cardi')       
        pass
    else:
        print('Error')


parse()