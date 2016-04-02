#!/usr/bin/env python2.7

import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

from ikol import tag

Rtag = tag.ReaderJSON("tags.json")

print Rtag.getArtista()

Tag = tag.Tag(os.path.join(os.getcwd(),'Musica'),'mp3')

print Tag.getStatus();

print Tag.loadMusicFiles()

Tag.setTags()