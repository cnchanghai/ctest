#coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

def print_qiushi(item):
    if item.find('div','thumb'):
        return
    if item.find('div','video_holder'):
        return
    author = item.find("h2")
    if author != None:
        author=author.get_text().strip()
    content=item.find("div",'content').get_text().strip()
    print author
    print content
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
  req= urllib2.Request(url,headers = headers)
  res= urllib2.urlopen(req)
  soup=BeautifulSoup(res.read(),"lxml")
  items=soup.findAll('div','article block untagged mb15')
  for item in items:
      print_qiushi(item)
except urllib2.URLError, e:
  if hasattr(e,"code"):
    print e.code
  if hasattr(e,"reason"):
    print e.reason
#print soup.title

#print soup.title.name

#print soup.title.string

#print soup.p

#print soup.a
#string=soup.findAll('div','article')
#sp2=BeautifulSoup(string[0])
#sp=sp2.span.string
#print sp


