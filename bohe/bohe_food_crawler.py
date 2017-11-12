#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path,sys
import math
import time
reload(sys)
sys.setdefaultencoding('utf8')

#proxies = shield_proxy.getListProxies()
#print proxies

food_classify_url = "http://www.boohee.com/food/group/"

def httpGet(url):
    time.sleep(0.1)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent': user_agent}
    session = requests.session()
    page = session.get(url, headers=headers) # no proxy
    #p = proxies[random.randint(0,len(proxies) - 1)]
    #page = session.get(url, proxies=p, headers=headers)
    soup = BeautifulSoup(page.text,'html.parser')#if not installed lxml, remove it
    return soup

def getPageDetail(page_url):
    page_detail = httpGet(page_url);
    classify_element_h2 = page_detail.find('h2', attrs={'class':'crumb'})
    classify_element_a = classify_element_h2.find_all('a')
    classify_string = re.sub('\s','',classify_element_a[1].string)
    classify_h2_text = re.sub('\s','',classify_element_h2.text)
    index = classify_h2_text.rfind('/')
    name = classify_h2_text[index+1:]
    print 'classify:' + classify_string + ';name:' + name
    nutrition_info = page_detail.find('div',attrs={'class':'nutr-tag margin10'})
    print nutrition_info



getPageDetail('http://www.boohee.com/shiwu/mifan_zheng')


