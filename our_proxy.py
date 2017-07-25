#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path
import json

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}
proxy_url = 'http://10.48.160.62:1700/proxy.php'

def getListProxies():
    p = {'http':'10.132.60.2:3128'}
    proxy_res = requests.get(proxy_url, proxies=p)
    all_pr = json.loads(proxy_res.content)
    pr = random.sample(all_pr, 20)
    proxyList = []
    for p in pr:
        proxy = {p['proxy_type'].lower(): p['ip'] + ':' + p['port']}
        proxyList.append(proxy)
    return proxyList

#a = getListProxies()
#for p in a:
#    print p
