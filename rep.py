from MBR import *
from EBR import *
from load import *
import struct

class REP():
    def __init__(self, listaparametros):
        self.listaparametros = listaparametros
        self.identificador = "" #Indica el id de la partición que se utilizará
        self. path =""
        self.name = "" #Nombre del reporte a generar. 
        self.ruta = ""
        self.temporalMBR = ""
        
    def ejecutarRep(self, listaMount):
        if not self.agregarvalores():
            print("El comandno rep no se pudo ejecutar correctamente")
            return
        if not self.verificarNombre():
            print("El nombre que ingreso en el comando REP no es valido")
            return
        self.crearGrafoMBR(listaMount)
        
        
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
            print("Generar reporte MBR")
            return True
        elif self.name == "disk":
            print("Generar reporte DISK")
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
        
    
    
    def crearGrafoMBR(self,listaMount):
        direccion=""
        for identificadores in listaMount:
            if identificadores['id'] == self.identificador:
                direccion= identificadores['path']
                particion = identificadores['particion']
                temporalMBR = MBR(0,0,0,0)
                datos = Fread_displacement(direccion,0,struct.calcsize(temporalMBR.constMBR) + struct.calcsize(temporalMBR.particion1.constanteParticion)*4)
                temporalMBR.doDeserialize(datos) #ya tenemos los datos del mbr
                self.temporalMBR = temporalMBR
                listaParticiones = [self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
                print("Reporte de MBR")
                tamanoMBR = self.temporalMBR.mbr_tamano
                fechacreacionMBR = self.temporalMBR.mbr_fecha_creacion
                asignatureMBR = self.temporalMBR.mbr_dsk_signature
                print(f"tamaño mbr {tamanoMBR}")
                print(f"fecha creacion mbr {fechacreacionMBR}")
                print(f"asignature mbr {asignatureMBR}")
                for particion in listaParticiones:
                    if particion.part_type == "E":
                        ebr_start = particion.part_start
                        print("Particion")
                        print(f"part status {particion.part_status}")
                        print(f"part next {particion.part_type}")
                        print(f"part fit {particion.part_fit}")
                        print(f"part start {particion.part_start}")
                        print(f"part size {particion.part_s}")
                        print(f"part name {particion.part_name}")
                        while True:
                            actualEBR = EBR()
                            tamanioEBR = struct.calcsize(actualEBR.constanteEBR)
                            datosEBR = Fread_displacement(direccion, ebr_start, tamanioEBR)
                            actualEBR.doDeserialize(datosEBR)
                            print("Particion logica")
                            if actualEBR.part_status == "1":
                                print(f"part status: {actualEBR.part_status}")
                                print(f"part next: {actualEBR.part_next}")
                                print(f"part fit: {actualEBR.part_fit}")
                                print(f"part start: {actualEBR.part_start}")
                                print(f"part size: {actualEBR.part_s}")
                                print(f"part name: {actualEBR.part_name}")
                            if actualEBR.part_next == -1:
                                break  # No hay más EBRs en la partición extendida
                            ebr_start = actualEBR.part_next  #Siguiente EBR
                    elif particion.part_status == "1":
                        print("Particion")
                        print(f"part status {particion.part_status}")
                        print(f"part next {particion.part_type}")
                        print(f"part fit {particion.part_fit}")
                        print(f"part start {particion.part_start}")
                        print(f"part size {particion.part_s}")
                        print(f"part name {particion.part_name}")
                        # Imprime otros campos de la partición primaria según tus necesidades
                return
        print(f"No se encontro el Disco")
        diagrama = 'digraph G { '"\n"'a0 [shape=none label=<  <TABLE cellspacing="10" cellpadding="10" style="rounded" bgcolor="red"> <TR> <TD bgcolor="yellow">REPORTE MBR</TD> </TR>'
    
    def crearImagen(self):
        pass
    
    
    """
    temporalParticion=""
                for part in listaParticiones:
                    if particion.part_type == "E":
                        temporalParticion = part
                if temporalParticion == "":
                    return
                actualEBR = EBR()
                tamanioEBR = struct.calcsize(actualEBR.constanteEBR)
                datosEBR = Fread_displacement(direccion, temporalParticion.part_start, tamanioEBR)
                actualEBR.doDeserialize(datosEBR)
                while actualEBR.part_next != -1:
                    datosEBR = Fread_displacement(direccion, actualEBR.part_next, tamanioEBR)
                    siguienteEBR = EBR()
                    siguienteEBR.doDeserialize(datosEBR)
                    print("ho")
                    print(siguienteEBR.part_status)
                    print(siguienteEBR.part_fit)
                    print(siguienteEBR.part_start)
                    print(siguienteEBR.part_s)
                    print(siguienteEBR.part_next)
                    print(siguienteEBR.part_name)
                    actualEBR = siguienteEBR
                return
    
    """
    
    
    """
                for particion in listaParticiones:
                    if particion.part_type == "E":
                        ebr_start = particion.part_start
                        while True:
                            actualEBR = EBR()
                            tamanioEBR = struct.calcsize(actualEBR.constanteEBR)
                            datosEBR = Fread_displacement(direccion, ebr_start, tamanioEBR)
                            actualEBR.doDeserialize(datosEBR)
                            if actualEBR.part_status == "1":
                                print(f"Nombre de la partición lógica: {actualEBR.part_name}")
                                # Imprime otros campos de EBR según tus necesidades

                            if actualEBR.part_next == -1:
                                break  # No hay más EBRs en la partición extendida

                            ebr_start = actualEBR.part_next  # Siguiente EBR
    """