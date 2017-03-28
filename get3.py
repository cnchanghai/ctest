#!/usr/bin/env python
#coding:utf-8
import requests
from bs4 import BeautifulSoup as bss 
def get3015():
    url='https://10.65.31.18/hp/device/this.LCDispatcher?nav=hp.Usage'
    r=requests.get(url,verify=False)
    content=r.content
    soup=bss(content,'lxml')
    taa=soup.findAll('table',id='tbl-1847')[-1]
    tab=taa.findAll('div','hpPageText')[-1].text
    print tab


get3015()
  
