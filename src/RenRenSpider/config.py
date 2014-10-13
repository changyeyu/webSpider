#! /usr/bin/env python
#coding:utf-8

'''
date:        2014/10/6
brief：            keep the account and passwd
author:      fish
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