#!/usr/bin/env python2.7

import os
import sys


this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir+"/src")


from youtube import Auth
from youtube import APIRequest


conf = trunk_dir + "/conf/client_secret.json"

sto = trunk_dir + "/conf/oauth.json"

A = Auth.Authorized(conf)

A.getFlow()

A.setStorage(sto)

srv = A.getService()

API = APIRequest.APIRequest(srv)

print API.getPlaylists()


lst = API.getVideosList(API.lstplaylists[5][1])

print lst

print len(lst)

print API.videos

print API.FormatLst(lst)