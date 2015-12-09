#!/usr/bin/env python2.7

import directory
import var

class InitConf(directory.Directorio):
    """Permite Revisar la integridad del directorio de configuracion"""
    def __init__(self):
        super(InitConf, self).__init__(var.CONFIG_DIR)

        self.ConfDir = var.CONFIG_DIR
        self.client_secret = var.CLIENT_SECRETS_FILE
        self.storage_path = var.CODE_STORAGE
        self.config_file = var.CONFIG_FILE
        self.url_conf = var.URL_CONF


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
            pass
        if check[1] == False:
            self.createFile(self.config_file,var.CONFIG_DEFAULT,rw="w")

        if check[2] == False:
            self.createFile(self.url_conf,rw="w")








