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
        self.videos = []
        # {playlistID:[videoId]}
        self.blacklist = {}

        
    def getVideosList(self,playlistID):
        # TODO : Evitar duplicados en ese caso devolver la lista anterior o
        #        reemplazarla en self.videos

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

        self.videos.append((playlistID,lst))

        return lst

    def getPlaylists(self):
        

        request = self.srv.playlists().list(
                part="id,snippet",
                mine="true",
                maxResults=10,
                fields="items/snippet/title,items/id,nextPageToken,pageInfo,prevPageToken"
                ).execute()

        rq = [request]
        #TODO : si los numeros de elementos de playlists o los videos de playlist
      # exceden en numero al parametro maxResults. la respuesta generara un token
      # nextPageToken utilizar este para recorrer a los siguientes resultados y
      # concatenarlos al anterior
      # totalResults y resultsPerPage pueden resultar utiles

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
            for i in self.lstplaylists:
                self.lstplaylists.pop()


        for i in rq:
            for x in i["items"]:
                self.lstplaylists.append((x["snippet"]["title"],x["id"]))

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


