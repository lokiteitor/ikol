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
import shutil
import string

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

        if not os.path.exists(path):
            os.mkdir(self.path)

    def getListSubDirectory(self):
        # obtener la lista de los subdirectorios en el primer nivel
        for x in os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path,x)):
                self.dirs.append(os.path.join(self.path,x))

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
        if os.path.exists(path) and os.path.isdir(path):
            if path in self.dirs:
                newdir = Directorio(path)
        else:
            os.mkdir(path)
            if os.path.dirname(path) == self.path:
                self.dirs.append(path)
            else:
                self.associate.append(path)

        return newdir
            
    def createSubDir(self,pathdir):
        # TODO : que pasa si pathdir es  path relativo
        if pathdir[0:len(self.path)] == self.path:
            if not os.path.exists(pathdir):
                os.mkdir(pathdir)
            else:
                # TODO : registrarlo en el log
                print("El directorio %s ya existe",pathdir)
        else:
            # TODO : lanzar excepcion
            print("El directorio %s esta fuera del alcanze del objeto",pathdir)

    def getListFiles(self):
        # Obtener lista de archivos en el primer nivel
        self.files = [] 
        for i in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,i)):
                self.files.append(os.path.join(self.path,i))
        return self.files

    def getBaseFiles(self):
        lst = []
        for i in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,i)):
                lst.append(i)
        return lst

    def FileinDir(self,name):
        if name in self.getBaseFiles():
            path = os.path.join(self.path,name)
        else:
            path = False

        return path    

    def createFile(self,path,msj=None,rw="w"):
        # Crear un archivo con msj como contenido
        # si msj es None crear solo un archivo vacio
        # rw el modo de lectura/escritura

        with open(path,rw) as fl:
            if msj and str(type(msj)) == "<type 'list'>":
                for i in msj:
                    fl.write(i+"\n")
            elif msj and str(type(msj)) == "<type 'str'>":
                fl.write(msj + "\n")


    def CleanName(self,path):
        # Limpia el nombre del archivo de extenciones, puntaciones
        # y caracteres no ascii
        name = os.path.basename(path)
        ext = os.path.splitext(name)[1]
        name  = os.path.splitext(name)[0]
        for x in name:
            if not x in string.printable:
                name = name.replace(x,'')

        for i in string.punctuation:
            if i == '_':
                name = name.replace(i,' ')
            else:
                name = name.replace(i,'')

        newpath = os.path.dirname(path) + "/" + name + ext
        # TODO : Implementar Filtro de palabras
        shutil.move(path,newpath)

        return newpath
    def moveToDest(self,orig,dest):
        
        if not os.path.exists(dest):
            try:
                os.mkdir(dest)
            except Exception, e:
                raise e

        shutil.move(orig,dest)

        return os.path.join(dest,os.path.basename(orig))