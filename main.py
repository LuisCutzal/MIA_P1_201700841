import os
import ctypes



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
                print("funciona")
                print(direccionPath)

if __name__ == "__main__":
    main()
                