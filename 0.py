from tkinter import *
import pymysql
#conn = pymysql.connect(host='localhost', user='root', password='', db='bills')
#cur = conn.cursor()

m = Tk()
m.title('Bill Management')

mb = Menu(m)
e = Menu(mb, tearoff=0)
e.add_command(label='Old bills')
e.add_command(label='Last bill')
mb.add_cascade(label='Electricity Bill', menu=e)

m.config(menu=mb)
m.mainloop()
