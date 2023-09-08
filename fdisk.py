import ctypes
import struct
from utilities import *
from load import *
from MBR import *
from EBR import *

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
        self.temporalMBR = ""
    
    def ejecutarFDISK(self):
        if not self.agregarValores():
            print("FDISK no se pudo ejecutar correctamente")
            return
        self.leerMBR()
        if self.temporalMBR == "":
            print("Error, no se encuentra el MBR del archivo")
            return
        listaParticiones = [self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        if self.add == 0 and self.delete == '\0':
            #aca comienza todo lo que debe de hacer para agregar particiones sin usar add o delete en el comando
            if self.existeNombre(listaParticiones):
                print("FDISK no se pudo ejecutar correctamente")
                return
            if self.type == "E":
                if self.comprobarExtendida(listaParticiones):
                    print("FDISK no se pudo ejecutar correctamente")
                    print("Error, Ya existe una extendida en el disco")
                    return
            if self.type == "L":
                if not self.comprobarExtendida(listaParticiones):
                    print("FDISK no se pudo ejecutar correctamente")
                    print("Error, no se puede agregar particion logica sin una extendida")
                    return
                else: 
                    self.escribirEBR()
                    return
                
                    
            if not self.comprobarEspacio(listaParticiones):
                print("FDISK no se pudo ejecutar correctamente")
                return
            if not self.comprobar4Particiones(listaParticiones):
                print("Error FDISK, existen ya 4 particiones")
                return
            self.particionLibre(listaParticiones)
            self.temporalMBR.mbr_fecha_creacion = convertirTiempoEntero(self.temporalMBR.mbr_fecha_creacion)
            #self.temporalMBR.dsk_fit = convertirstringaBin(self.temporalMBR.dsk_fit)
            #print(self.temporalMBR.doSerialize())
            escribirArchivoExistente(self.path, 0, self.temporalMBR.doSerialize())
            
        if self.delete != '\0':
            print("entro en delete")
            self.eliminarEBR(self.name)
            self.buscarPartExtendida(listaParticiones)
            
            
    
    def agregarValores(self):
        for val in self.listaParametros:
            if val.get("valorsize") != None:
                self.size = int(val.get("valorsize"))
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
        #print(self.listaParametros)
        if self.size <=0:
            print(f"El valor de size en fdisk {self.size} debe ser mayor a 0")
            return False
        if not archivoExistente(self.path):
            print(f"No existe el archivo en la ruta {self.path}")
            return False
        
        self.calcularValoresSize()
        self.tipoDeParticion()
        self.fit = convertirValoresFit(self.fit)
        return True
    
    
    def calcularValoresSize(self):
        if self.unit.lower() == "b": #byes
            print("particion en bytes")
        elif self.unit.lower() == "k": #kilobytes
            self.size = self.size * 1024
            print("particion en kilobytes")
        elif self.unit.lower() == "m": #megabytes
            self.size = self.size * 1024 * 1024
            print("particion en megabytes")
        else: print(f"Error, el valor {self.unit} de unit no es valido")
    
    def tipoDeParticion(self):
        if self.type.lower() == "p":
            print("particion primaria")
        elif self.type.lower() == "e":
            print("particion extendida")
        elif self.type.lower() == "l":
            print("particion logica")
        else: print(f"Error, el valor {self.type} de type no es valido")
    
    
    def leerMBR(self):
        temporalMBR = MBR(0,0,0,0)
        datos = Fread_displacement(self.path,0,struct.calcsize(temporalMBR.constMBR) + struct.calcsize(temporalMBR.particion1.constanteParticion)*4)
        temporalMBR.doDeserialize(datos) #ya tenemos los datos del mbr
        self.temporalMBR = temporalMBR
        
        
    def existeNombre(self, listaparticiones): #aca verificamos si el nombre de la particion existe
        for particion in listaparticiones:
            if particion.part_name == self.name:
                print("El nombre de la particion ya existe")
                return True
        return False
    
    def particionLibre(self, listaparticiones): #aca vamos a escribir la particion en el archivo binario
        for particion in listaparticiones:
            if particion.part_status == "\x00":
                self.crearParticion(particion)
                return
            
    def crearParticion(self,particion):
        particion.part_status = "1"
        particion.part_type = self.type
        particion.part_fit = self.fit
        particion.part_start = self.comprobarStart([self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4])
        particion.part_s = self.size
        particion.part_name = self.name
        
        
    def comprobarEspacio(self, listaparticiones):
        cantidadEspacio = 0
        for particion in listaparticiones:
            if particion.part_status != "\x00":
                cantidadEspacio += particion.part_s
        if self.temporalMBR.mbr_tamano < cantidadEspacio + self.size:
            print("No existe espacio suficiente para la particion que desea crear")
            return False
        return True
    
    def comprobar4Particiones(self, listaparticiones):
        for particion in listaparticiones:
            if particion.part_status == "\x00":
                return True
        return False
    
    def comprobarExtendida(self, listaparticiones):
        for particion in listaparticiones:
            if particion.part_type == "E":
                return True
        return False
    
    def comprobarStart(self, listaparticiones):
        partStart = struct.calcsize(self.temporalMBR.constMBR) + struct.calcsize(self.temporalMBR.particion1.constanteParticion)*4
        for particion in listaparticiones:
            if particion.part_status != "\x00":
                partStart += particion.part_s
        return partStart
    
    def retornarExtendida(self, listaparticiones):
        for particion in listaparticiones:
            if particion.part_type == "E":
                return particion
    
    
    def escribirEBR(self):
        actualEBR = EBR()
        listaparticiones = [self.temporalMBR.particion1,self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        particionExtendida = self.retornarExtendida(listaparticiones)
        tam = struct.calcsize(actualEBR.constanteEBR)
        datosEBR = Fread_displacement(self.path,particionExtendida.part_start,tam)
        actualEBR.doDeserialize(datosEBR)
        actualizarSize = particionExtendida.part_s
        #comienza la lista enlazada
        if actualizarSize < self.size:
            print("Error, no se puede crear la particion Logica")
            return        
        if actualEBR.part_s == 0: #es el primer ebr
            actualEBR.part_status = "1"
            actualEBR.part_fit = self.fit
            actualEBR.part_start = particionExtendida.part_start
            actualEBR.part_s = self.size
            actualEBR.part_next = -1
            actualEBR.part_name = self.name
            escribirArchivoExistente(self.path, particionExtendida.part_start, actualEBR.doSerialize())
            #print(particionExtendida.part_start)
        while actualEBR.part_next != -1:
            actualEBR.doDeserialize(Fread_displacement(self.path, actualEBR.part_next, tam))  #porque debemos de leer el siguiente
            actualizarSize -= actualEBR.part_s
            if actualEBR.part_name == self.name:
                print("Ya existe la particion logica")
                return
        actualEBR.part_next = actualEBR.part_start + self.size
        escribirArchivoExistente(self.path,actualEBR.part_start,actualEBR.doSerialize())#solo su next
        nuevoEBR = EBR()
        nuevoEBR.part_status = "1"
        nuevoEBR.part_fit = self.fit
        nuevoEBR.part_start = actualEBR.part_next
        nuevoEBR.part_s = self.size
        nuevoEBR.part_next = -1
        nuevoEBR.part_name = self.name
        escribirArchivoExistente(self.path, nuevoEBR.part_start, nuevoEBR.doSerialize())
        
    def verificarNombreEliminar(self, listaparticiones): #esto es para particiones primarias
        for particion in listaparticiones:
            if particion.part_name == self.name:
                return True
        return False
        
    
    def eliminarEBR(self, nombre):
        actualEBR = EBR()
        listaparticiones = [self.temporalMBR.particion1, self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        particionExtendida = self.retornarExtendida(listaparticiones)
        tam = struct.calcsize(actualEBR.constanteEBR)
        if particionExtendida.part_s == 0:
            print("No hay particiones lógicas en la partición extendida.")
            return
        # Leer el primer EBR
        datosEBR = Fread_displacement(self.path, particionExtendida.part_start, tam)
        actualEBR.doDeserialize(datosEBR)
        
        #para eliminar el primer ebr
        if actualEBR.part_name == nombre:
            # Eliminar el primer EBR ajustando los punteros
            particionExtendida.part_start = actualEBR.part_next
            particionExtendida.part_s -= tam  # Restar el tamaño de los datos del EBR eliminado
            #sobre escribir archivo
            escribirArchivoExistente(self.path, particionExtendida.part_start, particionExtendida.doSerialize())
            print(f"Partición lógica {nombre} eliminada.")
            return
        
        while actualEBR.part_next != -1:
            datosEBR = Fread_displacement(self.path, actualEBR.part_next, tam)
            siguienteEBR = EBR()
            siguienteEBR.doDeserialize(datosEBR)
            if siguienteEBR.part_name == nombre:
                actualEBR.part_next = siguienteEBR.part_next
                particionExtendida.part_s -= tam  # Restar el tamaño de los datos del EBR eliminado 
                escribirArchivoExistente(self.path, actualEBR.part_start, actualEBR.doSerialize())
                print(f"Partición lógica {nombre} eliminada.")
                return
            
            actualEBR = siguienteEBR
        print(f"No se encontró la partición lógica {nombre}.")
        
    
    def eliminarParticionesLogicas(self, path, start, size):
        # Calcular el número de bytes que ocupan las particiones lógicas
        actualEBR = EBR()
        tam_particion_logica = struct.calcsize(actualEBR.constanteEBR)

        # Calcular el número de particiones lógicas dentro de la partición extendida
        num_particiones_logicas = size // tam_particion_logica

        # Eliminar cada partición lógica dentro de la partición extendida
        for i in range(num_particiones_logicas):
            # Calcular la posición de inicio de la partición lógica
            offset = start + (i * tam_particion_logica)

            # Eliminar la partición lógica sobrescribiendo con caracteres nulos
            escribirArchivoExistente(path, offset, b'\0' * tam_particion_logica)

    def eliminarParticionExtendida(self):
        listaparticiones = [self.temporalMBR.particion1, self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4]
        for i, particion in enumerate(listaparticiones):
            if particion.part_type == 'E':  # Verificar si es una partición extendida
                particionExtendida = particion
                tam_part_extendida = particionExtendida.part_s

                # Eliminar particiones lógicas dentro de la partición extendida
                self.eliminarParticionesLogicas(self.path, particionExtendida.part_start, tam_part_extendida)

                # Eliminar la partición extendida sobrescribiendo con caracteres nulos
                escribirArchivoExistente(self.path, particionExtendida.part_start, b'\0' * tam_part_extendida)

                # Actualizar la información en la lista de particiones
                listaparticiones[i] = PARTICION()  # Crear una partición vacía en ese lugar

                # Actualizar la información en el MBR
                self.temporalMBR.particion1, self.temporalMBR.particion2, self.temporalMBR.particion3, self.temporalMBR.particion4 = listaparticiones

                # Escribir el MBR actualizado en el disco
                escribirArchivoExistente(self.path, 0, self.temporalMBR.doSerialize())

                print("Partición extendida y sus particiones lógicas eliminadas.")
                return

        print("No se encontró una partición extendida.")

    def buscarPartExtendida(self, listaparticiones):
        for particion in listaparticiones:
            if particion.part_type == self.type:
                if particion.part_name == self.name:
                    self.eliminarParticionExtendida()
                    print("particion extendida eliminada con exito")
                    return
        