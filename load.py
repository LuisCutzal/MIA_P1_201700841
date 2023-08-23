import ctypes

def leerArchivo(archivo): #para el path del archivo de entrada 
    try:
        data = archivo.read()
        archivo.close()
        return data
    except Exception as e:
        print(f"Error al leer objeto: {e}")
        
def Fwrite_displacement(file, displacement, obj):
    data = obj.doSerialize()
    file.seek(displacement)
    file.write(data)

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
    buffer = b'\0' * size_mb
    print(f"Tamaño del archivo: {len(buffer)} bytes")
    file.write(buffer)
    print("Tamaño aplicado")
    