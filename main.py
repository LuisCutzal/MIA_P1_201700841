import os
import ctypes
import re
from load import *

def main():
    print("Luis Antonio Cutzal Chalí")
    print("201700841")
    print("Proyecto 1")
    aplicacionComandos()

def aplicacionComandos():
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
                print(direccionPath)
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
                        for buscoParametro in range(1,len(separamosLineaComando)): #se debe de iniciar en 1 para omitir el mkdisk
                            primerSplitComandos = separamosLineaComando[buscoParametro].split('=')
                            #print(primerSplitComandos)
                            segundoSplitComandos = primerSplitComandos[0].split('-')
                            #print(segundoSplitComandos)
                            if(segundoSplitComandos[1].lower() == "size"):
                                print("entro en size")
                                valorSize = primerSplitComandos[1]
                                if(valorSize > 0):
                                    print(valorSize)
                            if(segundoSplitComandos[1].lower() == "path"):
                                print("entro en path")
                                valorPath = primerSplitComandos[1]
                                print(valorPath)
                            if(segundoSplitComandos[1].lower() == "unit"): #es opcional, si no se muestra entonces debe de crearse un disco en megas
                                print("entro en unit")
                                valorUnit = primerSplitComandos[1]
                                print(valorUnit)
                            if(segundoSplitComandos[1].lower() == "fit"): #como es opcional se tomara siempre el primer ajuste (FF)
                                print("entro en fit")
                                valorFit = primerSplitComandos[1]
                                print(valorFit)
                            
                                                      
                         
                            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    if (separamosLineaComando[0].lower() == "rmdisk"):
                        print("reconoce comando rmdisk") #eliminar archivo
                    if (separamosLineaComando[0].lower() == "fdisk"):
                        print("reconoce el comando fdisk")
                    if(separamosLineaComando[0].lower() == "rep"):
                        print("reconoce comando rep")


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
    print("U1nit")
            
if __name__ == "__main__":
    main()

# execute -path=/home/luis/Escritorio/Archivos2023/proyectos/MIA_P1_201700841/prueba.adsj
#mkdisk - size=3000 -unit=K -path=/home/user/Disco1.dsk

