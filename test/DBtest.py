#!/usr/bin/env python2.7
import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

from ikol.dbregister import DataBase
from ikol import var



if os.path.exists(var.DB_PATH):
    os.remove(var.DB_PATH)

DB = DataBase(var.DB_PATH)


DB.insertPlaylist("loLWOCl7nlk","test")
DB.insertPlaylist("loLWO357nlk","testb")

DB.insertVideo("KDk2341oEQQ","loLWOCl7nlk","test")
DB.insertVideo("KDktIWeoE23","loLWOCl7nlk","testb")

print DB.getAllVideosByPlaylist("loLWOCl7nlk")
print DB.getVideoById("KDk2341oEQQ")