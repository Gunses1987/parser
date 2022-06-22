import requests
from bs4 import BeautifulSoup

URL = 'https://themeforest.net/popular_item/by_category?category=wordpress'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 'accept':'*/*'}
  # HOST = 'https://themeforest.net/'
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

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


            
        } )
        print(WPsites)
        print(len(WPsites))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        pass
    else:
        print('Error')


parse()