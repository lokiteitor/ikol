#!/usr/bin/env python3

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

import os
import sys
import getopt


if __name__ == '__main__':
    # leer los argumentos
    # -C: --clean= : limpiar archivos repetidos -> CleanRepeat
    #       @requiere un directorio sobre el que actuar
    # -c:--convert= : convertir de video a audio -> Convert
    #       @directorio donde se encuentran los videos
    try:
        options,arg = getopt.getopt(sys.argv[1:], "Cch:",["clean=:","convert=","help"])
        
    except getopt.GetoptError:
        #TODO : Imprimir menu de ayuda
        print("""\
Uso: musicmanager [opciones] FUENTE DESTINO""")

    for opt, arg in options:
        if opt in ("-C" , "--clean"):
            if arg:
                #TODO Implementacion de limpieza de archivos
                #       con un directorio objetivo predefenido
                pass
            else:
                #TODO Usar Fuente
                pass
        if opt in ("-c" , "--convert"):
            if arg:
                #TODO Implementacion de conversion de archivos
                pass
            else:
                #TODO usar fuente
                pass
        if opt in ("--h","--help"):
            #TODO imprimir menu de ayuda
            pass


