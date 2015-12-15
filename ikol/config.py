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
        # Archivos basicos
        self.ConfDir = var.CONFIG_DIR
        self.client_secret = var.CLIENT_SECRETS_FILE
        self.storage_path = var.CODE_STORAGE
        self.config_file = var.CONFIG_FILE

        # revisar la integridad antes de continuar
        self.CheckDirectory()
        self.cfgfile = ConfigParser()
        self.cfgfile.read(self.config_file)
        # Si todo esta bien requerir las configuraciones hechas por el
        # usuario en el archivo de configuracion

    def CheckDirectory(self):
        # Registro: (Client_secret,Archivo de Configuracion,URL.conf)
        check = (False,False,False)
        for i in self.getListFiles():
            if i == self.client_secret:
                check[0] = True
            if i == self.config_file:
                check[1] = True
            if i == self.url_conf:
                check[2] = True

        if check[0] == False:
            # TODO : Enviar mensaje de excepcion
            raise AttributeError("No se encontro el archivo con la clave API")
        if check[1] == False:
            self.createFile(self.config_file,var.CONFIG_DEFAULT,rw="w")

        if check[2] == False:
            self.createFile(self.url_conf,rw="w")


    def getCacheDir(self):

        if self.cfgfile.has_option("DIRECTORIOS","CACHE_DIR"):
            self.CACHE_DIR = self.cfgfile.get("DIRECTORIOS","CACHE_DIR")

        else:
            self.cfgfile.set("DIRECTORIOS","CACHE_DIR",var.CACHE_DIR)

    def setCacheDir(self,path):
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            self.cfgfile.set("DIRECTORIOS","CACHE_DIR",path)

    def getFormat(self):
        if self.cfgfile.has_option("OPCIONES","FORMAT_DEFAULT"):
            self.FORMAT_DEFAULT = self.cfgfile.getint("OPCIONES","FORMAT_DEFAULT")

        else:
            self.cfgfile.set("OPCIONES","FORMAT_DEFAULT",var.FORMAT_DEFAULT)

    def setFormat(self,nformat):

        self.cfgfile.set("OPCIONES","FORMAT_DEFAULT",nformat)    

        
