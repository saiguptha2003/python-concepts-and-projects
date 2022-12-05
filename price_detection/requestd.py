import requests as r
import re
from matplotlib import pyplot as plt
from datetime import date 
import csv
import  pywhatkit as py
from bs4 import BeautifulSoup
import pandas as pd
import os
def plot(filename):
     plt.rcParams["figure.figsize"] = [7.00, 3.50]
     plt.rcParams["figure.autolayout"] = True
     columns = ["date", "price"]
     df = pd.read_csv(filename, usecols=columns)
     print("Contents in csv file:", df)
     plt.plot(df.date, df.price)
     plt.show()
def findPrice(url):
     s=r.get(url)
     soup=BeautifulSoup(s.content,'html.parser')
     e=soup.find('div',class_='_1YokD2 _3Mn1Gg col-8-12')
     d=e.find('div',class_='_25b18c')
     f=d.find('div',class_='_30jeq3 _16Jk6d')
     g=e.find('div',class_='aMaAEs')
     h=g.find('span',class_='B_NuCI')
     print(h.text)
     today=date.today()
     dd=today.strftime("%d/%m/%Y")
     print(dd)
     price=f.text
     price=re.sub("[^\d\.]","",price)
     price=int(price)
     print(price)
     filename="E:\python\price_detection\csddd.csv"
    # header=("data","price")
     data=(dd,price)
     if(os.path.isfile(filename)):
          with open(filename,"a",newline="") as csvfile:
               d=csv.writer(csvfile)
               d.writerow(data)
               plot(filename)
               g="Hi Admin!\n here is price of mobile phone \n"+h.text+"\n and its cost ₹"+str(price)+"\n"
               py.sendwhatmsg_instantly("+918897792929",g,10)
url='https://www.flipkart.com/oppo-k10-black-carbon-128-gb/p/itm6205e7e72fe0c?pid=MOBGCFUHMDFSCM9W&lid=LSTMOBGCFUHMDFSCM9WSL0U8O&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_8&otracker=search&otracker1=search&fm=organic&iid=06a02554-0bad-401b-b306-7fecfc38c3ad.MOBGCFUHMDFSCM9W.SEARCH&ppt=hp&ppn=homepage&ssid=94mo1r79b40000001670082465402&qH=eb4af0bf07c16429'

findPrice(url) 
