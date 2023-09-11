class Nodo:
    def __init__(self, nombreDisco, nombreParticion, estadoParticion):
        self.nombreDisco = nombreDisco
        self.nombreParticion = nombreParticion
        self.estadoParticion = estadoParticion
        self.contador = 1
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, nombreDisco, nombreParticion, estadoParticion):
        if self.cabeza is None:
            self.cabeza = Nodo(nombreDisco, nombreParticion, estadoParticion)
        else:
            actual = self.cabeza
            while actual:
                if actual.nombreDisco == nombreDisco:
                    actual.contador += 1
                    return
                if actual.siguiente:
                    actual = actual.siguiente
                else:
                    break

            # Si no se encontró un nodo existente, crea uno nuevo con contador=1
            nuevo_nodo = Nodo(nombreDisco, nombreParticion, estadoParticion)
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            if actual.contador > 0:
                print(f"****   {actual.contador}   ********** {actual.nombreParticion} ********** 41{actual.contador}{actual.nombreDisco} **********")
                actual.contador = 0  # Reinicia el contador después de imprimirlo
            actual = actual.siguiente