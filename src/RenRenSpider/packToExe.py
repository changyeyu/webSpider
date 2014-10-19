#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/8
brief:        打包为exe
                   例如：python packToExe.py py2exe
author:      fish
'''

from distutils.core import setup  
import py2exe  
  
includes = ["encodings", "encodings.*"]  
  
setup(  
    console = ["__init__.py", "allFriendsImgToExcel.py", "config.py",
              "getPassport.py","leaveMessage.py","login.py","main.py",
              "visit.py"],  
    )  
