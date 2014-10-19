#-*- coding: utf-8 -*-
#usr/bin/env python
'''
date:        2014/10/8
brief:        从网页抓取图片，之后保存到excel表格
author:      fish
'''

import os
import sys
import Image
import requests
from xlrd import *
from xlwt import *
from _codecs import decode

from config import *
from getPassport import *
from login import *
from visit import *
from leaveMessage import *
from random import choice
'''
    PIL 图形处理库：
    Windows 下，下载 PIL for Windows only不然会提醒：pil IOError: decoder zip not available
    Linux下，下载 all platforms，需要安装apt-get install libjpeg8 
    libjpeg62-dev libfreetype6 libfreetype6-dev
'''

reload(sys)
sys.setdefaultencoding('utf-8')

def saveImg(imgUrl, imgDir, friendId):
    '''
    brief：从网页抓取好友小头像并保存至本地
    '''
    file = requests.get(imgUrl)

    with open(imgDir + friendId + '.jpg', 'wb') as f:
        f.write(file.content)
        f.close()
#     im = Image.open(imgDir + friendId + '.bmp')    
#     im.save(imgDir + friendId + '.bmp', "bmp" )        

def cvtImg(photoUrl, photoDir, imgDir, friendId, friendName):
    '''
    brief：转换图片格式，用于Excel表格保存
    '''
    try:
        im = Image.open(photoDir + friendName + '.jpg')    
        im.save(imgDir + friendId + '.bmp', "bmp" ) 
    except Exception:
        pass
    
def savePhoto(photoUrl, photoDir, friendName):
    '''
    brief：从网页抓取好友大图并保存至本地
    '''
    file = requests.get(photoUrl)

    with open(photoDir + friendName + '.jpg', 'wb') as f:
        f.write(file.content)
        f.close()

def saveToExcel(tmpDir, imgDir, hostName, fDict):
    '''
    brief：将图片保存到excel表格
                    参考百度文库：python使用xlwt编辑excel
    '''
    maxColNum = 6
    
    #兼容中文
    friendWorkBook = Workbook('utf-8')
    
    #创建excel表格中的sheet表格栏 ，并命名   
    sheet = friendWorkBook.add_sheet('friend')

    #标题文字cell样式
    titleFont = Font()
    titleFont.height = 500
    titleAlignment = Alignment()
    titleAlignment.horz = Alignment.HORZ_CENTER
    titleAlignment.vert = Alignment.VERT_CENTER
    titleStyle = XFStyle()
    titleStyle.font = titleFont
    titleStyle.alignment = titleAlignment
        
    #图片cell样式
    font = Font()
    font.height = 2000
    alignment = Alignment()
    alignment.horz = Alignment.HORZ_CENTER
    alignment.vert = Alignment.VERT_CENTER
    style = XFStyle()
    style.font = font
    style.alignment = alignment

    #正文文字cell样式
    textFont = Font()
    textFont.height = 260
    textAlignment = Alignment()
    textAlignment.horz = Alignment.HORZ_CENTER
    textAlignment.vert = Alignment.VERT_CENTER
    textStyle = XFStyle()
    textStyle.font = textFont
    textStyle.alignment = textAlignment
    
    #创建标题
    sheet.write_merge(0, 0, 0, maxColNum, hostName + '的好友', titleStyle)
    
    #图片占用cell大小设置，cell高度不能直接设置，所以通过font.height来设置，并写入空字符。    
    for i in range(0, maxColNum):    
        sheet.col(i).width = 6666   
        
    #插入图片 
    count = 0 
    rowNum = 1
    colNum = 0    
    for name in fDict:
        count = count + 1
        friendId = fDict[name][1]
        friendPlace = fDict[name][0] 
        sheet.write(rowNum, colNum, '', style)
        #sheet.insert_bitmap(图片, 行, 列, 图片向下偏移, 图片向右偏移, 横向缩放, 纵向缩放)  
        try: 
            sheet.insert_bitmap(imgDir + friendId + '.bmp', rowNum, colNum, 2, 2, 1, 1)      
        except Exception:
            pass
        
        #图片下方注释
        sheet.write((rowNum + 1), colNum, (str(count) + '. ' + name +  ' ' + friendPlace), textStyle)
        
        #行与列计算
        colNum = count % maxColNum
        if 0 == colNum:
            rowNum = rowNum + 2

    #保存excel表格
    friendWorkBook.save(tmpDir + hostName + u'的人人网好友.xls')

    print 'Your friends list saved to: '
    print os.path.dirname(__file__) + tmpDir + hostName + '的人人网好友.xls'
    print '\n打开Excel表格:' + hostName + '的人人网好友.xls' + '  吗?'
    choice = raw_input('(\'y\' or \'n\'):')
    if 'y' == choice:
        os.startfile(tmpDir + hostName + '的人人网好友.xls')
    
def imgProcess(imgDir, friendId):
    '''
    brief：将图片转为为24位bmp位图，因为xlwt只支持这种格式
    '''
    try:
        im = Image.open(imgDir + friendId + '.bmp')
        im = im.resize((160, 160))
        out = im.convert('RGB')
        out.save(imgDir + friendId + '.bmp')
    except Exception:
        pass

def getAllFriendsInfo(tmpDir, imgDir, hostName, fDict):
    '''
    brief：抓取所有好友的图片等信息
    '''

    friendNum = len(fDict)
    count = 0
    for name in fDict:
        friendId = fDict[name][1]
        friendName = name
        friendInfo = fDict[name][0]
        
        #用于Excel表格存储的小头像
        imgUrl = fDict[name][3]
#         saveImg(imgUrl, imgDir, friendId)
         
        #好友大图
        photoUrl = fDict[name][2]
        savePhoto(photoUrl, photoDir, friendName)
        
        cvtImg(photoUrl, photoDir, imgDir, friendId, friendName)
        
        print ('Saving friend photo : (%.2f %%)'%(100.00 * count/friendNum)), name  
            
        imgProcess(imgDir, friendId)
        count = count + 1
        
    print 'Total: ' + str( count ) + 'friends\' photo have been saved!' 

    print 'Your friends photo saved to: '
    print os.path.dirname(__file__) + photoDir
    print '=' * 40    
    
    print '\nWait for a while... Your friend Excel table is cooking...'   
    saveToExcel(tmpDir, imgDir, hostName, fDict)   
    
    #打开好友大图文件夹
    os.startfile(photoDir)

def getAllFriendsInfoAct():
    #1.登陆
    passportDict = getPassWd()
    (hostName, hostId, s, fDict) = login(passportDict)
    
    #2.获取朋友列表 
    fDict = getFriends(s, fDict)
    
    #3.保存好友信息,删除自己
    del fDict[hostName]
    getAllFriendsInfo(tmpDir, imgDir, hostName, fDict)    

def main():
    getAllFriendsInfoAct() 
    
if '__main__' == __name__:
    main()
    
    