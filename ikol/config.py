# -*- coding: utf-8 -*-

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
from ConfigParser import ConfigParser

import directory
import var



class Config(directory.Directorio):
    """Permite obtener toda clase de configuracion desde la linea
    de comandos, el fichero de constantes y/o el archivo de 
    configuracion"""
    def __init__(self):
        super(Config, self).__init__(var.CONFIG_DIR)
        if not os.path.exists(var.CONFIG_DIR):
            os.makedirs(var.CONFIG_DIR)
        if not os.path.exists(var.CACHE_DIR):
            os.makedirs(var.CACHE_DIR)

        # Archivos basicos
        self.ConfDir = var.CONFIG_DIR
        self.client_secret = var.CLIENT_SECRETS_FILE
        self.storage_path = var.CODE_STORAGE
        self.config_file = var.CONFIG_FILE
        self.url_file = var.URL_FILE
        # si el usuario marco manualmente una configuracion no persistente verlo
        # aqui
        # CACHE_DIR,URL_FILE,FORMAT_DEFAULT,FINAL_DIR,Codec,kbps
        self.reg = [False,False,False,False,False,False]
        # Opciones
        self.format = var.FORMAT_DEFAULT
        self.codec = var.CODEC_DEFAULT

        # revisar la integridad antes de continuar
        self._CheckDirectory()
        self.cfgfile = ConfigParser()
        self.cfgfile.read(self.config_file)
        # Si todo esta bien requerir las configuraciones hechas por el
        # usuario en el archivo de configuracion

        # Directorios secundarios
        # TODO : si se establece manualmente revisar que no se sobrepongan
        self.CACHE_DIR = self.getCacheDir()
        self.FINAL_DIR = self.getFinalDir()



    def _CheckDirectory(self):
        # Registro: (Client_secret,Archivo de Configuracion,URL.conf)
        check = [False,False,False]
        for i in self.getListFiles():
            if i == self.client_secret:
                check[0] = True
            if i == self.config_file:
                check[1] = True
            if i == self.url_file:
                check[2] = True

        if check[0] == False:
            raise AttributeError("No se encontro el archivo con la clave API")
        if check[1] == False:
            self.createFile(self.config_file,var.CONFIG_DEFAULT,rw="w")

        if check[2] == False:
            self.createFile(self.url_file,rw="w")


    def getCacheDir(self):
        if self.reg[0]:
            # Si el usuario lo modifico no hacer nada y dar la respuesta de 
            # usuario
            pass
        elif self.cfgfile.has_option("DIRECTORIOS","CACHE_DIR"):
            self.CACHE_DIR = self.cfgfile.get("DIRECTORIOS","CACHE_DIR")

        else:
            # si no la dio ni esta en fichero de configuracion
            self.cfgfile.set("DIRECTORIOS","CACHE_DIR",var.CACHE_DIR)

        return self.CACHE_DIR

    def setCacheDir(self,path,flag=False):
        self.reg[0] = True
        if not os.path.exists(path):
            os.mkdir(path)
        # si se debe establecer por persistente 
        self.CACHE_DIR = path
        if flag:
            self.cfgfile.set("DIRECTORIOS","CACHE_DIR",path)
            with open(self.config_file,"w") as f:
                self.cfgfile.write(f)

        return self.CACHE_DIR

    def getFormat(self):
        if self.reg[2]:
            pass
        elif self.cfgfile.has_option("OPCIONES","FORMAT_DEFAULT"):
            self.format = self.cfgfile.getint("OPCIONES","FORMAT_DEFAULT")

        else:
            self.cfgfile.set("OPCIONES","FORMAT_DEFAULT",var.FORMAT_DEFAULT)

        return self.format

    def setFormat(self,nformat,flag=False):
        self.reg[2] = True
        self.format = nformat
        if flag:
            self.cfgfile.set("OPCIONES","FORMAT_DEFAULT",nformat)
            with open(self.config_file,"w") as f:
                self.cfgfile.write(f)

        return self.format

    def setFinalDir(self,path,flag=False):
        self.reg[3] = True
        if not os.path.exists(path):
            os.mkdir(path)
        # si se debe establecer por persistente 
        self.FINAL_DIR = path
        if flag:
            self.cfgfile.set("DIRECTORIOS","FINAL_DIR",path)
            with open(self.config_file,"w") as f:
                self.cfgfile.write(f)

        return self.FINAL_DIR

    def getFinalDir(self):
        if self.reg[3]:
            # Si el usuario lo modifico no hacer nada y dar la respuesta de 
            # usuario
            pass
        elif self.cfgfile.has_option("DIRECTORIOS","FINAL_DIR"):
            self.FINAL_DIR = self.cfgfile.get("DIRECTORIOS","FINAL_DIR")

        else:
            # si no la dio ni esta en fichero de configuracion
            self.cfgfile.set("DIRECTORIOS","FINAL_DIR",var.FINAL_DIR)
            self.FINAL_DIR = var.FINAL_DIR

        return self.FINAL_DIR


    def addURL(self,URL):
        # TODO : Revisar integridad del URL 
        lst = self.getAllURL()

        if URL in lst:
            dup = True
        else:
            dup = False

        with open(self.url_file,"a") as f:
            if dup == False:
                f.write(URL+"\n")

    def getAllURL(self):
        # Devolver una lista con las url
        urllist = []
        try:
            with open(self.url_file,"r") as f:
                while True:
                    url = f.readline()
                    if not url:
                        break
                    url = url.replace("\n","")
                    if len(url) > 0:
                        urllist.append(url)

            return urllist

        except Exception, e:
            # TODO: Lanzar aviso y log
            print e
            # crear el archivo
            self.createFile(self.url_file,rw="w")
            return []

    def getDelWrongList(self):
        
        if self.cfgfile.has_option("OPCIONES","DELETE_WRONG_LIST"):
            self.DELETE_WRONG_LIST = self.cfgfile.get("OPCIONES","DELETE_WRONG_LIST")

        else:
            # si no  esta en fichero de configuracion
            self.cfgfile.set("OPCIONES","DELETE_WRONG_LIST","YES")

        return self.DELETE_WRONG_LIST

    def getLogFile(self):
        return var.LOG_FILE

    def getCodec(self):
        if self.reg[4]:
            pass
        elif self.cfgfile.has_option("OPCIONES","CODEC_DEFAULT"):
            self.codec = self.cfgfile.get("OPCIONES","CODEC_DEFAULT")

        else:
            self.cfgfile.set("OPCIONES","CODEC_DEFAULT",var.CODEC_DEFAULT)
            self.codec = var.CODEC_DEFAULT
        return self.codec

    def setCodec(self,codec,flag=False):
        self.reg[4] = True
        self.codec = codec
        if flag:
            self.cfgfile.set("OPCIONES","CODEC_DEFAULT",codec)
            with open(self.config_file,"w") as f:
                self.cfgfile.write(f)

        return self.codec

    def getKbps(self):
        if self.reg[5]:
            pass
        elif self.cfgfile.has_option("OPCIONES","KBPS"):
            self.kpbs = self.cfgfile.get("OPCIONES","KBPS")

        else:
            self.cfgfile.set("OPCIONES","KBPS",var.KBPS)
            self.kpbs = var.KBPS
        return self.kpbs

    def setKbps(self,kpbs,flag=False):
        self.reg[5] = True
        self.kpbs = kpbs
        if flag:
            self.cfgfile.set("OPCIONES","KBPS",kpbs)
            with open(self.config_file,"w") as f:
                self.cfgfile.write(f)

        return self.kpbs