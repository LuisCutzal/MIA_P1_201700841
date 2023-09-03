import ctypes
import struct
from utilities import *
from load import *

class MOUNT(ctypes.Structure):
    def __init__(self, listaParametros):
        self.listaParametros = listaParametros
        self.path = '\0' #obligatorio
        self.name = '\0' #obligatorio
        self.constanteMOUNT = '2c'
    
    def ejecutarMOUNT(self):
        for val in self.listaParametros:
            if val.get("rutaArchivo") != None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
            elif val.get("valorname") != None:
                self.name = val.get("valorname")
        print(self.path)
        if not archivoExistente(self.path):
            print(f"No existe el archivo en la ruta {self.path}")
            return
        #aca se coloca la parte del nombre de la particion