#!/usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
import requests
url='http://www.moko.cc/mtb.html'
r=requests.get(url, verify=False)
content=r.content
soup=BeautifulSoup(content,'lxml')
modlist=soup.find_all('div','sub_show')
link=[]
for i in modlist:
    if i==modlist[-1] or i==modlist[0]:
        continue
    tmp=i.find_all('a')
    for j in tmp:
        if 'html' in j['href']:
            link.append(j['href'])
            print j['href']
print 'http://www.moko.cc'+link[0]
url2='http://www.moko.cc'+link[0]
r=requests.get(url2, verify=False)
content=r.content
soup=BeautifulSoup(content,'lxml')
alist=soup.find_all('div','thumbnail_box')
soup2=BeautifulSoup(str(alist),'lxml')
blist=soup2.find_all('dd')
for item in blist:
    link=item.find('img')
    try:
         if '.png' in link['src']:
              pass   
         else:
              print link['src'].split('?')[0]
    except:
        continue

