from setuptools import setup

setup(

    name="Ikol-Music Manager",
    # Cambiar esto entre cada lanzamiento
    version="1.5",
    description="Organizador de musica autonomo",
    long_description="Programa que permite el manejo autonomo de una coleccion de musica \
                descargada desde youtube",
    author="David Delgado",
    author_email="daviddelgado513ddg@gmail.com",
    url="http://www.desarrolloslkt.tk",
    license="GPL v2",
    scripts=["bin/ikol"],
    packages=["ikol","ikol.youtube","ikol.downloader"],
    # Listar dependencias
   # install_requires = ["google-api-python-client","youtube_dl"]
    )


