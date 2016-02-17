#!/usr/bin/env python2.7

import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

from ikol.youtube.APIRequest import APIRequest
from ikol.youtube.Auth import Authorized

conf = trunk_dir + "/conf/client_secret.json"

sto = trunk_dir + "/conf/oauth.json"

A = Authorized(conf)

A.getFlow()

A.setStorage(sto)

srv = A.getService()

API = APIRequest(srv)

print API.getPlaylists()


#lst = API.getVideosList(API.lstplaylists[5][1])
lst = API.getVideosList("PL3318306AE34218BC")

print lst

print len(lst)


print API.getSecondPeer(API.getPlaylists())

for i in API.getPlaylists():
    print API.getNameList(i[1])

print API.getNameList("PL3318306AE34218BC")

