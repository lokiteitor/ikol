#!/usr/bin/env python3

import os
import string

class CleanString(object):
    """Buscar aquellos patrones que impidan el buen funcionamiento 
       de la clase ///"""
    def __init__(self,listfiles):
        # Recibe una lista con todos los archivos que seran filtrados
        self.listfiles = listfiles
        self.registro = []
        self.namelist = []
        self.nameref = []
        self.indiceref = {}
        self.nameclean = []
        self.indice = {}
        self.conjunto = {}
        self.keywords = []
        self.orden = []
        self.relacion = {}
        # Conjunto filtrado
        self.conjuntokey = {}

    def getNameClean(self,path):
        # Limpia el nombre del archivo de extenciones, puntaciones
        # y caracteres no ascii
        name = os.path.basename(path)
        name  = os.path.splitext(name)[0]

        for x in name:
            if not x in string.printable:
                name = name.replace(x,'')

        for i in string.punctuation:
            if i == '_':
                name = name.replace(i,' ')
            else:
                name = name.replace(i,'')

        return name

    def setNameClean(self):
        # limpia toda la lista de archivos
        for i in self.listfiles:
            self.nameclean.append(self.getNameClean(i))

        return self.nameclean
    def setSplitList(self):
        # TODO : Guardar una referencia a cada lista

        # Divide los nombres para agrupamiento
        for i in self.listfiles:
            name = self.getNameClean(i)
            name = name.lower()
            # refencia mayuscula-minuscula
            name = name.split()
            self.nameref.append((i," ".join(name)))

            self.namelist.append(name)
        return self.namelist

    def setData(self):
        # preparar el indice de palabras
        # Iterar sobre cada elemento de la lista split
        for i in self.namelist:
            for x in i:
                # agrega las coincidencias al diccionario
                self.getValue(x)

    def getValue(self,value):
        # obtener indice de referencia para cada palabra value
        #Lo almacena en un diccionario si la palabra no existe
        # en caso contrario agrega la ruta donde se encontro 
        if not value in self.indice.keys():
            self.indice[value] = []
            self.indiceref[value] = []

            for i in self.namelist:
                if value in i:
                    self.indice[value].append(i)
                    #agregar la cadena en otro indice
                    self.indiceref[value].append(self.buscarPath(i))

    def buscarPath(self,lst):
        name = " ".join(lst)

        for i in self.nameref:
            if name == i[1]:
                rtn = i[0]

        return rtn

    def getParents(self,lst):

        #Porcentaje 
        prc =  100 / len(lst)
        prv = 0

        asocc = []
        for i in lst:
            for x in self.indice[i]:
                prv = prc * self.getprc(lst,x)
                # Por encima de la moda

                if prv >= 70:
                    asocc.append(x)

        return asocc

    def getprc(self,lst,lstx):
        coin = 0
        for i in lst:
            for y in lstx:
                if i == y:
                    coin += 1

        return coin


        


        

