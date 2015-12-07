#!/usr/bin/env python3

import os
import sys


this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

import directory
import sort


mainpath = '/home/lokiteitor/Vídeos/Drumm and Bass'

def main():
    d = directory.Directorio(mainpath)
    clean = sort.CleanString(d.getListFiles())


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

        filelog.write("\t Palabras clave\n")
        for i in clean.setKeywords():
            filelog.write(i+ " "+ str(len(clean.indice[i]))+"\n")


        # Hasta aqui todo bien

        filelog.write("\t Filtrado del Conjunto\n")
        clean.setConjunto()
        for i in clean.keywords:
            filelog.write("valor: " + i + "\n")

            filelog.write(str(clean.retirarKeywords(i))+"\n")



        filelog.write(str(clean.keywords))

        #Retirar en orden las palabras clave de los otros conjuntos
        filelog.write("\tReducir Conjunto\n")
        for i in clean.keywords:
            clean.reducirConjunto(i)


        for i in clean.keywords:
            filelog.write("valor: " + i + "\n")
            filelog.write(str(clean.conjuntokey[i])+"\n")




        # for i in clean.indiceref.keys():
        #     filelog.write("valor: " + i + "\n")            
        #     filelog.write(str(clean.indiceref[i])+ "\n")

        for x in clean.keywords:
            filelog.write("valor: " + x + "\n")
            filelog.write(str(clean.coincidir(x))+"\n")





        # filelog.write("\t Ordenando Conjunto\n")
        # clean.ordenarConjunto()
        # for x in clean.orden:
        #     filelog.write("valor: " + str(x) + "\n")
        # filelog.write("\tPreparacion de Conjunto\n")
        # clean.setConjunto()
        # clean.
        # for i in clean.conjunto.keys():
        #     filelog.write("valor: " + i + "\n")

        #     filelog.write(str(clean.conjunto[i])+"\n")
            

            

if __name__ == '__main__':
    main()
