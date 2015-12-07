#!/usr/bin/env python3

import os
import sys


this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

import directory
import other_sort


mainpath = '/home/lokiteitor/Vídeos/Drumm and Bass'

def main():
    d = directory.Directorio(mainpath)
    clean = other_sort.CleanString(d.getListFiles())


    with open('out.log','w') as filelog:

        clean.setNameClean()
        filelog.write("\tLimpieza de nombres\n")
        for i in clean.nameclean:
            filelog.write(i+"\n")

        filelog.write("\tPreparacion de entorno de busqueda")
        clean.setSplitList()
        for i in clean.namelist:
            filelog.write("\n")
            filelog.write(str(i))

        filelog.write("\tPreparacion de datos\n")

        clean.setData()

        filelog.write("\tPreparacion indice de datos\n")

        for i in clean.indice.keys():
            filelog.write("valor: " + i + "\n")
            filelog.write(str(clean.indice[i])+"\n")
            filelog.write(str(len(clean.indice[i]))+"\n")


        filelog.write("\tCoincidencias\n")
        for i in clean.namelist:
            #import pdb; pdb.set_trace()
            filelog.write(str(clean.getParents(i))+"\n")



            

if __name__ == '__main__':
    main()
