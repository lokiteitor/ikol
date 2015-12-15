from setuptools import setup
import glob



setup(

    name="Ikol-Music Manager",
    # Cambiar esto entre cada lanzamiento
    version="0.4.dev1",
    description="Organizador de musica autonomo",
    long_description="Programa que permite el manejo autonomo de una coleccion de musica \
                descargada desde youtube",
    author="David Delgado",
    author_email="daviddelgado513ddg@gmail.com",
    url="http://www.desarrolloslkt.tk",
    license="GPL v2",
    scripts=["bin/ikol"],
    packages=["ikol","ikol.youtube","ikol.sort"]
    # Listar dependencias
    )