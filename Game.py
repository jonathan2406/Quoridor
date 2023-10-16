class Node:
    def __init__(self, value):
        self.value = value
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return "es un nodo"
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.filas = None
        self.columnas = None

    def __repr__(self) -> str:
        return "lista enlazada"

    def append(self, value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node

    def generarTablero(self, filas, columnas):
        self.filas = filas-1
        self.columnas = columnas-1
        for i in range(filas):
            newLinkedList = LinkedList()
            self.append(newLinkedList)
            for j in range(columnas):
                if i == 0 and j == 0:
                    newLinkedList.append("player1")
                elif i == filas-1 and j == columnas-1:
                    newLinkedList.append("player2")
                else:
                    newLinkedList.append(None)

    def traverse(self):
        current = self.head
        while (current):
            print(current.value)
            salto = current.value.head
            current = current.right 
            while (salto):
                print(salto)
                salto = salto.right

    def cuadrarNodos(self, current, fila = 0):
        if fila == 0:
            currentLinkedList = current.value.head
            siguienteLinkedList = current.right.value.head
            while(siguienteLinkedList):
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                #saltos
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            self.cuadrarNodos(current.right,fila+1)
        elif fila == self.filas:
            currentLinkedList = current.value.head
            anteriorLinkedList = current.left.value.head
            while(currentLinkedList):
                currentLinkedList.up = anteriorLinkedList
                #saltos
                anteriorLinkedList = anteriorLinkedList.right
                currentLinkedList = currentLinkedList.right
        else:
            currentLinkedList = current.value.head
            siguienteLinkedList = current.right.value.head
            anteriorLinkedList = current.left.value.head
            while(currentLinkedList):
                anteriorLinkedList.down = currentLinkedList
                currentLinkedList.up = anteriorLinkedList
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                #saltos
                anteriorLinkedList = anteriorLinkedList.right
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            self.cuadrarNodos(current.right,fila+1)
            

class LinkedListVisual:
    def __init__(self):
        self.matriz = None

    def actualizarTablero(self, head):
        self.matriz = []
        self.generarTableroVisual(head)

    def generarTableroVisual(self, currentLinkedList):
        if (currentLinkedList is not None):
            current = currentLinkedList
            salto = current.value.head
            fila = []
            self.matriz.append(fila)
            while (salto):
                if salto.value == None:
                    fila.append("-")
                elif salto.value == "#":
                    fila.append("#")
                elif salto.value == "player1":
                    fila.append("P1")
                elif salto.value == "player2":
                    fila.append("P2")
                salto = salto.right 
            self.generarTableroVisual(current.right)
    def imprimirTablero(self):
        for fila in self.matriz:
            print(fila)

        
tablero = LinkedList()
tablero.generarTablero(5,5)
tablero.cuadrarNodos(tablero.head)
tableroVisual = LinkedListVisual()
tableroVisual.actualizarTablero(tablero.head)
tableroVisual.imprimirTablero()


    



        