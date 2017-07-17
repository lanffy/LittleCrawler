#!/usr/bin/python
# -*- coding: utf-8 -*-
import shield_proxy
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path,sys
import math
import time
import json
reload(sys)
sys.setdefaultencoding('utf8')

#proxies = shield_proxy.getListProxies()
#print proxies

lianjia_host = "http://sh.lianjia.com"
lianjia_app_host = "http://m.sh.lianjia.com/api/v1/m/strategy/contents/"

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print "running from", dirname
print "file is", filename

home = dirname + '/链家'
pc = home + '/pc'
app = home + '/app'
district_name = ''

if(not os.path.exists(home)):
    os.makedirs(home)
if(not os.path.exists(pc)):
    os.makedirs(pc)
if(not os.path.exists(app)):
    os.makedirs(app)

def httpGet(url):
    #time.sleep(0.5)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent': user_agent}
    session = requests.session()
    page = session.get(url, headers=headers)
    #p = proxies[random.randint(0,len(proxies) - 1)]
    #page = session.get(url, proxies=p, headers=headers)
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
    print '1->>>>>hand list:' + url + ' start====='
    p_community_count = getPageCommunityCount(url)
    cc = int(math.ceil(int(p_community_count) / float(20)))
    print 'community total:' + str(p_community_count) + ';page total:' + str(cc)
    for i in range(1, cc+1):
        page_url = url + 'd' + str(i) + '/'
        pageHandler(page_url)
    print '1->>>>>hand list:' + url + ' end====='

def pageHandler(page_url):
    print '2->>>>>hand page:' + page_url + ' start====='
    page_content_soup = httpGet(page_url)
    community_div = page_content_soup.find_all('a', attrs={'name':'selectDetail', 'title':re.compile(".*")})
    for a in community_div:
        #communityHandler(lianjia_host + a['href'])
        appCommunityHandler(a['key'])

def communityHandler(community_url):
    print '3->>>>>hand community:' + community_url + ' start====='
    comm_page_soup = httpGet(community_url)
    strategy = comm_page_soup.find('div', attrs={'class':'property_q50 js_content'})
    if(strategy == None):
        print '3->>>>>hand community:not have strategy end====='
        return
    strategy_con = strategy.find('a', attrs={'target':'_blank'})
    community_name = comm_page_soup.find('h1').text
    location = pc + '/' + district_name + '/' + community_name + '.html'
    strategy_url = strategy_con['href']
    strategy_page = requests.get(strategy_url)
    strategy_http_code = strategy_page.status_code
    if(strategy_http_code != 200):
        print '3->>>>>hand community error:' + community_url + ' end====='
        os._exit(0)
    strategy_content = strategy_page.content
    file_hand = open(location, 'w')
    file_hand.writelines(strategy_content)
    file_hand.close()
    print '3->>>>>hand community:' + community_url + ' end====='

def appCommunityHandler(community_id):
    cid = str(community_id)
    print '3->>>>>hand community:' + cid + ' start====='
    app_url = lianjia_app_host + cid
    print app_url
    strategy_res = requests.get(app_url)
    strategy_http_code = strategy_res.status_code
    if(strategy_http_code != 200):
        print '3->>>>>hand community error:' + cid + ' end====='
        return
    strategy_content = strategy_res.content
    sc = json.loads(strategy_content)
    sc_list = sc['data']['list']
    if(not sc_list[0]['content'].has_key('content')):
        print '3->>>>>not have strategy:' + cid + ' end====='
        return
    else:
        name = sc['data']['name']
        app_location = app + '/' + district_name + '/' + name + '.html'
        file_hand = open(app_location, 'w+')
        file_hand.write('<html><body><h1>' + name + '</h1>')
        for l in sc_list:
            file_hand.write('<h2>' + l['name'] + '</h2>')
            if(l.has_key('content') and l['content'].has_key('content')):
                file_hand.write(l['content']['content'])
            children = l['children']
            for c in children:
                file_hand.write('<h3>' + c['name']  + '</h3>')
                if(c.has_key('content') and c['content'].has_key('content')):
                    file_hand.write(c['content']['content'])
            file_hand.write('<hr/>')
        file_hand.write('</body></html>')
    print '3->>>>>hand community:' + cid + ' end====='

def setDistrictName(district_url):
    page = httpGet(district_url)
    l_txt = page.find('div',attrs={'class':'fl l-txt'})
    l_txt_a = l_txt.find_all('a')
    district_name = l_txt_a[2].text
    mkdirPcDoc(district_name)
    mkdirAppDoc(district_name)
    return district_name

def mkdirPcDoc(name):
    if(not os.path.exists(pc + '/' + name)):
        os.makedirs(pc + '/' + name)

def mkdirAppDoc(name):
    if(not os.path.exists(app + '/' + name)):
        os.makedirs(app + '/' + name)

district_name = setDistrictName('http://sh.lianjia.com/xiaoqu/shenzhuang/')
print district_name
#listHandler('http://sh.lianjia.com/xiaoqu/beicai/')
appCommunityHandler(5011102207057)
os._exit(0)

all_district_url = getAllDistrictUrl()
for d_url in all_district_url:
    print '=====hand district:' + d_url + ' start====='
    district_name = setDistrictName(d_url)
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

