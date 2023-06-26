# sc-130f0f3b-0 sc-458805bb-0 iTGRFm eOoaoa sc-47b02c3a-4 GpyoP
import fake_useragent
from bs4 import BeautifulSoup as bf
from selenium.webdriver.common.by import By
import requests
from selenium import webdriver

user = fake_useragent.UserAgent().random
header = {'User-Agent': user}
link = f'https://coinmarketcap.com/all/views/all/'
driver = webdriver.Firefox()
driver.get(link)
element = driver.find_elements(By.CLASS_NAME, 'cmc-table__column-name--name cmc-link')
print(element)
# element[0].click()
soup = bf(driver.page_source, 'lxml')
print([i.get_text() for i in soup.find_all('a', attrs={'class': 'cmc-table__column-name--name cmc-link'})])
driver.close()
