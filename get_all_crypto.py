# sc-130f0f3b-0 sc-458805bb-0 iTGRFm eOoaoa sc-47b02c3a-4 GpyoP
import fake_useragent
from bs4 import BeautifulSoup as bf
import requests


for i in range(1, 621):
    user = fake_useragent.UserAgent().random
    header = {'User-Agent': user}
    link = f'https://cryptorank.io/?page=2'
    response = requests.get(link, headers=header)
    soup = bf(response.content, 'lxml')
    print([i.get_text() for i in soup.find_all('p', attrs={'class': 'sc-130f0f3b-0 sc-458805bb-0 iTGRFm eOoaoa sc-47b02c3a-4 GpyoP'})])
