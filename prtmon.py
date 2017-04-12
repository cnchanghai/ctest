#!/usr/bin/env python
#coding:utf-8
import requests
import time
import sys
import os
from bs4 import BeautifulSoup as bss
import threading
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mylock = threading.Lock()
global prtnum
prtnum=dict()
## 定义2420打印机类
class th24(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        global prtnum
        try:
            url = 'http://' + self.ip + '/hp/device/this.LCDispatcher?nav=hp.Usage'
            r = requests.get(url, verify=False)
            content = r.content
            soup = bss(content, 'lxml')
            taa = soup.findAll('table', 'hpTable')[-1]
            tab = taa.findAll('span', 'hpPageText')[-1].text
            mylock.acquire()
            prtnum[self.ip]=tab
            mylock.release()
        except:
            mylock.acquire()
            prtnum[self.ip] = 0
            mylock.release()
## 定义3015打印机类
class th35(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        global prtnum
        try:
            url = 'https://' + self.ip + '/hp/device/this.LCDispatcher?nav=hp.Usage'
            r = requests.get(url, verify=False)
            content = r.content
            soup = bss(content, 'html5lib')
            taa = soup.findAll('table', id='tbl-1847')[-1]
            tab = taa.findAll('div', 'hpPageText')[-1].text
            mylock.acquire()
            prtnum[self.ip] = tab
            mylock.release()
        except:
            mylock.acquire()
            prtnum[self.ip] = 0
            mylock.release()

def sendmms():
    global prtnum
    dt=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sender = 'Robot@aseglobal.com'
    receivers = ['Arthur_Li@aseglobal.com']
    day = dt.split('-')[-1]
    if int(day)==5:
        receivers.append('jop_huang@aseglobal.com')
        receivers.append('luke_wu@aseglobal.com')
    f=open(mulu+'log/'+dt+'.txt','w')#打开日志文件

    mail_msg = '<h3>'+dt+'打印量记录</h3><br/><table  style="width:360px;" border="1" cellspacing="0" cellpadding="0">'
    for(k ,v) in prtnum.items():
        kvs='<tr style="heigh:60px;"><td style="width:180px;">'+str(k)+'</td><td style="width:180px;">'+str(v)+'</td></tr>'
        mail_msg+=kvs
        f.write(str(k)+'    '+str(v)+'\n')#写入日志文件
    f.close()

    mail_msg+='</table>'
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("unreply", 'utf-8')
    subject = '打印机每日监控'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP('10.65.1.134')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"


if __name__=="__main__":
    thlist2=[]
    thlist3=[]
    mulu=os.path.split(sys.argv[0])[0]+'/'
    ip2=open(mulu+'ip2.txt','r')
    ip3=open(mulu+'ip3.txt','r')
    for ip in ip2:
        th=th24(ip.strip())
        th.start()
        thlist2.append(th)
    for ip in ip3:
        th=th35(ip.strip())
        th.start()
        thlist3.append(th)
    ip2.close()
    ip3.close()
    for th in thlist2:
        th.join()
    for th in thlist3:
        th.join()
    sendmms()
