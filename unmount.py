import ctypes
import struct
from utilities import *
from load import *
class UNMOUNT(ctypes.Structure):
    def __init__(self, listaides):
        self.listaides = listaides
        self.id = '\0'
        self.constanteUNMOUNT = 'C'
    
    def ejecutarUNMOUNT(self):
        for val in self.listaides:
            if val.get("valorid") != None:
                self.id = val.get("valorid")
        print(self.id)