import requests
from lxml import html

today=[]
nesco=['NESCO']
ongc=['ONGC']
coal=['Coal India']
prev=[]
stocks=['NESCO','ONGC','Coal India']
cost = [589.0, 187.3, 311.0]
diff=[]

print('\nStock\t\tToday\t\tYesterday\tCost\tCurrent difference\n')
nescopage = requests.get('https://www.moneycontrol.com/india/stockpricequote/diversified/nesco/NES')
nescotree = html.fromstring(nescopage.content)
nesco.append(float(nescotree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')[0]))
nesco.append(float(nescotree.xpath('//*[@id="b_prevclose"]/strong/text()')[0]))
today.append(nesco[1])
prev.append(nesco[2])

ongcpage = requests.get('https://www.moneycontrol.com/india/stockpricequote/oil-drilling-and-exploration/oilnaturalgascorporation/ONG')
ongctree = html.fromstring(ongcpage.content)
ongc.append(float(ongctree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')[0]))
ongc.append(float(ongctree.xpath('//*[@id="b_prevclose"]/strong/text()')[0]))
today.append(ongc[1])
prev.append(ongc[2])

coalpage = requests.get('https://www.moneycontrol.com/india/stockpricequote/mining-minerals/coalindia/CI11')
coaltree = html.fromstring(coalpage.content)
coal.append(float(coaltree.xpath('//*[@id="Bse_Prc_tick"]/strong/text()')[0]))
coal.append(float(coaltree.xpath('//*[@id="b_prevclose"]/strong/text()')[0]))
today.append(coal[1])
prev.append(coal[2])

for i in range(3): diff.append(today[i]-cost[i])

#print(today)
#print(prev)
#for i in nesco: print(i,end='\t')

for i in range(len(today)):
    if(stocks[i]=='Coal India'): print(stocks[i],'\t',('%.2f' % today[i]),'\t',('%.2f' % prev[i]),'\t',('%.2f' % cost[i]),'\t',('%.2f' % diff[i]))
    else: print(stocks[i],'\t\t',('%.2f' % today[i]),'\t',('%.2f' % prev[i]),'\t',('%.2f' % cost[i]),'\t',('%.2f' % diff[i]))

#-----------------------------------------------------------------------------------------
#------------------------------DESKTOP NOTIFYING

import notify2
import time
notify2.init('Prices')
n = notify2.Notification(message='This is the notification') 

n.set_urgency(notify2.URGENCY_NORMAL) 
n.set_timeout(10000) 
n.update(today[1])
n.show() 

time.sleep(15) 

print(input('Press Enter to stop'))
