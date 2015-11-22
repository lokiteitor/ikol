#!/usr/bin/env python3

import unittest
import os
import random
import string
import sys

# modificamos el path para poder acceder mejor a los modulos
this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]
sys.path.insert(0,trunk_dir)

import directory



class DirectoryTest(unittest.TestCase):
    """Pruebas para la creacion eliminacion y modificacion de ficheros"""

    def setUp(self):
        self.ldir = []        
        self.maindir = trunk_dir + "/test/files"

        if not os.path.exists(self.maindir):
            os.mkdir(self.maindir)

        self.directory = directory.Directorio(self.maindir)

        #crear paths aleatorios y agregarlos a la lista para el primer test
        # TODO : Codigo repetitivo refactorizar
        for x in range(1,20):
            name = ""
            name = name.join([random.choice(string.ascii_lowercase) for i in range(10)])

            self.ldir.append(self.maindir + '/' + name)

        print("Directorios en ldir:")
        print(self.ldir)

    def getName(self,root=None):

        name = "".join([random.choice(string.ascii_lowercase) for i in range(10)])

        if root != None:
            name = os.path.join(root,name)

        return name

    def testAcreateSubDir(self):
        for i in self.ldir:
            self.directory.createSubDir(i)

            self.assertTrue(os.path.exists(i))

    def testBListSubDirectory(self):
        self.testAcreateSubDir()
        print("Directorios devueltos por el objeto:")
        print(self.directory.getListSubDirectory())
        
        for x in self.directory.getListSubDirectory():
            self.assertIn(x,self.ldir)

    def testCgetAllSubDirectory(self):
        sub = []
        for i in self.ldir:
            self.directory.createSubDir(i)
            for x in range(2):
                subname = self.getName(i)
                sub.append(subname)
                self.directory.createSubDir(subname)
        self.ldir += sub
        print("Lista subldir")
        print(self.ldir)
        print("lista del objeto")
        print(self.directory.getAllListSubDirectory())

        for i in self.directory.getAllListSubDirectory():    
            self.assertIn(i,self.ldir)

    #TODO: Crear prueba para deleteFile

    def tearDown(self):
        for root, dirs, files in os.walk(self.maindir,topdown=False):
            for name in files:
                obj =  os.path.join(root, name)
                if os.path.exists(os.path.join(root, name)):
                    os.remove(obj)
            for name in dirs:
                if os.path.exists(os.path.join(root, name)):
                    os.rmdir(os.path.join(root, name))

            os.rmdir(root)


if __name__ == '__main__':
    unittest.main()