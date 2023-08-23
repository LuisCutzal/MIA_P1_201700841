import ctypes
import struct
from utilities import coding_str
from load import *

const = 'I 50s 2s 1s' #3 enteros sin signo, formato que se utilizara

class MKDISK(ctypes.Structure):
    __fields__ = [
        ('size', ctypes.c_int),
        ('path', ctypes.c_char * 50),
        ('fit', ctypes.c_char * 2 ),
        ('unit', ctypes.c_char * 1)
    ]
        
    def __init__(self,listaParametros):
        self.listaParametros = listaParametros
        self.size = 0
        self.path = "" #no se guarda
        self.fit = "FF"
        self.unit = "M" #no se guarda
    
    def ejecutar(self):
        for val in self.listaParametros:
            if val.get("valorfit") != None:
                self.fit = val.get("valorfit")
            elif val.get("valorunit") != None:
                self.unit = val.get("valorunit")
            elif val.get("valorsize") != None:
                self.size = int(val.get("valorsize"))
            elif val.get("rutaArchivo") != None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
        #print(self.size, self.path, self.fit, self.unit)
        if self.path == "":
            print("error, MKDISK path obligatorio")
            return
        if self.size <= 0:
            print("error, MKDISK size debe ser mayor a 0")
            return
        if self.fit != "BF" and self.fit != "FF" and self.fit != "WF":
            print("error, MKDISK fit no se aceptan los valores")
            return
        if self.unit != "K" and self.unit != "M":
            print("error, MKDISK unit no se aceptan los valores")
            return
        
        Fcreate_file(self.path)
        Crrfile = open(self.path,"rb+")
        desplazamiento = 0
        if self.unit == "K":
            Winit_size(Crrfile,self.size * 1024)
            objeto = MKDISK(self.listaParametros)
            Fwrite_displacement(Crrfile,desplazamiento,objeto)
            Crrfile.close()
        elif self.unit == "M":
            Winit_size(Crrfile,self.size * 1024 * 1024)
            objeto = MKDISK(self.listaParametros)
            Fwrite_displacement(Crrfile,desplazamiento,objeto)
            Crrfile.close()
            

    def set_size(self, size):
        self.size = size

    def set_path(self, path):
        self.path = coding_str(path, 50)

    def set_fit(self, fit):
        self.fit = coding_str(path, 2)
    
    def set_unit(self, unit):
        self.unit = coding_str(unit,1)

    def set_infomation(self, size, path, fit, unit):
        self.set_size(size)
        self.set_path(path)
        self.set_fit(fit)
        self.set_unit(unit)




    def display_info(self):
        print(f"size: {self.size}")
        print(f"path: {self.path.decode()}")
        print(f"fit: {self.fit.decode()}")
        print(f"unit: {self.unit.decode()}")

    def doSerialize(self):
        return struct.pack(
            const,
            self.size,
            self.path,
            self.fit,
            self.unit
        )

    def doDeserialize(self, data):
        self.size, self.path, self.fit, self.unit = struct.unpack(const, data)