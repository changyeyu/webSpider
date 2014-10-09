#! /usr/bin/env python
#coding:utf-8

'''
Created on 2014年10月6日
功能：账户名、密码
@author: fish
'''
def getPassWd():

    passportDictDefault ={
                           'email': '',
                           'passwd': ''
                           }
    passportDict={}
    
    passportDict['email'] = raw_input('Input your RenRen acount(\'Enter\' to use Default):')
    passportDict['passwd'] = raw_input('Input your RenRen passwd(\'Enter\' to use Default):')  
      
    if '' == passportDict['email']:
        passportDict['email'] = passportDictDefault['email']
    if '' == passportDict['passwd']:
        passportDict['passwd'] = passportDictDefault['passwd']    
    
    return passportDict

def main():
    getPassWd()

if __name__ == '__main__':   
    main()