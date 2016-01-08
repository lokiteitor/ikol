#!/usr/bin/env python3

#Copyright (C) 2015  David Delgado Hernandez 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



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

    # TODO : aun no funciona
    def setData(self):
        # preparar el indice de palabras
        # Iterar sobre cada elemento de la lista split
        for i in self.namelist:
            for x in i:
                # agrega las coincidencias al diccionario
                self.getValue(x)
        

    def setKeywords(self):
        # preparar palabras clave con mayor aparicion
        for i in self.indice.keys():
            if len(self.indice[i]) >= 2:
                self.keywords.append(i)

        self.keywords =  self.ordenarKeywords()

        return self.keywords

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

    def setConjunto(self):
        # Fusiona las lista y prepara un conjunto con los resultados
        for i in self.indice.keys():
            lst = []
            for x in  self.indice[i]:
                lst.extend(x)
            self.conjunto[i] = set(lst)
        return self.conjunto

    def retirarKeywords(self,value):
        # Retirar del conjunto la palabras que no sean clave
        lstdel = []
        conjunto = self.conjunto
        for i in self.conjunto[value]:
            if not i in self.keywords:
                lstdel.append(i)
            if i == value:
                lstdel.append(i)

        for x in lstdel:
            conjunto[value].remove(x)

        self.conjuntokey[value] = conjunto[value]
        return conjunto[value]


    def ordenarKeywords(self):
        # Ordena los conjuntos del que tiene menor longitud al mayor
        ordenkey = []
        lst = []
        for i in self.keywords:
            ordenkey.append((i,len(self.indice[i])))

        ordenkey.sort(key = self.getNumber)

        for i in ordenkey:
            lst.append(i[0])

        return lst


    def getNumber(self,n):
        return n[1]


    def reducirConjunto(self,value):
        #value es una palabra clave

        for x in self.conjuntokey[value]:
                if value in self.conjuntokey[x]:
                    self.conjuntokey[x].remove(value)


    def coincidir(self,value):
        # iterar sobre los elementos del conjuntokey
        lst1 = self.indiceref[value]
        same = []
        for x in self.conjuntokey[value]:
            #buscar coincidencias en ambas listas
            lst2 = self.indiceref[x]

            for i in lst1:
                for y in lst2:
                    if i == y:
                        same.append(y)

        return same


