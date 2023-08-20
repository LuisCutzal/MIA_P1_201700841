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
                for buscamosComando in range(len(comandosArchivo)):
                    reconocerComentarios(comandosArchivo[buscamosComando])
                    if(comandosArchivo[buscamosComando] == 'mkdisk'):
                        print("reconoce comando mkdisk")
                    if(comandosArchivo[buscamosComando] == "rep"):
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


            
if __name__ == "__main__":
    main()

# execute -path=/home/luis/Escritorio/Archivos2023/proyectos/MIA_P1_201700841/prueba.adsj
#mkdisk - size=3000 -unit=K -path=/home/user/Disco1.dsk

