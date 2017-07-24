#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import random
import os.path
import json


def getAnjukeCommIdByLianjiaCommid(lianjia_comm_id):
    c_id = str(lianjia_comm_id)
    headers = {
        'Content-Type':'application/json',
        'Accept-Encoding':'application/gzip',
        'Api-Token':'1ecb1544-d146-417d-bbdf-618cebad7e22'
    }
    proxy_url = 'http://d.a.ajkdns.com/v1/hdp_anjuke_dm_db_dw_crawl_communities_id_map/rows?clientId=user_community'
    condition = {
        'where':[{
                'commid':c_id,
                'source':'1-Other'
            }],
        'columns':'commid,source,commid_list'
    }
    c = json.dumps(condition)
    r = requests.post(proxy_url, data=c, headers=headers)
    if(r.status_code != 200):
        print 'get anjuke comm id error,http code:' + str(r.status_code) + ';lianjia comm id:' + c_id
        return '0'
    try:
        res = r.content
        if(len(res) < 3):
            print 'not have mapping with anjuke comm;lianjia comm id:' + c_id + ';res:' + res
            return '0'
        res_j = json.loads(res)
        commid_other = res_j[0]['commid_list']
        co_j = json.loads(commid_other)
        cid = str(co_j[0]['commid_other'])
        print 'found have mapping with anjuke comm;lianjia comm id:' + c_id + ';anjuke comm id:' + cid
        return cid
    except Exception,e:
        print 'get anjuke comm id error,http code:' + str(r.status_code) + ';lianjia comm id:' + c_id
        return '0'

#getAnjukeCommIdByLianjiaCommid(5011000002998)
#getAnjukeCommIdByLianjiaCommid('5011000002998')
#getAnjukeCommIdByLianjiaCommid(1)
#getAnjukeCommIdByLianjiaCommid(0)
#getAnjukeCommIdByLianjiaCommid('a')
#getAnjukeCommIdByLianjiaCommid(9991)
