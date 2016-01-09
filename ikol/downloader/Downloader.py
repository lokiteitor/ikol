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

from subprocess import Popen,PIPE
import string
import logging

import var



class Downloader(object):
    """Objeto que realiza el seguimiento del video desde su descarga hasta 
    su Almacenamiento, pasando por la conversion, no realiza el tageo"""
    def __init__(self, URL):
        super(Downloader, self).__init__()
        self.URL = URL
        self.CACHE_DIR = var.CACHE_DIR
        self.PATH_TO_FILE = self.CACHE_DIR

        self.formatAvailable = []
        self.format = var.FORMAT_DEFAULT
        # lista de extenciones disponibles
        self.extAvailable = []
        self.ext = ""
        self.formatopt = [""]


    def setCacheDir(self,path):
        # Para funcionar se debe proprocionar un directorio
        # donde almacenar los videos que se esten descargando}
        # De la opcion %id se puede obtener el nombre
        self.CACHE_DIR = path
        cachedir = self.CACHE_DIR + "/%(title)s.%(ext)s"

        self.PATH_TO_FILE = cachedir


    def setFormat(self,format):
        # Establece un formato diferente al de defecto}


        Procss = Popen(["youtube-dl","-F",self.URL],stdout=PIPE)
        rest = Procss.stdout.read()
        req = rest.split("\n")

        # index
        ind = []


        # dividir la cadena por saltos de linea 
        # luego contar hasta la primera linea que empieze con exactamente un numero

        for i in req:
            try:
                for x in i.split()[0]:
                    if not x in string.digits:
                        no  = False
                        break
                    # TODO : posiblemente genere errores
                    no = True

                if no:
                    y = req.index(i)
                    ind.append(y)
                    self.formatAvailable.append(int(req[y].split()[0]))
                    self.extAvailable.append(req[y].split()[1])
                # Si llega hasta aqui debo encontrar el indice
            except Exception, e:
                # TODO : genera un error Index manejarlo
                logging.debug(str(e) + str(i))
                break
                print e

        if format in self.formatAvailable:
            self.format = format
            self.ext = self.extAvailable[self.formatAvailable.index(format)]
        elif var.FORMAT_DEFAULT in self.formatAvailable:
            self.format = var.FORMAT_DEFAULT
            self.ext = self.extAvailable[self.formatAvailable.index(self.format)]
        else:
            self.format = self.formatAvailable[0]
            self.ext = self.extAvailable[0]

    def download(self):
        #devuelve el nombre del archivo
        P = Popen(["youtube-dl","-o",self.PATH_TO_FILE,"-f",str(self.format),
            "-ci",self.URL],stdout=PIPE)
        if P.wait() == 0:
            codereturn = True
        else:
            logging.debug(P.stdout.read())
            codereturn = False

        print P.stdout.read()

        return codereturn        