import os
from subprocess import Popen,PIPE
import logging

import var

class Convert(object):
    """Realiza las conversiones de archivos utilizando ffmpeg
       o avconv"""
    def __init__(self, path):
        super(Convert, self).__init__()
        self.binary = ""
        self.kbps = var.KBPS
        self.format = var.CODEC_DEFAULT
        self.path = path
        self.dest = path
        self.formatsAvaible = []
        self.getBinary()

    def getBinary(self):

        if "avconv" in os.listdir("/usr/bin"):

            self.binary = "avconv"

        elif "ffmpeg" in os.listdir("/usr/bin"):
            self.binary = "ffmpeg"

        else:
            raise Warning("El binario para la conversion no esta instalado")
            logging.warning("Binario de convesion no encontrado")

        logging.debug(self.binary)

        return self.binary

    def setConfig(self,format,kbps):
        # Revisar si el formato es aceptado
        Procss = Popen([self.binary,"-formats"],stdout=PIPE)
        rest = Procss.stdout.read()
        req = rest.split("\n")


        for i in req:
            try:
                self.formatsAvaible.append(i.split()[1])
            except Exception, e:
                logging.debug(str(e))

        if format in self.formatsAvaible:
            self.format = format
        else:
            self.format = var.CODEC_DEFAULT

        if "K" in kbps or "k" in kbps:
            self.kbps = kbps
        else:
            self.kbps = kbps + "K"

        return self.format

    def convert(self):
        # Convierte los archivos
    
        self.dest = self.path.replace(os.path.splitext(self.path)[1],"."+self.format)
        

        
        Procss = Popen([self.binary,"-i",self.path,"-vn","-ar","44100",
                "-ac","2","-ab",self.kbps,"-f",self.format,self.dest],stdout=PIPE)

        if Procss.wait() == 0:
            codereturn = True
        else:
            logging.debug(Procss.stdout.read())
            codereturn = False

        print Procss.stdout.read()

        return codereturn        

