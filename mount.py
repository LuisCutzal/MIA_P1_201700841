import ctypes
import struct
from utilities import *
from load import *
from MBR import *
from EBR import *
from lista import *
class MOUNT(ctypes.Structure):
    def __init__(self, listaParametros):
        self.listaParametros = listaParametros
        self.path = '\0' #obligatorio
        self.name = '\0' #obligatorio
        self.nombrearchivo = ""
        self.constanteMOUNT = '2c'
        self.temporalMBR = ""
        self.temportalEBR = ""
        self.agregar_a_lista = ListaEnlazada()
        
    def ejecutarMOUNT(self):
        if not self.validarMount():
            print("Error, no se pudo ejecutar el comando mount")
            return
        self.leerMBR()
        if self.temporalMBR == "":
            print("Error, no se encuentra el MBR del archivo")
            return        
        listaParticiones = [self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        self.montarParticion(listaParticiones)
        self.imprimirMount()
        return
        
        
        
    
    def validarMount(self):
        for val in self.listaParametros:
            if val.get("rutaArchivo") != None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
                self.nombrearchivo = val.get("nombrearchivo")
            elif val.get("valorname") != None:
                self.name = val.get("valorname")
        if not archivoExistente(self.path):
            print(f"No existe el archivo en la ruta {self.path}")
            return
        return True
    
    def leerMBR(self):
        temporalMBR = MBR(0,0,0,0)
        datos = Fread_displacement(self.path,0,struct.calcsize(temporalMBR.constMBR) + struct.calcsize(temporalMBR.particion1.constanteParticion)*4)
        temporalMBR.doDeserialize(datos) #ya tenemos los datos del mbr
        self.temporalMBR = temporalMBR
    
    def retornarExtendida(self, listaparticiones):
        for particion in listaparticiones:
            if particion.part_type == "E":
                return particion
    
    
    def montarParticion(self, listaparticiones):
        #aca se coloca la parte del nombre de la particion
        actualEBR = EBR()
        particionExtendida = self.retornarExtendida(listaparticiones)
        tam = struct.calcsize(actualEBR.constanteEBR)
        datosEBR = Fread_displacement(self.path,particionExtendida.part_start,tam)
        actualEBR.doDeserialize(datosEBR)
        self.temportalEBR = actualEBR
        nombre = self.nombrearchivo.split(".") #esto es nombre del disco
        if actualEBR.part_name == self.name: #primera particion
            #aca encontre la particion ahora comenzare a agregarlo a una lista
            #                                     nombre disco, nombre particion, estado particion  
            self.agregar_a_lista.agregar_elemento(nombre[0], actualEBR.part_name, actualEBR.part_status)
            #agregar_a_lista.imprimir_lista()
            return
        
        while actualEBR.part_next != -1:
            actualEBR.doDeserialize(Fread_displacement(self.path, actualEBR.part_next, tam))
            if actualEBR.part_name == self.name:
                self.agregar_a_lista.agregar_elemento(nombre[0], actualEBR.part_name, actualEBR.part_status)
                return
    def imprimirMount(self):
        print("**** Indice ********** Particion ********** Identificador **********")
        self.agregar_a_lista.imprimir_lista()


"""
ultimos digitos carnet + numero particion + nombredisco
para los ids -> 411disco1
"""