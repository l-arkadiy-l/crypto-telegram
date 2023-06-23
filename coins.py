import shutil
import requests
from bs4 import BeautifulSoup as bf
import fake_useragent
from PIL import Image, ImageDraw, ImageFont


def get_info_image(coin, price, low_price, high_price, precent):
    # TODO: переделать расположение стрелок в зависимости от ширины цены, которая идет вверх и вниз
    # TODO: добавить, что это статистика за (1 day)
    background = Image.open('images/Screenshot_191.png')
    currency = Image.open('images/coin.png')
    arrow_up = Image.open('images/arrow_up.png')
    arrow_down = Image.open('images/arrow_up.png')
    arrow_precent = Image.open('images/arrow_up.png')
    arrow_down = arrow_down.rotate(270)
    arrow_precent = arrow_precent.rotate(270 if precent[0] == '-' else 0)
    # group images
    background.paste(currency, (30, 30))
    background.paste(arrow_up, (990, 96))
    background.paste(arrow_down, (990, 200))
    background.paste(arrow_precent, (450, 330))
    draw = ImageDraw.Draw(background)
    # fonts
    font_name = ImageFont.truetype("fonts/Asap-Bold.otf", 70)
    font_price = ImageFont.truetype("fonts/Asap-Italic.otf", 150)
    font_low_price = ImageFont.truetype("fonts/Amatic-Bold.ttf", 70)
    font_high_price = ImageFont.truetype("fonts/Amatic-Bold.ttf", 70, encoding='unic')
    font_precent = ImageFont.truetype("fonts/Asap-Italic.otf", 80)
    # text place
    draw.text((200, 30), coin.upper(), (0, 0, 0), font=font_name)
    draw.text((200, 90), price, (0, 0, 0), font=font_price)
    draw.text((850, 80), high_price, (0, 128, 0), font=font_high_price)
    draw.text((850, 180), low_price, (255, 0, 0), font=font_low_price)
    draw.text((200, 300), precent, (255, 0, 0) if precent[0] == '-' else (0, 128, 0), font=font_precent)
    background.save('images/new.png', quality=100)


def get_price(coin):
    user = fake_useragent.UserAgent().random
    header = {'User-Agent': user}
    link = f'https://cryptorank.io/price/{coin}'
    response = requests.get(link, headers=header)
    soup = bf(response.content, 'lxml')
    block = soup.find('div', attrs={'class': 'sc-8369f605-1 ceYCfg'})
    price = block.find('div', attrs={'class': 'sc-c366a7c4-0 gAvwjX'}).get_text()
    low_and_hight = block.find('div', attrs={'class': 'information'}).find_all('p')
    low_price = low_and_hight[-1].get_text()
    high_price = low_and_hight[0].get_text()
    # differents classes for up and down prices
    try:
        precent = block.find('span', attrs={'class': 'sc-ce9abdd0-0 cIgbZX percent'}).get_text()
    except AttributeError:
        precent = block.find('span', attrs={'class': 'sc-ce9abdd0-0 cnvycl percent'}).get_text()

    # get image coin
    logo_coin = block.find('img', attrs={'class': 'coin-logo'})['src']
    response_img = requests.get(logo_coin, stream=True)
    with open('images/coin.png', 'wb') as out_file:
        shutil.copyfileobj(response_img.raw, out_file)
    del response_img
    get_info_image(coin, price, low_price, high_price, precent)


if __name__ == '__main__':
    get_price('render-token')
