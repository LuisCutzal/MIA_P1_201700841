from MBR import *
from load import *
import struct

class REP():
    def __init__(self):
        pass
    
    def ejecutarRep(self):
        nuevoObjetoMBR = MBR(0,0,0,"")
        data=Fread_displacement("/home/luis/Escritorio/Archivos2023/proyectos/Disco1.dsk",0,struct.calcsize(nuevoObjetoMBR.constMBR))
        nuevoObjetoMBR.doDeserialize(data)
        print("Fit: " ,deBinaString(nuevoObjetoMBR.dsk_fit))
        print("Asignature: " ,nuevoObjetoMBR.mbr_dsk_signature)
        print("Fecha de Creacion:" , nuevoObjetoMBR.mbr_fecha_creacion)
        print("Tamaño disco: " ,nuevoObjetoMBR.mbr_tamano)