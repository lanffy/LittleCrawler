#!/usr/bin/python
import shield_proxy
import requests
from bs4 import BeautifulSoup
import random
import os.path
import math

#proxies = shield_proxy.getListProxies()
#proxy = proxies[random.randint(0, len(proxies) - 1)]
#print proxy

lianjia_host = "http://sh.lianjia.com"
def httpGet(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent': user_agent}
    session = requests.session()
    page = session.get(url, headers=headers)
    #page = session.get(lianjia_community, proxies=proxy, headers=headers)
    soup = BeautifulSoup(page.text,'html.parser')#if not installed lxml, remove it
    return soup

def getAllDistrictUrl():
    lianjia_community_url = "http://sh.lianjia.com/xiaoqu/"
    all_community_soup = httpGet(lianjia_community_url)
    dllist = all_community_soup.find_all('div', attrs={'class': 'option-list gio_district'})
    all_district = [] #all community after district
    for dl in dllist:
        alist = dl.find_all('a', attrs={'class': ''})
        for a in alist:
            all_district.append(lianjia_host + a['href'])
    return all_district

def getBlockUrl(district_url):
    block_page_soup = httpGet(district_url)
    block = block_page_soup.find('div', attrs={'class':'option-list sub-option-list gio_plate'})
    alist = block.find_all('a', attrs={'class': ''})
    all_block = []
    for a in alist:
        all_block.append(lianjia_host + a['href'])
    return all_block

def getPageCommunityCount(url):
    page_soup = httpGet(url)
    page_community_count_div = page_soup.find('div', attrs={'class':'list-head clear'})
    p_community_count = page_community_count_div.find('span').string
    return p_community_count


def listHandler(url):
    print '=====hand page:' + url + ' start====='
    p_community_count = getPageCommunityCount(url)
    cc = int(math.ceil(int(p_community_count) / float(20)))
    print 'community total:' + str(p_community_count) + ';page total:' + str(cc)
    for i in range(1, cc+1):
        page_url = url + 'd' + str(i) + '/'
        print page_url



all_district_url = getAllDistrictUrl()
for d_url in all_district_url:
    print '=====hand district:' + d_url + ' start====='
    district_community_count = getPageCommunityCount(d_url)
    cc = int(math.ceil(int(district_community_count) / float(20)))
    print district_community_count
    if(cc > 100):
        print 'district community page big than 100, handle it by block'
        all_block_url = getBlockUrl(d_url)
        for bl in all_block_url:
            print 'hand block:' + bl
            listHandler(bl)
    else:
        listHandler(d_url)
    print '=====hand district:' + d_url + ' end====='

