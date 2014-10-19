#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/6
brief:        从网页抓取图片，之后保存到excel表格
author:        fish
'''

import re
import sys
import requests
import time

from _codecs import decode

from config import *
from login import login
from getPassport import *

reload(sys)
sys.setdefaultencoding('utf-8')
 
def getFriends(s, fDict):
    unicodeFlag = True
    count = 0

    #判断抓取的网页内编码是否已经是Unicode，如果是，则重新获取网页。因为本网页会随机返回Unicode或者其他编码      
    while(unicodeFlag):
        res = s.get('http://friend.renren.com/groupsdata')
        
        #编码为utf-8
        file = res.text.encode('utf-8') 
        with open(tmpDir + 'OriginalFriendGroup.txt','w+') as f:  
            f.write(file)  
            f.close()            
    
        reFriend = re.compile(r"fid.:(\d*?),.ti.*?large_url.{3}(.*?).,.*?" + 
                              "tiny_url...(.*?).,.*?fname.?:.(.*?).,.info.:.(.*?).,", re.DOTALL)             
        fList = reFriend.findall(file)  

        friendNum = fList.__len__()
    
        if '\u' == fList[0][3][:2]: 
            unicodeFlag = True
            WebspiderLogger.debug('the file is Unicode, need to try again')
        else:
            unicodeFlag = False
            
        count = count + 1
        
        print 'Wait for a while... Getting your friend list...'
            
        WebspiderLogger.debug('尝试获取好友列表次数：%d' % count)
        
    fData=open(tmpDir + 'friendInfo.txt','w+')    
    #从1开始，因为有host        
    for i in range(1, friendNum):
        '''
                            去除掉名字中除汉字之外的其他符号，以Unicode 值来匹配 所以先将name转换为Unicode
                            汉字：\u4E00-\u9fff
        '''
        name = fList[i][3]
        notChineseRe = re.compile(u'[\u0000-\u4DFF\u9fa6-\uffff]')
        
        #从’utf-8‘解码为Unicode
        name = name.decode('utf-8')                      
        name = re.sub(notChineseRe, '', name)

        #fDict[name] = (地址，id，大头像网址，小头像地址)
        fDict[name] = (fList[i][4].decode('utf-8'), fList[i][0].decode('utf-8'), 
                       fList[i][1].decode('utf-8'), fList[i][2].decode('utf-8'))
        
        WebspiderLogger.debug (name + '\t'*2 + fDict[name][0] + '\t' + fDict[name][1])  

        fData.write(name + '\t'*2 + fDict[name][0] + '\t'*2 + fDict[name][1] +
                     '\t'*2 + fDict[name][2] + '\t'*2 + fDict[name][3] + '\n')
          
    fData.close() 

    return fDict  
 
def visit(s, fDict):
    name = raw_input('\nInput the name who you want to visit:')
    #如果解码错误，自动切换编码
    try:
        name = name.decode('gb2312')
    except Exception:
        name = name.decode('utf-8')     
           
    id = fDict[name][1]
    profileUrl = 'http://www.renren.com/'+ id +'/profile'

    res = s.get(profileUrl) 
    print '\n踩  ' + name + ' 的主页成功!'  

def visitAct():
    #1.登陆
    passportDict = getPassWd()
    (hostName, hostId, s, fDict) = login(passportDict)
    
    #2.获取朋友列表 
    fDict = getFriends(s, fDict)
    
    #3.踩好友主页
    visit(s, fDict)
               
def main():
    visitAct()

if __name__ == '__main__':   
    main()