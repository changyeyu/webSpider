#! /usr/bin/env python
#coding:utf-8
'''
date:        2014/10/6
brief:         the global settings
author:      fish
'''
import logging 

tmpDir = '.\\tmp\\'
imgDir = tmpDir + 'img\\'
photoDir = tmpDir + 'photo\\'
cfgDir = tmpDir + 'config\\' 
logDir = tmpDir + 'log\\'

WebspiderLogger = logging.getLogger('WebspiderLogger')
WebspiderLogger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler(logDir + 'WebspiderLogger.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.CRITICAL)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
WebspiderLogger.addHandler(fh)
WebspiderLogger.addHandler(ch)






