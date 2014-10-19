#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/6
brief:        get the account and passwd
author:      fish
'''

import os
import sys
import re

from config import *

def getPassWd():

    passportDictDefault = {}
    
    try:
        with open(cfgDir + 'config.txt','r') as f:
            conf = f.read()
    except Exception:
        print 'No default password and account'
        pass
    else:
        conf = conf.encode('utf-8') 
        confReg = re.compile(r"email:(.*?)\spassword:(.*?)$")  
        info = confReg.findall(conf)  
        passportDictDefault['email']  = info[0][0]  
        passportDictDefault['passwd']  = info[0][1]
       
    passportDict = {}
    while True:
        passportDict['email'] = raw_input('Input your RenRen acount(\'Enter\' to use Default):')
        passportDict['passwd'] = raw_input('Input your RenRen passwd(\'Enter\' to use Default):')

        try:
            if ('' != passportDict['email']) and ('' != passportDict['passwd']):
                break            
            if ('' != passportDictDefault['email']) and ('' != passportDictDefault['passwd']):
                break
        except:
            continue
        else:
            break
        
    if '' == passportDict['email']:
        passportDict['email'] = passportDictDefault['email']
    if '' == passportDict['passwd']:
        passportDict['passwd'] = passportDictDefault['passwd'] 
        print 'Nothing input, It will use the defualt passport'
    #保存账户名，密码   
    else:
        with open(cfgDir + 'config.txt','w') as f:
            conf = f.write('email:' + passportDict['email'] + '\n' +
                           'password:' + passportDict['passwd']) 
            
        print 'Your password and account saved here: '
        print os.path.dirname(__file__) + cfgDir + 'config.txt' 
            
    return passportDict

def main():
    getPassWd()

if __name__ == '__main__':   
    main()