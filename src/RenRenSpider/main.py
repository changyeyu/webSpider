#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/8
brief:        从网页抓取图片，之后保存到excel表格
author:      fish
'''

import sys
from _codecs import decode

from config import *
from getPassport import *
from login import *
from visit import *
from leaveMessage import *
from allFriendsImgToExcel import *

reload(sys)
sys.setdefaultencoding('utf-8')

def main():

    choiceDict = {
                  '1' : loginAct,
                  '2' : visitAct,
                  '3' : gossipAct,
                  '4' : getAllFriendsInfoAct,
                  '5' : sys.exit
                  }
        
    fDict = {'a':('xian','11'), 'b':('xian','22'), 'c':('Shenzhen','33'), 'd':('xian','44'),
             'e':('xian','55'), 'f':('xian','66'),  'g':('Shenzhen','77'), 'h':('xian','88')}
    
    print '''
            ==========    RenRen Spider    ==========
                     
            [1] Login my RenRen account
            [2] Login and Visit a friend
            [3] Login and Leave a message to a friend
            [4] Login and Get all my friends info 
                and head Image
            [5] ByeBye
            
          '''

    while True:
        try:
            choice = raw_input('Input your choice:')
            choiceDict[choice]()       
#            choiceDict.get(choice)()            
        except Exception,e:
            print 'Input Error!'
            print Exception,':',e
        else:
            break
    raw_input('\nPress to exit...')
if '__main__' == __name__:
    main()
    