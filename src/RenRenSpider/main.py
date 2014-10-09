#-*- coding: utf-8 -*-
#usr/bin/env python
'''
Created on 2014-10-8
功能：主程序
@author: fish
'''

def main():
    imgUrl = 'http://www.baidu.com/img/bd_logo1.png'
    tmpDir = '.\\tmp\\'
    imgDir = tmpDir + '\\img\\'
        
    fDict = {'a':('xian','11'), 'b':('xian','22'), 'c':('Shenzhen','33'), 'd':('xian','44'),
             'e':('xian','55'), 'f':('xian','66'),  'g':('Shenzhen','77'), 'h':('xian','88')}
    
    print ''
        
    print '''
            ==========    RenRen Spider    ==========
                     
            [1] Login my RenRen account
            [2] Login and Visit a friend
            [3] Login and Leave a message to a friend
            [4] Login and Get all my friends info 
                and head Image
            [5] ByeBye
          '''
    choice = raw_input('Input your choice:')
    while((choice < '1') or (choice > '5')):
        choice = raw_input('Input Error! Input your choice again:')
    choiceDict = {
                  '1' : login()
                  '2' : visit()
                  '3' : gossip()
                  '4' : getAllFriendsInfo()
                  '5' : exit()
                  }
    choiceDict[choice]
    
    hostName = '主人'
    getAllFriendsInfo(tmpDir, imgDir, hostName, fDict)
    
if '__main__' == __name__:
    main()
    