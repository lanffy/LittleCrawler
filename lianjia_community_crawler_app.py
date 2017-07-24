#!/usr/bin/python
# -*- coding: utf-8 -*-
import shield_proxy,our_proxy
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


lianjia_host = "http://sh.lianjia.com"
lianjia_app_host = "http://m.sh.lianjia.com/api/v1/m/strategy/contents/"
proxies = our_proxy.getListProxies()

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
    global proxies
    time.sleep(0.01)
    a = str(random.randint(1,10))
    aa = str(random.randint(1,10))
    b = str(random.randint(1,11))
    c = str(random.randint(1,12))
    d = str(random.randint(1,8))
    user_agent = 'Mozilla/' + a + '.' + aa + ' (Macintosh; Intel Mac OS X '+b+'_'+c+'_'+d+')'
    headers = {'User-Agent': user_agent}
    session = requests.session()
    #page = session.get(url, headers=headers)
    length = len(proxies) - 1
    for i in range(0, length):
        p = proxies[i]
        try:
            page = session.get(url, proxies=p, headers=headers, timeout=2)
            if(type(page) != 'NoneType'):
                print 'http get ok,proxy:' + str(p)
                break;
            else:
                continue
        except Exception, e:
            proxies = our_proxy.getListProxies()
            i = 0
            print 'http get failed,proxy:' + str(p)
            continue
    soup = BeautifulSoup(page.text,'html.parser')#if not installed lxml, remove it
    if(type(soup) == 'NoneType'):
        proxies = our_proxy.getListProxies()
        print 'get none type, try again'
        return httpGet(url)
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
    global proxies
    try:
        page_soup = httpGet(url)
        page_community_count_div = page_soup.find('div', attrs={'class':'list-head clear'})
        p_community_count = page_community_count_div.find('span').string
    except Exception, e:
        print 'get community count failed,try again:' + url
        proxies = our_proxy.getListProxies()
        return getPageCommunityCount(url)
    return p_community_count

def listHandler(url):
    proxies = our_proxy.getListProxies()
    print '1->>>>>hand list:' + url + ' start====='
    p_community_count = getPageCommunityCount(url)
    cc = int(math.ceil(int(p_community_count) / float(20)))
    print 'community total:' + str(p_community_count) + ';page total:' + str(cc)
    for i in range(1, cc+1):
        page_url = url + 'd' + str(i) + '/'
        pageHandler(page_url)
    print '1->>>>>hand list:' + url + ' end====='

block = ''
def pageHandler(page_url):
    global block
    print '2->>>>>hand page:' + page_url + ' start====='
    page_content_soup = httpGet(page_url)
    #community_div = page_content_soup.find_all('a', attrs={'name':'selectDetail', 'title':re.compile(".*")})
    community_div = page_content_soup.find_all('div', attrs={'class':'info-panel'})
    for cd in community_div:
        cd_h2 = cd.find('a', attrs={'name':'selectDetail', 'title':re.compile(".*")})
        c_id = cd_h2['key']
        con = cd.find('div', attrs={'class':'con'})
        block = con.find_all('a')[1].string
        mkdirBlockDoc(block)
        mkdirAppBlockDoc(block)
        appCommunityHandler(c_id)

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
    time.sleep(0.01)
    cid = str(community_id)
    print '3->>>>>hand community:' + cid + ' start====='
    app_url = lianjia_app_host + cid
    print app_url
    global proxies
    all_p = len(proxies) - 1
    for i in range(0, all_p):
        p = proxies[i]
        try:
            strategy_res = requests.get(app_url, proxies=p, timeout=2)
        except Exception, e:
            print '3->>>>>hand community get error:' + cid + ' end=====' + str(p)
            proxies = our_proxy.getListProxies()
            i = 0
            continue
        strategy_http_code = strategy_res.status_code
        if(strategy_http_code != 200):
            print '3->>>>>hand community http code error:' + cid + ' end=====' + str(p)
            proxies = our_proxy.getListProxies()
            i = 0
            continue
        else:
            break
    strategy_content = strategy_res.content
    sc = json.loads(strategy_content)
    sc_list = sc['data']['list']
    if(not sc_list[0]['content'].has_key('content')):
        print '3->>>>>not have strategy:' + cid + ' end====='
        return
    else:
        name = sc['data']['name']
        app_location = app + '/' + district_name + '/' + block + '/' + name + '.html'
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

def appCommunityHandlerNoStyle(community_id):
    time.sleep(0.01)
    cid = str(community_id)
    print '3->>>>>hand community:' + cid + ' start====='
    app_url = lianjia_app_host + cid
    print app_url
    global proxies
    all_p = len(proxies) - 1
    for i in range(0, all_p):
        p = proxies[i]
        try:
            strategy_res = requests.get(app_url, proxies=p, timeout=2)
        except Exception, e:
            print '3->>>>>hand community get error:' + cid + ' end=====' + str(p)
            proxies = our_proxy.getListProxies()
            i = 0
            continue
        strategy_http_code = strategy_res.status_code
        if(strategy_http_code != 200):
            print '3->>>>>hand community http code error:' + cid + ' end=====' + str(p)
            proxies = our_proxy.getListProxies()
            i = 0
            continue
        else:
            break
    strategy_content = strategy_res.content
    sc = json.loads(strategy_content)
    sc_list = sc['data']['list']
    if(not sc_list[0]['content'].has_key('content')):
        print '3->>>>>not have strategy:' + cid + ' end====='
        return
    else:
        name = sc['data']['name']
        app_location = app + '/' + district_name + '/' + block + '/' + name + '.txt'
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
    global proxies
    try:
        page = httpGet(district_url)
        l_txt = page.find('div',attrs={'class':'fl l-txt'})
        l_txt_a = l_txt.find_all('a')
        district_name = l_txt_a[2].text
        mkdirPcDoc(district_name)
        mkdirAppDoc(district_name)
        return district_name
    except Exception, e:
        print 'get community count failed,try again:' + district_url
        proxies = our_proxy.getListProxies()
        return setDistrictName(district_url)

def mkdirPcDoc(name):
    if(not os.path.exists(pc + '/' + name)):
        os.makedirs(pc + '/' + name)

def mkdirAppDoc(name):
    if(not os.path.exists(app + '/' + name)):
        os.makedirs(app + '/' + name)

def mkdirBlockDoc(block_name):
    if(not os.path.exists(pc + '/' + district_name+ '/' + block_name)):
        os.makedirs(pc + '/' + district_name+ '/' + block_name)


def mkdirAppBlockDoc(block_name):
    if(not os.path.exists(app + '/' + district_name+ '/' + block_name)):
        os.makedirs(app + '/' + district_name+ '/' + block_name)

#district_name = setDistrictName('http://sh.lianjia.com/xiaoqu/shenzhuang/')
#print district_name
#listHandler('http://sh.lianjia.com/xiaoqu/beicai/')
#appCommunityHandler(5011102207057)
#proxies = shield_proxy.getListProxies()

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

