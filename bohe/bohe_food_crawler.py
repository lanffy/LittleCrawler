#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding: utf-8
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
host = 'http://www.boohee.com'
max_page = 10
max_group = 10

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

# 详情页
def handPageDetail(page_url):
    print '==333== strat hand detail page:' + page_url
    page_detail = httpGet(page_url);
    classify_element_h2 = page_detail.find('h2', attrs={'class':'crumb'})
    classify_element_a = classify_element_h2.find_all('a')
    classify_string = re.sub('\s','',classify_element_a[1].string)
    classify_h2_text = re.sub('\s','',classify_element_h2.text)
    index = classify_h2_text.rfind('/')
    name = classify_h2_text[index+1:]
    img = page_detail.find('div',attrs={'class':'food-pic pull-left'}).find('img')['src']
    alias_div = page_detail.find('ul',attrs={'class':'basic-infor'})
    alias_div_li = alias_div.find('li').text
    alias_div_li_name = re.sub(ur'别名：','',alias_div_li)
    alias = '无'
    if(len(alias_div_li) != len(alias_div_li_name)):
        alias = alias_div_li_name
    print 'classify:' + classify_string + ';name:' + name + ';alias:' + alias + ';image:' + img
    nutrition_info = page_detail.find('div',attrs={'class':'nutr-tag margin10'})
    nutrition_info2 = nutrition_info.find_all('dd',attrs={})
    nutrition_info3 = nutrition_info2[2:6]
    print '营养信息:'
    for info in nutrition_info3:
        name = info.find('span', attrs={'class':'dt'}).string
        value = info.find('span', attrs={'class':'dd'}).string
        print name + ':' + value
    more_nutrition_info = page_detail.find('div',attrs={'class':'widget-unit'})
    more_nutrition_info2 = more_nutrition_info.find('tbody')
    tr_list = more_nutrition_info2.find_all('tr')
    print '度量单位(大卡):'
    for tr in tr_list:
        tds = tr.find_all('td')
        name = tds[0]
        value = tds[1]
        print getMoreNutritionInfo(name) + ':' + re.sub(ur'大卡','',getMoreNutritionInfo(value))
    print '==333==  end  hand detail page'

def getMoreNutritionInfo(elment):
    name_inner = elment.find('a')
    if(name_inner):
        return name_inner.string
    else:
        name_inner = elment.find('span')
        if(name_inner):
            return name_inner.string
        else:
            return elment.string

def getListPages(url):
    page_detail = httpGet(url)
    food_list = page_detail.find('ul',attrs={'class':'food-list'})
    food_list_lis = food_list.find_all('li',attrs={'class':'item clearfix'})
    page_list = []
    for li in food_list_lis:
        a = li.find('div',attrs={'class':'text-box pull-left'}).find('a')['href']
        page_list.append(a)
    return page_list

def handListPage(uri_list):
    for page_uri in uri_list:
        page_detail_url = host + page_uri
        handPageDetail(page_detail_url)

#handPageDetail('http://www.boohee.com/shiwu/yumi_xian')
#getListPages('http://www.boohee.com/food/group/1?page=1')

def listPageHandler(group_url):
    for page in range(1, max_page+1):
        page_url = group_url + '?page=' + str(page)
        page_list = getListPages(page_url)
        print '=='+str(page)+'== strat hand list page:' + page_url
        handListPage(page_list)
        print '=='+str(page)+'==  end  hand list page'

def main():
    for group_index in range(1, max_group+1):
        group_url = food_classify_url + str(group_index)
        print '==G'+str(group_index)+'== start hand group:' + group_url
        listPageHandler(group_url)
        print '==G'+str(group_index)+'==  end  hand group'


max_group = 10
max_page = 10

main()
