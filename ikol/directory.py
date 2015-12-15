
import os


# Clase que representa un directorio y que su funcion es toda la
# gestion de los ficheros

class Directorio(object):
    """Clase que representa un directorio y que su funcion es toda la
        gestion de los ficheros"""
    def __init__(self, path):
        super(Directorio, self).__init__()
        self.path = path
        self.dirs = []
        self.files = []
        self.associate = []

        if not os.path.exists(path):
            os.mkdir(self.path)

    def getListSubDirectory(self):
        # obtener la lista de los subdirectorios en el primer nivel
        for x in os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path,x)):
                self.dirs.append(os.path.join(self.path,x))

        return self.dirs
        
    def getAllListSubDirectory(self):
        # Obtener todos los subniveles
        for root, dirs, files in os.walk(self.path):
            for i in dirs:
                self.dirs.append(os.path.join(root,i))

        return self.dirs

    def deleteFile(self,f):
        # Borrar archivos
        # el nombre del archivo debe de estar de la forma absolute path
        if os.path.exist(f) and os.path.isfile(f):
            os.remove(f)
            self.files.remove(f)
        else:
            #TODO lanzar error y registrarlo en el log
            pass
    def getDirectory(self,path):
        # Para moverse entre subdirectorios forzamente debe 
        # de usarse este metodo que devuelve un objeto Directorio
        if os.path.exists(path) and os.path.isdir(path):
            if path in self.dirs:
                newdir = Directorio(path)
        else:
            os.mkdir(path)
            if os.path.dirname(path) == self.path:
                self.dirs.append(path)
            else:
                self.associate.append(path)

        return newdir
            
    def createSubDir(self,pathdir):
        # TODO : que pasa si pathdir es  path relativo
        if pathdir[0:len(self.path)] == self.path:
            if not os.path.exists(pathdir):
                os.mkdir(pathdir)
            else:
                # TODO : registrarlo en el log
                print("El directorio %s ya existe",pathdir)
        else:
            # TODO : lanzar excepcion
            print("El directorio %s esta fuera del alcanze del objeto",pathdir)

    def getListFiles(self):
        # Obtener lista de archivos en el primer nivel
        self.files = [] 
        for i in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,i)):
                self.files.append(os.path.join(self.path,i))
        return self.files


    def moveFile(self):
        pass

    def createFile(self,path,msj=None,rw="w"):
        # Crear un archivo con msj como contenido
        # si msj es None crear solo un archivo vacio
        # rw el modo de lectura/escritura

        with open(path,rw) as fl:
            if msj and type(msj) == "<type 'list'>":
                for i in msj:
                    fl.write(i+"\n")
            elif msj and msj == "<type 'str'>":
                fl.write(msj + "\n")