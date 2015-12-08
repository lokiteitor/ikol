import os


### Directorios ### 

CONFIG_DIR = os.environ["HOME"] + "/.config/ikol"


### Archivos ### 
CODE_STORAGE = os.environ["HOME"] + CONFIG_DIR + "/code_oauth.json" 
CLIENT_SECRETS_FILE = os.environ["HOME"] + CONFIG_DIR +"/client_secret.json"


### Argumentos Comunes ### 
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


### Mensajes ### 
MISSING_CLIENT_SECRETS_MESSAGE = "El archivo client_secret no se encuentra"
