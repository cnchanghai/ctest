#!/usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
import requests
url='http://www.moko.cc/mtb.html'
r=requests.get(url, verify=False)
content=r.content
soup=BeautifulSoup(content,'lxml')
modlist=soup.find_all('dl','sub_fl')
link=[]
for i in modlist:
    if i==modlist[-1]:
        break
    tmp=i.find_all('a')
    for j in tmp:
        link.append(j['href'])
print 'http://www.moko.cc'+link[0]
pic=[]
link2=[]
url2='http://www.moko.cc'+link[0]
r=requests.get(url2, verify=False)
content=r.content
soup=BeautifulSoup(content,'lxml')
blist=soup.find_all('dd')
for item in blist:
    link2=item.find('img')
    try:
         if '.png' in link2['src']:
              pass   
         else:
              print link2['src'].split('?')[0]
    except:
        continue

