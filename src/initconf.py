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

    def CheckDirectory(self):

        for i in self.getListFiles():
            if 




