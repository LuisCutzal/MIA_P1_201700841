class Nodo:
    def __init__(self, nombreParticion, identificador):
        self.nombreParticion = nombreParticion
        self.identificador = identificador
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contadores = {}  # Un diccionario para llevar el contador por nombre de disco
        self.indice = 0

    def agregar_elemento(self, nombreDisco, nombreParticion, estadoParticion):
        if nombreDisco not in self.contadores:
            self.contadores[nombreDisco] = 1
        else:
            self.contadores[nombreDisco] += 1
        
        numeroparticion = self.contadores[nombreDisco]
        identificador = f"41{numeroparticion}{nombreDisco}"
        nuevo_nodo = Nodo(nombreParticion, identificador)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.indice += 1

    
    def eliminar_disco(self, nombreDisco):
        actual = self.cabeza
        previo = None

        while actual:
            if actual.identificador.startswith(f"41{nombreDisco}"):
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.indice -= 1  # Disminuir el índice ya que se eliminó una partición
            previo = actual
            actual = actual.siguiente
                
    
    
    def imprimir_lista(self):
        actual = self.cabeza
        indice = 1
        while actual:
            print(f"**** {indice} ********** {actual.nombreParticion} ********** {actual.identificador} **********")
            actual = actual.siguiente
            indice +=1
