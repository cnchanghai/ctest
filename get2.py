#!/usr/bin/env python
#coding:utf-8
import requests
from bs4 import BeautifulSoup as bss
import threading
class th24(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        url = 'http://' + self.ip + '/hp/device/this.LCDispatcher?nav=hp.Usage'
        r = requests.get(url, verify=False)
        content = r.content
        soup = bss(content, 'html5lib')
        taa = soup.findAll('table', 'hpTable')[-1]
        tab = taa.findAll('span', 'hpPageText')[-1].text
        print tab

if __name__=="__main__":
    ip='10.65.2.16\n'
    print ip
    ip=ip.strip()
    print ip
    th=th24(ip)
    th.start()
    th.join()
    print ip
  
