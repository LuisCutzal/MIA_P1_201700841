import ctypes
import struct
from utilities import *
from particiones import *

class MBR():
    def __init__(self, mbr_tamano, mbr_fecha_creacion, mbr_dsk_signature, dsk_fit):
        self.mbr_tamano = mbr_tamano
        self.mbr_fecha_creacion = mbr_fecha_creacion
        self.mbr_dsk_signature = mbr_dsk_signature
        self.dsk_fit = dsk_fit
        self.constMBR = '3I c'
        self.particion1 = PARTICION()
        self.particion2 = PARTICION()
        self.particion3 = PARTICION()
        self.particion4 = PARTICION()
        
    def doSerialize(self):
        objetoMBR = struct.pack( #todo debe de estar en binario
            self.constMBR,
            self.mbr_tamano,
            self.mbr_fecha_creacion,
            self.mbr_dsk_signature,
            self.dsk_fit
        )
        return objetoMBR + self.particion1.doSerialize() + self.particion2.doSerialize() + self.particion3.doSerialize() + self.particion4.doSerialize() #aca ya se puede sumar las particiones serializadas
    
    def doDeserialize(self, data):
        sizeMK = struct.calcsize(self.constMBR)
        datoBinarioMBR = data[:sizeMK]
        self.mbr_tamano, self.mbr_fecha_creacion, self.mbr_dsk_signature, self.dsk_fit = struct.unpack(self.constMBR, datoBinarioMBR)
        self.mbr_fecha_creacion = convertirFecha(self.mbr_fecha_creacion)
        
        
    