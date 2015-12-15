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
        self.url_file = var.URL_FILE

        # Directorios secundarios
        # TODO : si se establece manualmente revisar que no se sobrepongan
        self.CACHE_DIR = self.getCacheDir

        # Opciones
        self.format = var.FORMAT_DEFAULT

        # revisar la integridad antes de continuar
        self.CheckDirectory()
        self.cfgfile = ConfigParser()
        self.cfgfile.read(self.config_file)
        # Si todo esta bien requerir las configuraciones hechas por el
        # usuario en el archivo de configuracion

        # si el usuario marco manualmente una configuracion no persistente verlo
        # aqui
        # CACHE_DIR,URL_FILE,FORMAT_DEFAULT
        self.reg = [False,False,False]

    def CheckDirectory(self):
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

    def addURL(self,URL):
        # TODO : Revisar integridad del URL 
        #       Si existe duplicado
        #        Revisar que se una lista de reproduccion si no solo agregarla
        #        temporalmente
        with open(self.url_file,"a") as f:
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
                    urllist.append(url)

            return urllist

        except Exception, e:
            # TODO: Lanzar aviso y log
            print e
            # crear el archivo
            self.createFile(self.url_file,rw="w")
            return []

        


