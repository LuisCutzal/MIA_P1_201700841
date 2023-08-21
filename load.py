import ctypes

def leerArchivo(archivo): #para el path del archivo de entrada 
    try:
        data = archivo.read()
        archivo.close()
        return data
    except Exception as e:
        print(f"Error al leer objeto: {e}")
        

def Fcreate_file(fileName):
    try:
        fileOpen = open(fileName, "wb")
        fileOpen.close()
        print("Archivo creado exitosamente")
        return False
    except Exception as e:
        print(f"Error al crear archivo: {e}")
        return True

def Winit_size(file, size_mb):
    buffer = b'\0' * 1024 * size_mb * 1024
    print(f"Tamaño del archivo: {len(buffer)} bytes")
    file.write(buffer)
    print("Tamaño aplicado")
    