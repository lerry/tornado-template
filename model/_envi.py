#coding:utf-8

import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    #import logging
    #logging.basicConfig(
    #    level=logging.DEBUG,
    #    format='%(message)s\n',
    #    datefmt='%H:%M:%S',
    #)



from os.path import dirname, abspath, exists


PWD = abspath(__file__)
PREFIX = None
while True and len(PWD) > 1:
    PWD = dirname(PWD)
    if exists('%s/README.md'%PWD):
        PREFIX = PWD
        break

if PREFIX and PREFIX not in sys.path:
    sys.path.insert(0, PREFIX)    
#print sys.path
