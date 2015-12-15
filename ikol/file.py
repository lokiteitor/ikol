import os
import string

import var


class File(object):
    """hacer el seguimiento de un archivo"""
    def __init__(self, path):
        super(File, self).__init__()

        if os.path.exists(path):
            self.path = path
        else:
            # TODO : Lanzar excepcion
            pass

        self.name = os.path.basename(path)
        self.onlyname = os.path.splitext(self.name)[0]
        self.ext = os.path.splitext(self.name)[1]


    def asciiName(self):
        
        # Limpia el nombre del archivo de extenciones, puntaciones
        # y caracteres no ascii
        name  = os.path.splitext(self.name)[0]

        for x in name:
            if not x in string.printable:
                name = name.replace(x,'')

        for i in string.punctuation:
            if i == '_':
                name = name.replace(i,' ')
            else:
                name = name.replace(i,'')


        return name

    def FormatLst(self,tpl):
        # La lista de archivos que genere el objeto debe pasar por aqui
        # se encarga de marcar y separar los videos eliminados
        # luego de ello devuelve una lista de URL+ID validos
        idstr = tpl[1]

        URL = var.YOUTUBE_URL + idstr


        return URL        
        
