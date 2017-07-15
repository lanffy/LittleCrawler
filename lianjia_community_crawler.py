#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path

ua = 'Mozilla/5.0 (Mactintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': ua}
session = requests.session()
url = "http://www.xicidaili.com/nn/" + str(random.randint(1,1))
page = session.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
taglist = soup.find_all('tr', attrs={'class':re.compile("(odd)|()")})
for trtag in taglist:
    tdlist = trtag.find_all('td')
    proxy_url = tdlist[5].string.lower() + ':' + tdlist[1].string + ':' + tdlist[2].string
    url = "http://ip.chinaz.com/getip.aspx"
    proxy = {proxy_url}
    try:
        response = session.get(url, proxies=proxy, timeout=10)
        print proxy_url + ' useable'
    except Exception, e:
        print proxy_url + ' unuseable'
        continue

