#https://www.datacamp.com/community/tutorials/web-scraping-using-python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline

import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.hubertiming.com/results/2017GPTR10K')
soup = BeautifulSoup(res.text,'lxml')

rows = soup.find_all('tr')
#for i in rows[:10]:
#    print(i.get_text())

for row in rows:
    row_td = row.find_all('td')
#print(row_td)
#type(row_td)

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, 'lxml').get_text()
print(cleantext)

df = pd.DataFrame(cleantext, columns=2)
df.head(10)
