import requests
from lxml import html
from bs4 import BeautifulSoup

nescopage = requests.get('https://www.moneycontrol.com/india/stockpricequote/diversified/nesco/NES')
nescotree = html.fromstring(nescopage.content)
nesco = nescotree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')
print('NESCO = '+nesco[0])

ongcpage = requests.get('https://www.moneycontrol.com/india/stockpricequote/oil-drilling-and-exploration/oilnaturalgascorporation/ONG')
ongctree = html.fromstring(ongcpage.content)
ongc = ongctree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')
print('ONGC = '+ongc[0])

coalpage = requests.get('https://www.moneycontrol.com/india/stockpricequote/mining-minerals/coalindia/CI11')
coaltree = html.fromstring(coalpage.content)
coal = coaltree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')
print('Coal India = '+coal[0])

#a = coaltree.xpath('//*[@id="content_bse"]/div[1]/text()')
#print(a)

#soup = BeautifulSoup(coalpage.text,'html.parser')
#print(soup.prettify)
#print(soup.title.get_text())
#print(soup.find_all('p'))
#print(soup.p)
#print(soup.get_text())

#l = soup.find({"class":"brdb PB5"})
#print(l)
