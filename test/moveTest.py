#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
import sys
this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

from ikol.config import Config
from ikol.directory import Directorio

config = Config()


def moveToDest(listfiles,dircache):
    # Mover los archivos correctos al directorio destino
    D = Directorio(dircache)
    dest = os.path.join(config.getFinalDir(),os.path.basename(dircache))

    for i in listfiles:
        if D.FileinDir(i):
            i = D.FileinDir(i)
            # Renombrar el archivo para Filtrar Caracteres non-ascii
            i = D.CleanName(i)
            try:

                print "Moviendo "+ D.path +" hacia " + dest
                D.moveToDest(i,dest)
            except Exception, e:
                #TODO : hacer algo con este error decode ascii en print
                print e

        else:
            print "Error Al buscar el archivo " + i

if __name__ == '__main__':
    lst = os.listdir(config.getCacheDir())

    for i in lst:
        print i
        if os.path.isdir(os.path.join(config.getCacheDir(),i)):
            files = os.listdir(os.path.join(config.getCacheDir(),i))
            print files
            moveToDest(files,os.path.join(config.getCacheDir(),i))