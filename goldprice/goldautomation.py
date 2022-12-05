import requests as r
import re
from matplotlib import pyplot as plt
from datetime import date 
import csv
import  pywhatkit as py
from bs4 import BeautifulSoup
import pandas as pd
import os
def goldPrice(url):
     d=r.get(url)
     soup=BeautifulSoup(d.content,"html.parser")
     f=soup.find('div',class_='commodity-page__pricelist')
     d=f.find('div',class_='commodity-page__date')
     g=f.find('div',class_='commodity-page__value')
     price=g.text
     price=re.sub("[^\d\.]","",price)
     price=float(price)
     price=price//10
     return price


def datei(url):
     d=r.get(url)
     soup=BeautifulSoup(d.content,"html.parser")
     f=soup.find('div',class_='commodity-page__date')
     return f.text

url='https://www.5paisa.com/commodity-trading/gold'

def runner(url):
     k="hai ak\nIam your GoldPrice Bot\n Today's "+"Gold Price :₹{0}\n Date and Time {1}".format(goldPrice(url),datei(url))
     py.sendwhatmsg_instantly("+918897792929",k,10)
runner(url)