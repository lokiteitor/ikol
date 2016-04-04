#!/usr/bin/env python2.7

import json
import os

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3,APIC
# el JSON debe tener la siguiente estructura
# debe de llamarse tags.json

# {
#     "tags":{
#         "Artista":"foo",
#         "ArtistaAlbum":"foo",
#         "AlbumArt":"pathtojpg",
#         "Album":"bar",
#         "Genero":"var",
#     }
# }

class ReaderJSON(object):
    """Realizar la lectura del json que contiene los datos de tag"""
    def __init__(self,path):
        self.jsonpath = path
        self.json = self.getJsonObject(path)
        self.data = self.setData()


    def getJsonObject(self,path):
        with open(path,"r") as file:
            data = json.loads(file.read())
        return data

    def setData(self):
        # Asignar los datos a un diccionario
        # si artistaAlbum no esta usar artista
        # revisar si albumArt existe como ruta
        data = {}
        data["artista"] = self.json['tags']['Artista']
        data['artistaAlbum'] = self.json['tags']['ArtistaAlbum']
        data['album'] = self.json['tags']['Album']
        data['genero'] = self.json['tags']['Genero']

        if os.path.isabs(self.json['tags']['AlbumArt']): 
            data['albumArt'] = self.json['tags']['AlbumArt']

        else:
            data['albumArt'] = os.path.join(os.path.dirname(self.jsonpath),self.json['tags']['AlbumArt'])

        return data

    def getArtista(self):
        return self.data['artista']

    def getArtistaAlbum(self):
        return self.data['artistaAlbum']

    def getAlbumArt(self):
        return self.data['albumArt']

    def getAlbum(self):
        return self.data['album']

    def getGenero(self):
        return self.data['genero']

class Tag(ReaderJSON):
    """Estable las tags en las canciones de cada carpeta"""
    def __init__(self,path,format):
        # recibe la ruta de las carpetas
        # recibe la extencion de los archivos a modificar
        # se puede utilizar esta informacion para personalizar la implementacion
        # de las etiquetas
        self.format = format
        self.path = path
        # busca el archivo json
        self.jsonfile = self.SearchJSON()
        self.files = []
        if (self.jsonfile != ''):
            self.flag = True
            super(Tag, self).__init__(self.jsonfile)
        else:
            self.flag = False
        
    def SearchJSON(self):
        rtrn = ''
        for i in os.listdir(self.path):
            if i == 'tags.json':
                rtrn = os.path.join(self.path,i)

        return rtrn

    def getStatus(self):
        return self.flag

    def setJsonObject(self,path):
        if self.flag == False:
            self.jsonfile = self.SearchJSON(path)
            if (self.jsonfile != ''):
                self.flag = True
                super(Tag, self).__init__(self.jsonfile)
            else:
                self.flag = False

    def loadMusicFiles(self,files=False):
        # cargar la lista de archivos a modifcar por defecto son los 
        # que se encuentran en la raiz del directorio objetivo
        if files == False:
            for i in os.listdir(self.path):
                # revisar que los archivos sean del tipo indicado
                if os.path.splitext(i)[1] == '.'+self.format:

                    self.files.append(os.path.join(self.path,i))
        else:
            for i in files:
                if os.path.isabs(i) and os.path.isfile(i):
                    self.files.append(i)
                else:
                    filepath = os.path.join(self.path,i)
                    if os.path.isfile(filepath) and os.path.exists(filepath):
                        self.files.append(filepath)


        return self.files

    def convertCover(self,path):
        # Convertir la imagen en jpeg 
        pass

    def setTags(self):
        # no verifica si existe el archivo es lo debe de realizar desde la 
        # la implementacion

        # Tags de mutagen ['album'],['artist']['genre']
        for i in self.files:
            print "Tageando: " + i

            # la imagen debe de estar en formato jpeg
            picture = ID3(i)

            with open(self.getAlbumArt(),"rb") as img:
                imgdata = img.read()
                picture.add(APIC(encoding=3,mime='image/jpeg',type=3,data=imgdata,
                    desc=self.getAlbumArt()))

            picture.update_to_v24()
            picture.save(v2_version=3)

            if self.format == 'mp3':
                obj = MP3(i, ID3=EasyID3)
            else:
                obj = EasyID3(i)


            obj['album'] = self.getAlbum()
            obj['artist'] = self.getArtista()
            obj['genre'] = self.getGenero()

            obj['performer'] = self.getArtistaAlbum()

            obj.save()



