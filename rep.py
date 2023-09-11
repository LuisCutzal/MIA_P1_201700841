from MBR import *
from load import *
import struct

class REP():
    def __init__(self, listaparametros):
        self.listaparametros = listaparametros
        self.identificador = ""
        self. path =""
        self.name = ""
        self.ruta = ""
        self.temporalMBR = ""
        
    def ejecutarRep(self):
        if not self.agregarvalores():
            print("El comandno rep no se pudo ejecutar correctamente")
            return
        if not self.verificarNombre():
            print("El nombre que ingreso en el comando REP no es valido")
            return
        print(self.identificador)
        
    def agregarvalores(self):
        for val in self.listaparametros:
            if val.get("valorid") is not None:
                self.identificador = val.get("valorid")
            elif val.get("rutaArchivo") is not None:
                self.path = val.get("rutaArchivo") + val.get("nombrearchivo")
            elif val.get("valorname") is not None:
                self.name = val.get("valorname")
            elif val.get("ruta") is not None:
                self.ruta = val.get("ruta") + val.get("nombre")
        if not archivoExistente(self.path):
            print(f"No existe el archivo en la ruta {self.path}")
            return False
        return True
    def verificarNombre(self):
        if self.name == "mbr":
            print("mbr")
            self.crearGrafoMBR()
            return True
        elif self.name == "disk":
            print("disk")
            return True
        elif self.name == "inode":
            print("indoe")
            return True
        elif self.name == "Journaling":
            print("Journaling")
            return True
        elif self.name == "block":
            print("block")
            return True
        elif self.name == "bm_inode":
            print("bm_inode")
            return True
        elif self.name == "bm_block":
            print("bm_block")
            return True
        elif self.name == "tree":
            print("tree")
            return True
        elif self.name == "sb":
            print("sb")
            return True
        elif self.name == "file":
            print("file")
            return True
        else: return
    """def ejecutarRep(self):
        nuevoObjetoMBR = MBR(0,0,0,"")
        data=Fread_displacement("/home/luis/Escritorio/Archivos2023/proyectos/Disco1.dsk",0,struct.calcsize(nuevoObjetoMBR.constMBR))
        nuevoObjetoMBR.doDeserialize(data)
        print("Fit: " ,deBinaString(nuevoObjetoMBR.dsk_fit))
        print("Asignature: " ,nuevoObjetoMBR.mbr_dsk_signature)
        print("Fecha de Creacion:" , nuevoObjetoMBR.mbr_fecha_creacion)
        print("Tamaño disco: " ,nuevoObjetoMBR.mbr_tamano)"""
        
    def crearGrafoMBR(self):
        
        
        
        diagrama = 'digraph G { '"\n"'a0 [shape=none label=<  <TABLE cellspacing="10" cellpadding="10" style="rounded" bgcolor="red"> <TR> <TD bgcolor="yellow">REPORTE MBR</TD> </TR>'
        
        

    
    def crearImagen(self):
        pass