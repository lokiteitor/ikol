# -*- coding: utf-8 -*-
import os


### Directorios ### 

CONFIG_DIR = os.environ["HOME"] + "/.config/ikol"
CACHE_DIR = os.environ["HOME"] + "/.cache/ikol"
# TODO : utilizar las variables XDG
FINAL_DIR = os.environ["HOME"] + "/Música"


### Archivos ### 
CODE_STORAGE = CONFIG_DIR + "/code_oauth.json" 
CLIENT_SECRETS_FILE = CONFIG_DIR +"/client_secret.json"
CONFIG_FILE = CONFIG_DIR + "/ikol.conf"
URL_FILE = CONFIG_DIR + "/url.conf"
DB_PATH = CONFIG_DIR + "/history.db"


### Argumentos Comunes ### 
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

YOUTUBE_URL  = "https://www.youtube.com/watch?v="

FORMAT_DEFAULT = 140


### Mensajes ### 
MISSING_CLIENT_SECRETS_MESSAGE = "El archivo client_secret no se encuentra"

# TODO: Agregar las configuraciones por defecto tales como directorio de
#       descargas y similares
CONFIG_DEFAULT = ["[DIRECTORIOS]",
                    "CACHE_DIR="+CACHE_DIR,
                    "FINAL_DIR="+FINAL_DIR,
                    "[OPCIONES]",
                    "FORMAT_DEFAULT="+str(FORMAT_DEFAULT),
                    "DELETE_WRONG_LIST=YES"]



