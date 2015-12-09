import var

# TODO Mover en la clase que configure el entorno CONF
class URL(object):
    """lee el archivo de configuracion para obtener las fuentes de video
       parsea estas fuentes para obtener el ID o informar si se trata de un 
       archivo local"""
    def __init__(self):
        super(URL, self).__init__()
        self.url_conf = var.URL_CONF

        self.youtubeURL = []
        self.FileURL = []
        self.youtubeID = []
        self.FileID = []

    def Parser(self,string):
        # https://www.youtube.com/playlist?list=PLCvsDNs462g6ogVJxJ_BcDB8GTDlLh_XQ
        # /run/media/Archivos/Musica/Drumm and Bass/[DnB] - Bustre - Don`t Forget (feat. LaMeduza) [Monstercat Release].mp4
        # Dividir el nombre en / si la primera divicion contiene https ,
        # comprobar que la segunda tambien tenga youtube
        # si la primera division no empieza por https revisar que la cadena 
        # original sea una ruta valida
        div = string.split("/")

        if div[0] == "http:" or div[0] == "https:":
            if div[2] == "www.youtube.com":
                self.youtubeURL.append()




