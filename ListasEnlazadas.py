class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #Puntero
class ListaSimple:
    def __init__(self):
        self.cabeza = None #Al inicio está vacía
    def mostrar_lista(self):
            actual = self.cabeza
            while actual is not None:
                print(f"[{actual.dato}]")
                actual = actual.siguiente
            print("Fin de la lista")
    # Reto 6
    def insertar_final(self, nueva_tarea):
        nuevo_nodo = Nodo(nueva_tarea)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
    # Reto 7
    def invertir_lista(self):
        anterior = None
        actual = self.cabeza

        while actual is not None:
            siguiente = actual.siguiente

            actual.siguiente = anterior

            anterior = actual
            actual = siguiente

        self.cabeza = anterior
    # Reto 8
    def nodo_desde_final(self, n):
        if n <= 0:
            return None

        rapido = self.cabeza
        lento = self.cabeza

        for i in range(n):
            if rapido is None:
                return None

            rapido = rapido.siguiente

        while rapido is not None:
            rapido = rapido.siguiente
            lento = lento.siguiente

        return lento
    # Reto 9
    def eliminar_duplicados(self):
        actual = self.cabeza

        while actual is not None and actual.siguiente is not None:
            if actual.dato == actual.siguiente.dato:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente
    # Reto 10
    def detectar_bucle(self):
        lento = self.cabeza
        rapido = self.cabeza

        while rapido is not None and rapido.siguiente is not None:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente

            if lento is rapido:
                return True

        return False