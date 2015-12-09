#!/usr/bin/env python2.7

import os
import sys


this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir+"/src")


from youtube import Auth


conf = trunk_dir + "/conf/client_secret.json"

sto = trunk_dir + "/conf/oauth.json"

A = Auth.Authorized(conf)

A.getFlow()

A.setStorage(sto)

srv = A.getService()

# Esta solicitud ayuda a filtrar las listas de reproduccion
# Solo muestra el id y el title
resp = srv.playlists().list(
    part="id,snippet",
    mine="true",
    maxResults=10,
    fields="items/snippet/title,items/id,nextPageToken,pageInfo,prevPageToken"

).execute()

#TODO : si los numeros de elementos de playlists o los videos de playlist
#       exceden en numero al parametro maxResults. la respuesta generara un token
#       nextPageToken utilizar este para recorrer a los siguientes resultados y
#       concatenarlos al anterior
#       totalResults y resultsPerPage pueden resultar utiles


print resp["pageInfo"]["totalResults"]
print resp["nextPageToken"]

with open('out.log','w') as filelog:

    filelog.write(str(type(resp)) + "\n\n")

    respd = resp["items"]

    filelog.write("\n")

    playlst = []

    for i in respd:

        # Aqui obtenemos el Nombre de la playlist
        print i["snippet"]["title"]
        # Aqui hemos obtenido el ID que forma parte de la url de la playlist
        print i["id"]

        playlst.append(i["id"])


    # Obtener los nombres de todos los videos de la playlist
    # TODO : Me devolvera videos eliminados estos abra que eliminarlos 
    #        de la playlist y de la cola de descarga

    # filelog.write("\n\n")

    # for x in playlst:
    #     print x

    #     # Query para obtener el nombre de los videos y la ID parte de la
    #     # URL de descarga
    #     playlstitems = srv.playlistItems().list(
    #         playlistId=x,
    #         part="snippet",
    #         fields="items/snippet/title,items/snippet/resourceId(videoId),nextPageToken,pageInfo,prevPageToken",
    #         maxResults=50
    #         ).execute()

    #     # TODO : Manejar posibles errores desde google
    #     respd = playlstitems["items"][0]

    #     print respd["snippet"]["title"]









