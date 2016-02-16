#!/usr/bin/env python2.7
import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)


from ikol.config import Config

C = Config()

print C.getCacheDir()

C.setCacheDir(os.getcwd(),True)

print C.getCacheDir()

print C.getFormat()

C.setFormat(130,True)

print C.getFormat()

URL = "https://www.youtube.com/watch?v=8lp20JFiB4s"

C.addURL(URL)
C.addURL(URL)

lst = C.getAllURL()

for i in lst:
    print i


print C.getCodec()
print C.getKbps()


