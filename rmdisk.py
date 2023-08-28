import os

class RMDISK():
    def __init__(self):
        pass
    
    def ejecutarRMDISK(self,diccionarioRuta):
        ruta = diccionarioRuta['rutaArchivo'] + diccionarioRuta['nombrearchivo']
        #print(ruta)
        if os.path.exists(ruta):
            os.remove(ruta)
            print(f"El archivo {diccionarioRuta['nombrearchivo']} fue eliminado")
        else: print("El archivo no existe")
        