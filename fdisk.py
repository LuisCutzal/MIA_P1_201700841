import ctypes
import struct
from utilities import *
from load import *

class FDISK(ctypes.Structure):
    def __init__(self,listaParametros):
        self.listaParametros = listaParametros
        self.size = 0 #obligatorio
        self.path = '\0' #obligatorio
        self.name = '\0' #obligatorio
        self.unit = 'K' #kilobytes es default 
        self.type = 'P' #primaria es default 
        self.fit = 'WF'
        self.delete = '\0'
        self.add = 0
        self.constanteFDISK = 'I 6s i'
    
    def ejecutarFDISK(self):
        for val in self.listaParametros:
            if val.get("valorsize") != None:
                self.size = val.get("valorsize")
            elif val.get("rutaArchivo") != None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
            elif val.get("valorname") != None:
                self.name = val.get("valorname")
            elif val.get("valorunit") != None:
                self.unit = val.get("valorunit")
            elif val.get("valortype") != None:
                self.type = val.get("valortype")
            elif val.get("valorfit") != None:
                self.fit = val.get("valorfit")
            elif val.get("valordelete") != None:
                self.delete = val.get("valordelete")
            elif val.get("valoradd") != None:
                self.add = val.get("valoradd")
        print(self.size, self.path, self.name, self.unit,self.type,self.fit,self.delete,self.add)