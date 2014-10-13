#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/6
brief：            从网页抓取图片，之后保存到excel表格
author:      fish
'''

import re
import re 
import sys
import requests
import time
from _codecs import decode

from config import *

reload(sys)
sys.setdefaultencoding('utf-8')

def login( passportDict ):
    
    loginUrl = 'http://www.renren.com/PLogin.do'   
     
    s = requests.session()
    
    #伪装浏览器
    headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
    }  
    
    loginData = {'email': passportDict['email'], 'password': passportDict['passwd']}
    
    res = s.post(loginUrl, data = loginData, headers = headers)

    file = res.text.encode('utf-8') 
    
    f=open('E:\\python\\tmp\\doc\\loginData.txt','w+')  
    f.write(file)  
    f.close()      
     
    findHostRe = re.compile(r"profile\.do\?id=(\d+).*?name.{1,4}title=.(.*?).\>", re.DOTALL)
      
    info = findHostRe.findall(file)  

    hostId = info[0][0]
    hostName = info[0][1].decode('utf-8')   
    
    print 'Account：' + passportDict['email'] + ' login success！'
    print 'Host name： ' + hostName
    print 
        
    fDict = {} 
    fDict[hostName] = ('', hostId)
    return (hostId, s, fDict)

def loginAct():
    passportDict = getPassWd()
    (id, s, fDict) = login( passportDict )

def main():
    loginAct()

if __name__ == '__main__':   
    main()