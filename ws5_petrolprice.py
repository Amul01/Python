import requests
from bs4 import BeautifulSoup
from lxml import html

page = requests.get('https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-surat.cms')
tree = html.fromstring(page.content)

petrolprice = tree.xpath('//*[@id="mainPage"]/section[1]/div[2]/div[2]/table/tbody/tr[41]/td[2]/text()')
print('Current price of petrol =',petrolprice[0])
