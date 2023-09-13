import os
import ctypes
import re
from load import *
from ArchivoComandos import iniciarAnalisis

    
    
#hexdump -s 2173 -n 400 -Cv /home/luis/Escritorio/Archivos2023/proyectos/Disco1.dsk | head -n 100

def aplicacionComandos():
    input = iniciarAnalisis("execute -path=/home/luis/Escritorio/Archivos2023/proyectos/MIA_P1_201700841/prueba.adsj")
    #print(input)
    iniciarAnalisis(input)
   
    """while True: 
        #iniciarAnalisis(input("-> "))
        iniciamos = iniciarAnalisis(input("-> "))
        #print(input)
        iniciarAnalisis(iniciamos)"""
    
    
    '''
    while True:
        comandoIngresado = input("-> ")
        analizarComando = comandoIngresado.split(' ')
        #el primer comando que se debe analizar el es execute
        if(len(analizarComando) <=1):
            print("error")
        else:
            #execute -path=/home/Desktop/calificacion.ads
            comandoExecute = analizarComando[0]
            if(comandoExecute.lower() == "execute"):#aca se encontro el comando execute
                siguienteParametro = analizarComando[1].split('=')
                obtenerPath = siguienteParametro[0].split('-')
                comandoPath = obtenerPath[1]
                direccionPath = siguienteParametro[1]
            if(comandoPath.lower() == "path"):
                #print(direccionPath)
                archivo = open(direccionPath, "r")
                contenidoLeido = leerArchivo(archivo)#aca ya leemos todo lo que esta dentro del archivo                
                comandosArchivo = contenidoLeido.split('\n') #separamos con split para tomar todas las lineas del archivo que estamos leyendo
                #print(comandosArchivo)
                for buscamosComando in range(len(comandosArchivo)):
                    reconocerComentarios(comandosArchivo[buscamosComando]) #es una funcion para los comentarios
                    
                    lineaComando = comandosArchivo[buscamosComando] #aca ya esta por saltos de linea cada comando, se debe de hacer el split
                    separamosLineaComando = lineaComando.split(' ') #aca las lineas de comando son divididas por espacios vacios
                    #no logro entender cuando viene un path con espacios por ejemplo: -path="/home/mis discos/Disco3.dsk" el espacio de "mis discos" no se como trabajarlo
                    #creo que ya se,  puedo concatenar las 2 partes del path por ejemplo separamosLineaComando[1] + separamosLineaComando[2] creo que con esto ya funciona
                    #print(separamosLineaComando)
                        
                    if(separamosLineaComando[0].lower() == 'mkdisk'):
                        # execute -path=/home/luis/Escritorio/Archivos2023/proyectos/MIA_P1_201700841/prueba.adsj
                        banderaUnit = False
                        banderaFit = False
                        
                        buscarUnit = '-unit='
                        buscarFit = '-fit='
                        
                        unitEncontrado = buscandoUnit(separamosLineaComando,buscarUnit)
                        fitEncontrado = buscandoFit(separamosLineaComando,buscarFit)
                        
                        if(unitEncontrado != -1):
                            banderaUnit = True #aca si existe entonces hace todo el proceso del unit
                        else: print("Aqui se crea el disco por defecto en Megabytes") #desde aca trabajaria
                        
                        if(fitEncontrado != -1):
                            banderaFit = True #aca si existe entonces hace todo el proceso del unit
                        else: print("Aqui se crea el disco por defecto con FF") #desde aca trabajaria
                        
                        for buscoParametro in range(1,len(separamosLineaComando)): #se debe de iniciar en 1 para omitir el mkdisk
                            primerSplitComandos = separamosLineaComando[buscoParametro].split('=')
                            #print(primerSplitComandos)
                            segundoSplitComandos = primerSplitComandos[0].split('-')
                            #print(segundoSplitComandos)
                            
                            if(segundoSplitComandos[1].lower() == "path"):
                                #print("entro en path")
                                valorPath = primerSplitComandos[1]
                                #print(valorPath)
                                
                            elif(segundoSplitComandos[1].lower() == "size"):
                                valorSize = primerSplitComandos[1]
                                #if(int(valorSize) >= 1):
                                    #print("valor" + valorPath)
                                    #tamaño del disco a crear
                                    #Crrfile = open(valorPath, "rb+") #lectura y escritura
                                    #Winit_size(Crrfile,int(valorSize))#le paso el archivo abierto
                                    
                            if(banderaUnit == True):
                                if(segundoSplitComandos[1].lower() == "unit"):
                                    print("entro en unit")
                                    valorUnit = primerSplitComandos[1] #aca tenemos el valor, ya sea K o M
                                    print(valorUnit)
                                    if(valorUnit.lower() == 'k'):
                                        print("kilobytes")
                                    else: print("Megabytes")
                            #else: print("Aqui se crea el disco por defecto en Megabytes")
                            
                            
                            
                            #if(segundoSplitComandos[1].lower() == "unit"): #es opcional, si no se muestra entonces debe de crearse un disco en megas
                            
                            if(banderaFit == True):
                                if(segundoSplitComandos[1].lower() == "fit"): #como es opcional se tomara siempre el primer ajuste (FF)
                                    print("entro en fit")
                                    valorFit = primerSplitComandos[1]
                                    print(valorFit)
                                    if(valorFit.lower() == "bf"):
                                        print("Indicará el mejor ajuste")
                                    elif(valorFit.lower() == "ff"):
                                        print("Utilizará el primer ajuste")
                                    elif(valorFit.lower() == "wf"):
                                        print("Utilizará el peor ajuste")
                                    else:print("error")

                    if (separamosLineaComando[0].lower() == "rmdisk"):
                        print("reconoce comando rmdisk") #eliminar archivo
                    if (separamosLineaComando[0].lower() == "fdisk"):
                        print("reconoce el comando fdisk")
                    if(separamosLineaComando[0].lower() == "rep"):
                        print("reconoce comando rep")


'''

def reconocerComentarios(datos):
    lineas = datos.split('\n')
    indice = len(lineas)
    #print(indice)
    for linea in lineas:
        exprecionRegular = re.compile('#(\w*\s*)', re.IGNORECASE)
        if(exprecionRegular.match(linea) != None): 
            print("es un comentario: "+linea) #funciona la parte de saber los comentarios
            
    
        
        #else: print("No es un comentario")
        
        
def reconoceSize():
    print("Size")
    
def reconocePath():
    print("Path")

def reconoceUnit():
    print("Unit")
    
    
def buscandoUnit(lista, unit):
    contador = 0
    for indice, elemento in enumerate(lista):
        if elemento == unit+'K' or elemento == unit+'M' or elemento == unit+'m' or elemento == unit+'k':
            return elemento
    return -1    

def buscandoFit(lista, fits):
    contador = 0
    for indice, elemento in enumerate(lista):
        if elemento == fits+'BF' or elemento == fits+'FF' or elemento == fits+'WF' or elemento == fits+'bf' or elemento == fits+'ff' or elemento == fits+'wf':
            return elemento
    return -1 



if __name__ == "__main__":
    print("Luis Antonio Cutzal Chalí")
    print("201700841")
    print("Proyecto 1")
    aplicacionComandos()

# execute -path=/home/luis/Escritorio/Archivos2023/proyectos/MIA_P1_201700841/prueba.adsj
#mkdisk - size=3000 -unit=K -path=/home/user/Disco1.dsk

