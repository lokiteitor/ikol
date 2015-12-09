import os


### Directorios ### 

CONFIG_DIR = os.environ["HOME"] + "/.config/ikol"


### Archivos ### 
CODE_STORAGE = CONFIG_DIR + "/code_oauth.json" 
CLIENT_SECRETS_FILE = CONFIG_DIR +"/client_secret.json"
CONFIG_FILE = CONFIG_DIR + "/ikol.conf"


### Argumentos Comunes ### 
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

YOUTUBE_URL  = "https://www.youtube.com/watch?v="


### Mensajes ### 
MISSING_CLIENT_SECRETS_MESSAGE = "El archivo client_secret no se encuentra"

# TODO: Agregar las configuraciones por defecto tales como directorio de
#       descargas y similares
CONFIG_DEFAULT = []



