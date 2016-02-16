#!/usr/bin/env python2.7
import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

from ikol.downloader.Convert import Convert
from ikol import var





for i in os.listdir(var.FINAL_DIR):
    # Necesita funcion recursiva
    #  o path.walk

    if os.path.isdir(os.path.join(var.FINAL_DIR,i)):
        dirp = os.path.join(var.FINAL_DIR,i)
        for x in os.listdir(dirp):
            D = Convert(os.path.join(dirp,x))
            print D.path                        
            print D.getBinary()
            print D.setConfig("mp3","256K")

            D.convert()


