from LinkedList import LinkedList
from LinkedListVisual import LinkedListVisual

class Tablero:

    def __init__(self):
        self.tablero = None
        self.tableroVisual = None

    def generarTablero(self, filas, columnas):
        tablero = LinkedList()
        tablero.generarTablero(int(filas), int(columnas))
        tablero.cuadrarNodos(tablero.head)
        tableroVisual = LinkedListVisual()
        tableroVisual.actualizarTablero(tablero.head)
        self.tablero = tablero
        self.tableroVisual = tableroVisual

    def getNodojugador(self, jugador):
        currentLinkedList = self.tablero.head
        currentNode = currentLinkedList.value.head
        while(currentLinkedList):
            while(currentNode):
                if currentNode.value == jugador:
                    return currentNode
                currentNode = currentNode.right
            currentNode = currentLinkedList.right.value.head
            currentLinkedList = currentLinkedList.right

    def getNodoPorPosicion(self, fila, columna):
        currentLinkedList = self.tablero.head

        for i in range(fila):
            currentLinkedList = currentLinkedList.right

        currentNode = currentLinkedList.value.head
        for j in range(columna):
            currentNode = currentNode.right

        return currentNode
    
    def bloqueo(self, fila, columna):
        nodoBloquear = self.getNodoPorPosicion(fila, columna)
        if nodoBloquear.value == "#":
            print("Ya hay un bloqueo en esa posición")
            return False
        elif nodoBloquear.value != None:
            print("No puedes bloquear donde hay un jugador")
            return False
        nodoBloquear.value = "#"
        verificacionp1 = self.verificarGanarP1(self.getNodojugador("Player1"))
        print(f"Valor verificación P1: {verificacionp1}")
        verificacionp2 = self.verificarGanarP2(self.getNodojugador("Player2"))
        print(f"Valor verificación P2: {verificacionp2}")
        self.tableroVisual.actualizarTablero(self.tablero.head)

        if verificacionp1 == True and verificacionp2 == True:
            return True
        else:
            nodoBloquear.value = None
            return False

    def desplazarArriba(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.up is None:
            if jugador == "Player1":
                return False

        if nodoJugador.up is not None:
            if nodoJugador.up.value != None:
                return False
            if nodoJugador.up.up == None and jugador != "Player1":
                return True
            nodoJugador.value = None
            nodoJugador.up.value = jugador
            self.tableroVisual.actualizarTablero(self.tablero.head)

    def desplazarAbajo(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.down is None:
            if jugador == "Player2":
                return False
        if nodoJugador.down.value != None:
            return 
        if nodoJugador.down.down is None and jugador != "Player2":
            return True
        nodoJugador.value = None
        nodoJugador.down.value = jugador
        self.tableroVisual.actualizarTablero(self.tablero.head)

    def desplazarDerecha(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.right is None:
            return False
        if nodoJugador.right.value != None:
            return False
        nodoJugador.value = None
        nodoJugador.right.value = jugador
        self.tableroVisual.actualizarTablero(self.tablero.head)

    def desplazarIzquierda(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.left is None:
            return False
        if nodoJugador.left.value != None:
            return False
        nodoJugador.value = None
        nodoJugador.left.value = jugador
        self.tableroVisual.actualizarTablero(self.tablero.head)

    def verificarGanarP1(self, nodo, visitados=None):
        if visitados is None:
            visitados = LinkedList()

        if nodo is None or visitados.contiene(nodo) == True or nodo.value == "#" or nodo.value == "Player2":
            return False

        if nodo.down is None:
            return True

        visitados.append(nodo)

        arriba = self.verificarGanarP1(nodo.up,visitados)
        abajo = self.verificarGanarP1(nodo.down,visitados)
        derecha = self.verificarGanarP1(nodo.right,visitados)
        izquierda = self.verificarGanarP1(nodo.left,visitados)

        return arriba or abajo or derecha or izquierda

    def verificarGanarP2(self, nodo, visitados=None):
        if visitados is None:
            visitados = LinkedList()
        if nodo is None or visitados.contiene(nodo) == True or nodo.value == "#" or nodo.value == "Player1":
            return False

        if nodo.up is None:
            return True

        visitados.append(nodo)

        arriba = self.verificarGanarP2(nodo.up,visitados)
        abajo = self.verificarGanarP2(nodo.down,visitados)
        derecha = self.verificarGanarP2(nodo.right,visitados)
        izquierda = self.verificarGanarP2(nodo.left,visitados)

        return arriba or abajo or derecha or izquierda
