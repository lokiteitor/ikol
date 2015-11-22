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
import sys
import getopt


# Clase que representa un directorio y que su funcion es toda la
# gestion de los ficheros

class Directorio(object):
    """Clase que representa un directorio y que su funcion es toda la
        gestion de los ficheros"""
    def __init__(self, path):
        super(Directorio, self).__init__()
        self.path = path
        self.dirs = []
        self.files = []
        self.associate = []

        if os.path.exists(path):
            self.exist = True
        else:
            self.exist = False

    def create(self):
        # si el directorio no existe crearlo
        if not self.exist:
            os.mkdir(self.path)

    def getListSubDirectory(self):
        # obtener la lista de los subdirectorios en el primer nivel
        for x in os.listdir(self.path):
            if os.path.isdir(os.path.join(os.getcwd(),x)):
                self.dirs.append(os.path.join(os.getcwd(),x))

        return self.dirs
        
    def getAllListSubDirectory(self):
        # Obtener todos los subniveles
        for root, dirs, files in os.walk(self.path):
            for i in dirs:
                self.dirs.append(os.path.join(root,i))

        return self.dirs

    def deleteFile(self,f):
        # Borrar archivos
        # el nombre del archivo debe de estar de la forma absolute path
        if os.path.exist(f) and os.path.isfile(f):
            os.remove(f)
            self.files.remove(f)
        else:
            #TODO lanzar error y registrarlo en el log
            pass
    def getDirectory(self,path):
        # Para moverse entre subdirectorios forzamente debe 
        # de usarse este metodo que devuelve un objeto Directorio
        if os.path.exist(path) and os.path.isdir(path):
            if path in self.dirs:
                newdir = Directorio(path)
        else:
            os.mkdir(path)
            if os.path.dirname(path) == self.path:
                self.dirs.append(path)
            else:
                self.associate.append(path)

        return newdir
            
    def createDir(self):
        pass

    def moveFile(self):
        pass

            



if __name__ == '__main__':
    # leer los argumentos
    # -C: --clean= : limpiar archivos repetidos -> CleanRepeat
    #       @requiere un directorio sobre el que actuar
    # -c:--convert= : convertir de video a audio -> Convert
    #       @directorio donde se encuentran los videos
    try:
        options,arg = getopt.getopt(sys.argv[1:], "Cch:",["clean=:","convert=","help"])
        
    except getopt.GetoptError:
        #TODO : Imprimir menu de ayuda
        print("""\
Uso: musicmanager [opciones] FUENTE DESTINO""")

    for opt, arg in options:
        if opt in ("-C" , "--clean"):
            if arg:
                #TODO Implementacion de limpieza de archivos
                #       con un directorio objetivo predefenido
                pass
            else:
                #TODO Usar Fuente
                pass
        if opt in ("-c" , "--convert"):
            if arg:
                #TODO Implementacion de conversion de archivos
                pass
            else:
                #TODO usar fuente
                pass
        if opt in ("--h","--help"):
            #TODO imprimir menu de ayuda
            pass


