import ctypes
import struct
from utilities import *
from load import *
from MBR import *
class MOUNT(ctypes.Structure):
    def __init__(self, listaParametros):
        self.listaParametros = listaParametros
        self.path = '\0' #obligatorio
        self.name = '\0' #obligatorio
        self.constanteMOUNT = '2c'
    
    def ejecutarMOUNT(self):
        if not self.validarMount():
            print("Error, no se pudo ejecutar el comando mount")
            return
        self.leerMBR()
        if self.temporalMBR == "":
            print("Error, no se encuentra el MBR del archivo")
            return
        listaParticiones = [self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        if self.validarNombre(listaParticiones):
            print("FDISK no se pudo ejecutar correctamente")
            return
        
    
    
    def validarMount(self):
        for val in self.listaParametros:
            if val.get("rutaArchivo") != None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
            elif val.get("valorname") != None:
                self.name = val.get("valorname")
        print(self.path)
        if not archivoExistente(self.path):
            print(f"No existe el archivo en la ruta {self.path}")
            return
        return True
    def leerMBR(self):
        temporalMBR = MBR(0,0,0,0)
        datos = Fread_displacement(self.path,0,struct.calcsize(temporalMBR.constMBR) + struct.calcsize(temporalMBR.particion1.constanteParticion)*4)
        temporalMBR.doDeserialize(datos) #ya tenemos los datos del mbr
        self.temporalMBR = temporalMBR
        
    def validarNombre(self, listaparticiones):
        #aca se coloca la parte del nombre de la particion
        for particion in listaparticiones:
            if particion.part_name == self.name:
                print("El nombre de la particion ya existe")
                return True
        return False
        
        
"""
ultimos digitos carnet + numero particion + nombredisco
para los ids -> 411disco1
"""