#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}

def getListProxies():
    session = requests.session()
    #proxy_source = "http://www.xicidaili.com/nn/" + str(random.randint(1,1))
    proxy_source = "http://www.xicidaili.com/nt/" + str(random.randint(1,1))
    print proxy_source
    page = session.get(proxy_source, headers=headers)
    soup = BeautifulSoup(page.text,'html.parser')#if not installed lxml, remove it

    proxyList = []
    #find label tr which have property class
    taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    for trtag in taglist:
        tdlist = trtag.find_all('td')  #find label td in tr
        pu = tdlist[5].string.lower() + '://' + tdlist[1].string + ':' + tdlist[2].string   #ip:port
        proxy = {'http': tdlist[1].string + ':' + tdlist[2].string,
                 'https': tdlist[1].string + ':' + tdlist[2].string}
        url = "http://ip.chinaz.com/getip.aspx"
        try:
            response = session.get(url, proxies=proxy, timeout=5)
            proxyList.append(proxy)
            print pu + ' useable'
            if(len(proxyList) == 10):
                break
        except Exception, e:
            print pu + ' unuseable'
            continue
    return proxyList

a = getListProxies()
for p in a:
    print p
