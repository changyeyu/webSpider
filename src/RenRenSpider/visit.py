#! /usr/bin/env python
#coding:utf-8

'''
Created on 2014年10月6日

@author: fish
'''
import re
import re 
import sys
import requests
import time
from _codecs import decode
from login import login

reload(sys)
sys.setdefaultencoding('utf-8')
 
def getFriends(s, fDict):
    
    unicodeFlag = True
    count = 0
    #判断抓取的网页内编码是否已经是Unicode，如果是，则重新获取网页。因为本网页会随机返回Unicode或者其他编码 
    
    fData=open('E:\\python\\tmp\\doc\\fData.txt','w+')      
    while(unicodeFlag):
        res = s.get('http://friend.renren.com/groupsdata')
        
        #编码为utf-8
        file = res.text.encode('utf-8') 
        
        f=open('E:\\python\\tmp\\doc\\1.txt','w+')  
        f.write(file)  
        f.close()      
        
        f = open('E:\\python\\tmp\\doc\\1.txt','r+')  
        reFriend = re.compile(r"fid.?:(\d*?),.?ti.*?fname.?:.?(.*?).?,.?info.?:.?(.*?).?,", re.DOTALL)  
        
        fList = reFriend.findall(f.read())
        


        friendNum = fList.__len__()
    
        if '\u' == fList[0][1][:2]: 
            unicodeFlag = True
            time.sleep(0.1)
        else:
            unicodeFlag = False
            
        count = count + 1
        print '获取好友列表次数：', count
    
    #从1开始，因为有host        
    for i in range(1, friendNum):
        '''
                            去除掉名字中除汉字之外的其他符号，以Unicode 值来匹配 所以先将name转换为Unicode
                            汉字：\u4E00-\u9fff
        '''
        name = fList[i][1]
        notChineseRe = re.compile(u'[\u0000-\u4DFF\u9fa6-\uffff]')
        
        #从’utf-8‘解码为Unicode
        name = name.decode('utf-8')                      
        name = re.sub(notChineseRe, '', name)

        fDict[name] = (fList[i][2].decode('utf-8'), fList[i][0].decode('utf-8'))
        
        print (name + '\t'*2 + fDict[name][0] + '\t' + fDict[name][1])  

        fData.write(name + '\t'*2 + fDict[name][0] + '\t'*2 + fDict[name][1] + '\n')
          
    fData.close() 
    f.close()
    
    return fDict  
 
def visit(s, fDict):

    name = raw_input('Input the name who you want to visit:')
    name = name.decode('utf-8')
    id = fDict[name][1]
    profileUrl = 'http://www.renren.com/'+ id +'/profile'
    
    res = s.get(profileUrl) 
    print '踩  ' + name + ' 的主页成功!'  

def visitAct():
    #1.登陆
    (hostId, s, fDict) = login()
    
    #2.获取朋友列表 
    fDict = getFriends(s, fDict)
    
    #3.踩好友主页
    visit(s, fDict)
               
def main():
    visitAct()

if __name__ == '__main__':   
    main()