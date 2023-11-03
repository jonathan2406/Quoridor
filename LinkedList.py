from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.filas = None
        self.columnas = None

    def __repr__(self) -> str:
        return "Lista enlazada"

    # metodo append el cual toma un valor y va a pegarlo en la lista enlazada
    def append(self, value):
        new_node = Node(value)
        # si la cabeza esta vacia significa que no existe nada en ella por lo que el nodo que creamos pasa a
        # ser la cabeza
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            # si no esta vacia cuadramos la cola y cuadramos la derecha e izquierda de los nodos
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node

    # metodo que se encarga de generar una "matriz" pero con listas enlazadas
    def generarTablero(self, filas, columnas):
        self.filas = filas - 1
        self.columnas = columnas - 1
        # creamos una lista enlazada de listas enlazadas en la que ellas representaran las filas de nuestra matriz y
        # el contenido de ellas las columnas
        for i in range(filas):
            newLinkedList = LinkedList()
            self.append(newLinkedList)
            for j in range(columnas):
                # si la "fila" es la primera y la "columna" tambien pegamos el jugador 1
                if i == 0 and j == 0:
                    newLinkedList.append("Player1")
                # hacemos lo mismo para pegar el segundo jugador en el ultimo nodo de la ultima lista enlazada
                elif i == filas - 1 and j == columnas - 1:
                    newLinkedList.append("Player2")
                else:
                    newLinkedList.append(None)

    # metodo para recorrer toda la lista enlazada a profundidad
    def traverse(self):
        current = self.head
        while (current):
            print(current.value)
            salto = current.value.head
            current = current.right
            while (salto):
                print(salto)
                salto = salto.right

    # metodo el cual cuadra los nodos de las sublistas enlazadas con el up y down para comunicarse entre ellos
    def cuadrarNodos(self, current, fila=0):
        # si estamos parados en la primera lista enlazada entonces significa que todos esos nodos solo pueden
        # apuntar para abajo
        if fila == 0:
            # nodos los cuales vamos a cuadrar
            currentLinkedList = current.value.head
            siguienteLinkedList = current.right.value.head
            # bucle que me verifica que el nodo donde estemos parados exista
            while (siguienteLinkedList):
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                # saltos
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            # llamado recursivo para que siga con el resto de la matriz
            self.cuadrarNodos(current.right, fila + 1)
        # si nuestro auxiliar fila es igual a la cantidad de filas significa que estamos parados en la
        # ultima fila lo cual significa que los nodos de esa lista enlazada deben apuntar para arriba
        elif fila == self.filas:
            # nodos los cuales vamos a cuadrar
            currentLinkedList = current.value.head
            anteriorLinkedList = current.left.value.head
            # bucle que me verifica que el nodo donde estemos parados exista
            while (currentLinkedList):
                currentLinkedList.up = anteriorLinkedList
                # saltos
                anteriorLinkedList = anteriorLinkedList.right
                currentLinkedList = currentLinkedList.right
                # aqui ya no necesitamos llamo recursivo ya que es la ultima fila de la matriz
        # y si no es ninguno de los anteriores significa que los nodos de la lista enlazada deben apuntar
        # para arriba y abajo
        else:
            # nodos los cuales vamos a cuadrar
            currentLinkedList = current.value.head
            siguienteLinkedList = current.right.value.head
            anteriorLinkedList = current.left.value.head
            # bucle que me verifica que el nodo donde estemos parados exista
            while (currentLinkedList):
                # actualizacion de punteros
                anteriorLinkedList.down = currentLinkedList
                currentLinkedList.up = anteriorLinkedList
                currentLinkedList.down = siguienteLinkedList
                siguienteLinkedList.up = currentLinkedList
                # saltos
                anteriorLinkedList = anteriorLinkedList.right
                siguienteLinkedList = siguienteLinkedList.right
                currentLinkedList = currentLinkedList.right
            # llamado recursivo para que siga el procedimiento con la siguiente fila
            self.cuadrarNodos(current.right, fila + 1)

    def contiene(self, valor):
        actual = self.head
        while actual:
            if actual.value == valor:
                return True
            actual = actual.right
        return False
