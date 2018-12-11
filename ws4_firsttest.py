import requests
from bs4 import BeautifulSoup
from lxml import html

page1 = requests.get('https://economictimes.indiatimes.com/')
tree = html.fromstring(page1.content)

sensexpoint = tree.xpath('//*[@id="i_sensex"]/p[2]/span[1]/a/b/text()')
print("The value of sensex = ",sensexpoint)

sensex = tree.xpath('//*[@id="i_sensex"]/p[2]/span[1]/a/text()')
print("The value of sensex = ",sensex)

page2 = requests.get('https://economictimes.indiatimes.com/indices/sensex_30_companies')
tree2 = html.fromstring(page2.content)

openprice = tree2.xpath('//*[@id="open"]/text()')
closeprice = tree2.xpath('//*[@id="prevClose"]/text()')

print(openprice, ' ', closeprice)

#headstuff = tree.xpath('//*[@id="headStuff"]/text()')
#print(headstuff)
