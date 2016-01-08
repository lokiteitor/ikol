#Copyright (C) 2015  David Delgado Hernandez 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging

from ikol import var


class APIRequest(object):
    """Maneja todas la solicitudes hacia el API youtube 
       Devuelve los datos formateados para su uso adecuado"""
    def __init__(self, srv):
        # recibe un objeto service proveniente de Authorized
        super(APIRequest, self).__init__()
        self.srv = srv
        # [(title,playlistID)]
        self.lstplaylists = []
        #[(playlistID,[(title,VideosID])]
        # {playlistID:[videoId]}
        self.blacklist = {}

        
    def getVideosList(self,playlistID):
        # Recibe un ID de playlistID
        # Devuelve una lista de ID de los videos que conforman la playlist

        # Esta solicitud ayuda a filtrar las listas de reproduccion
        # Solo muestra el id y el title

        playlstitems = self.srv.playlistItems().list(
            playlistId=playlistID,
            part="snippet",
            fields="items/snippet/title,items/snippet/resourceId(videoId),nextPageToken,pageInfo,prevPageToken",
            maxResults=50
            ).execute()

        rq = [playlstitems]

        total = playlstitems["pageInfo"]["totalResults"]
        splitnum = playlstitems["pageInfo"]["resultsPerPage"]

        if total > splitnum:
            nextToken = playlstitems["nextPageToken"]
            next = True
            while (next):
                nextrequest = self.srv.playlistItems().list(
                playlistId=playlistID,
                part="snippet",
                fields="items/snippet/title,items/snippet/resourceId(videoId),\
                nextPageToken,pageInfo,prevPageToken",
                maxResults=50,
                pageToken= nextToken
                ).execute()


                rq.append(nextrequest)

                if nextrequest.has_key("nextPageToken"):
                    nextToken = nextrequest["nextPageToken"]
                else:
                    next = False

        lst = []
        for i in rq:
            for x in i["items"]:
                lst.append((x["snippet"]["title"],x["snippet"]["resourceId"]["videoId"]))

        logging.debug(str(lst))
        return lst

    def getPlaylists(self):
        
        request = self.srv.playlists().list(
                part="id,snippet",
                mine="true",
                maxResults=10,
                fields="items/snippet/title,items/id,nextPageToken,pageInfo,prevPageToken"
                ).execute()

        rq = [request]

      # Revisar si la respuesta excede en tamano en ese caso realizar 
      # la solicituda las veces necesarias

        total = request["pageInfo"]["totalResults"]
        splitnum = request["pageInfo"]["resultsPerPage"]

        if total > splitnum:
            nextToken = request["nextPageToken"]
            next = True
            while (next):
                nextrequest = self.srv.playlists().list(
                part="id,snippet",
                mine="true",
                maxResults=10,
                fields="items/snippet/title,items/id,nextPageToken,pageInfo,prevPageToken",
                pageToken= nextToken
                ).execute()


                rq.append(nextrequest)

                if nextrequest.has_key("nextPageToken"):
                    nextToken = nextrequest["nextPageToken"]
                else:
                    next = False


        if len(self.lstplaylists) != 0:
            self.lstplaylists = []

        for i in rq:
            for x in i["items"]:
                self.lstplaylists.append((x["snippet"]["title"],x["id"]))
        logging.debug(str(self.lstplaylists))
        return self.lstplaylists


    def FormatURL(self,idvideo):
        # Dar formato de URL valido
        URL = var.YOUTUBE_URL + idvideo
        return URL

    def getSecondPeer(self,lst):
        lstrq = []
        for i in lst:
            lstrq.append(i[1])
        return lstrq

    def getNameList(self,idlst):
        self.getPlaylists()

        for i in self.lstplaylists:
            if idlst == i[1]:

                name = i[0]

        return name


