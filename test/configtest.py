#!/usr/bin/env python2.7
import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir+"/ikol")


from config import Config

C = Config()

print C.getCacheDir()

C.setCacheDir(os.getcwd(),True)

print C.getCacheDir()

print C.getFormat()

C.setFormat(130,True)

print C.getFormat()


