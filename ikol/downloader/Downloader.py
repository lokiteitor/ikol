from subprocess import Popen,PIPE

import var


class Downloader(object):
    """Objeto que realiza el seguimiento del video desde su descarga hasta 
    su Almacenamiento, pasando por la conversion, no realiza el tageo"""
    def __init__(self, URL):
        super(Downloader, self).__init__()
        self.URL = URL
        self.CACHE_DIR = var.CACHE_DIR

    def setCacheDir(self,path):
        # Para funcionar se debe proprocionar un directorio
        # donde almacenar los videos que se esten descargando}
        # De la opcion %id se puede obtener el nombre
        cachedir = self.CACHE_DIR + "/%(title)s-%(id)s.%(ext)s"

        self.CACHE_DIR = cachedir


    def setFormat(self,format):
        # Establece un formato diferente al de defecto
        self.format = format


        # Procss = Popen(["youtube-dl","-J",self.URL],stdout=PIPE)
        # rest = Procss.stdout.read()

        # TODO : De la salida que genere obtener los numeros de formato


    def download(self):
        #devuelve el nombre del archivo
        P = Popen(["youtube-dl","-o",self.CACHE_DIR,"-f",str(self.format),
            "-ci",self.URL],stdout=PIPE)

        P.wait()
        # TODO : esto no devuelve nada asi que se debe comprobar manualmente
        # o por el codigo 0 de P.wait()
        print P.stdout.read()




        