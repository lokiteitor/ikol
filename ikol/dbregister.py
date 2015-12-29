
import sqlite3
import os
import datetime

class DataBase(object):
    """Si la base de datos no exite iniciar los valores por defecto"""
    def __init__(self, pathDB):
        super(DataBase, self).__init__()
        self.pathDB = pathDB
        if not os.path.exists(self.pathDB):
            self._drawTables()
    
    def _drawTables(self):
        Conn = sqlite3.connect(self.pathDB)
        cursr = Conn.cursor()

        TABLEINIT = "CREATE TABLE historial (id INTEGER NOT NULL ,name VARCHAR(255)\
                    NOT NULL, IDvideo VARCHAR(25) NOT NULL, IDplaylist VARCHAR(25)\
                    NOT NULL, fecha TIMESTAMP, PRIMARY KEY('id')) "

        cursr.execute(TABLEINIT)

        TABLEPLSINIT = "CREATE TABLE playlist (id INTEGER NOT NULL, name VARCHAR(255)\
                        , IDplaylist VARCHAR(25) NOT NULL,fecha TIMESTAMP,PRIMARY KEY('id'))"
                
        cursr.execute(TABLEPLSINIT)
        # nombre del archivo, idvideo, ruta completa
        TABLEPATH = "CREATE TABLE registro (id INTEGER NOT NULL, namef VARCHAR(255)\
                    NOT NULL, IDVideo VARCHAR(25) NOT NULL , pathabs VARCHAR(255)\
                    NOT NULL,mfecha TIMESTAMP,PRIMARY KEY('id'))"
        
        cursr.execute(TABLEPATH)

        Conn.commit()
        Conn.close()
        return

    def insertPlaylist(self,IDplaylist,name):
        Conn = sqlite3.connect(self.pathDB)
        cursr = Conn.cursor()
        # Obtiene el id del siguiente elemento
        req = cursr.execute("SELECT id FROM playlist").fetchall()
        # TODO : Testear a fondo
        if len(req) == 0:
            idn = 1
        else:
            idn = req[len(req) - 1][0] + 1

        # Obtiene la fecha de creacion
        # Crea una playlist en la base de datos
        QUERY = "INSERT INTO playlist (id,name,IDplaylist,fecha) VALUES (?,?,?,datetime('now'))"
        t = (idn,name,IDplaylist)
        cursr.execute(QUERY,t)

        Conn.commit()
        Conn.close()
        return

    def insertVideo(self,IDVideo,IDplaylist,name):
        # Ingresa un video al historial
        Conn = sqlite3.connect(self.pathDB)
        cursr = Conn.cursor()
        # Obtiene el id del siguiente elemento
        req = cursr.execute("SELECT id FROM historial").fetchall()
        # TODO : Testear a fondo
        if len(req) == 0:
            idn = 1
        else:
            idn = req[len(req) - 1][0] + 1

        QUERY = "INSERT INTO historial (id,name,IDvideo,IDplaylist,fecha)\
                VALUES (?,?,?,?,datetime('now'))"
        t = (idn,name,IDVideo,IDplaylist)
        cursr.execute(QUERY,t)
        
        Conn.commit()
        Conn.close()
        return

    def getAllVideosByPlaylist(self,IDplaylist):
        # Devuelve todos los videos que pertenecen a la misma playlist
        Conn = sqlite3.connect(self.pathDB)
        cursr = Conn.cursor()

        QUERY = "SELECT id,IDVideo FROM historial WHERE IDplaylist=?"
        t = (IDplaylist,)
        req = cursr.execute(QUERY,t).fetchall()

        return req

    def getVideoById(self,IDVideo):
        Conn = sqlite3.connect(self.pathDB)
        cursr = Conn.cursor()

        QUERY = "SELECT * FROM historial WHERE IDVideo=?"
        t = (IDVideo,)
        req = cursr.execute(QUERY,t).fetchall()

        return req


    def getPlaylist(self,IDplaylist):
        # obtiene los datos de una playlist
        Conn = sqlite3.connect(self.pathDB)        
        cursr = Conn.cursor()
        
        t = (IDplaylist)
        QUERY = "SELECT * FROM playlist WHERE IDplaylist=?"
        req = cursr.execute(QUERY,t)

        # TODO : Darle formato a los datos devueltos
        Conn.close()
        return req


    def movePath(self,name,pathabs):
        # Cambiar el lugar donde se encuentre el archivo
        pass

