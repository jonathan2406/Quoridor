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
            newNode = Node(newLinkedList)
            self.append(newNode)
            for j in range(columnas):
                otherNewNode = Node(None)
                newLinkedList.append(otherNewNode)

    def traverse(self):
        current = self.head
        while (current):
            print(current.value.value)
            salto = current.value.value.head
            current = current.right 
            while (salto):
                print(salto.value)
                salto = salto.right

    def cuadrarNodos(self, current, fila = 0):
        if fila == 0:
            currentLinkedList = current.value
            siguienteLinkedList = current.right.value
            while(siguienteLinkedList, currentLinkedList):
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                #saltos
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            self.cuadrarNodos(current.right,+1)
        if fila == self.fila:
            currentLinkedList = current.value.head
            anteriorLinkedList = current.left.value.head
            while(currentLinkedList, currentLinkedList):
                currentLinkedList.up = anteriorLinkedList
                #saltos
                anteriorLinkedList = anteriorLinkedList.right
                currentLinkedList = currentLinkedList.right
        else:
            currentLinkedList = current.value.head
            siguienteLinkedList = current.right.value.head
            anteriorLinkedList = current.left.value.head
            while(currentLinkedList,siguienteLinkedList,anteriorLinkedList):
                anteriorLinkedList.down = currentLinkedList
                currentLinkedList.up = anteriorLinkedList
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                #saltos
                anteriorLinkedList = anteriorLinkedList.right
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            self.cuadrarNodos(current.right,+1)
            
        


tablero = LinkedList()
tablero.generarTablero(2,2)
tablero.traverse()
tablero.cuadrarNodos(tablero.head)

    



        