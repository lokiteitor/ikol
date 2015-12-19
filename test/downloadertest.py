#!/usr/bin/env python2.7
import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir+"/ikol")

import var

from  downloader.Downloader import Downloader



URL = "https://www.youtube.com/watch?v=8lp20JFiB4s"


D = Downloader(URL)

D.setCacheDir(var.CACHE_DIR)

print D.CACHE_DIR


# TODO :Esta parte genera un retardo y debera ser manejado con multihilo
D.setFormat(171)

print D.format

D.download()





