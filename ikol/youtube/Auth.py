#!/usr/bin/env python2.7

import argparse
import httplib2
import os


from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from apiclient.discovery import build

from ikol import var


class Authorized(object):
    """Permite obtener un objeto capaz de realizar las peticiones a la API 
       de Youtube
       Recibe una ruta hacia el json con las credenciales"""
    def __init__(self,client_secret):
        super(Authorized, self).__init__()
        # Puede pasar argumentos a la linea de comandos
        # TODO : se puede crear un menu - personalizar
        #        Posible error al pasar los argumentos durante la autorizacion
        # self.parser = argparse.ArgumentParser(parents=[tools.argparser])
        # self.args = self.parser.parse_args()
        self.client_secret = client_secret


    def getFlow(self):
        # Carga el archivo con los datos de la credencial

        self.flow = flow_from_clientsecrets(self.client_secret,
            scope=var.YOUTUBE_SCOPE,
            message=var.MISSING_CLIENT_SECRETS_MESSAGE)

        return self.flow

    def setStorage(self,path):
        #Recibe la ruta donde seran almacenados la credencial
        self.storage = Storage(path)
        self.credentials = self.storage.get()

        #TODO : Quizas este argumento sirva para autentificarse 
        #       De forma remota
        # if os.environ.has_key("DISPLAY"):
        #     args=[]
        # else:
        #     args=["--noauth_local_webserver"]


        # Si el usuario nunca a autorizado la aplicacion o la denego
        if self.credentials is None or self.credentials.invalid:
            #Esto abre la ventana del navegador
            #TODO : encontrar forma de cerrar esa ventana
            # NOTA Revisar webbrowser libreria estandar
            # Redirigir el navegador a una pagina con javascript para cerrar
            # Para ello debemos usar otro metodo para obtener las credenciales
            parser = argparse.ArgumentParser(parents=[tools.argparser])
            flags = parser.parse_args(args=[])
            self.credentials = tools.run_flow(self.flow, self.storage,flags)




    def getService(self):
        http_auth = self.credentials.authorize(httplib2.Http())


        return  build(var.YOUTUBE_API_SERVICE_NAME, var.YOUTUBE_API_VERSION,
                http=http_auth)






