#clase la cual se encarga de guadar y representar visualmente nuestra lista enlazada graficmanete por medio de una matriz convencional de filas pero no interactua nada en la logica del juego
class LinkedListVisual:
    def __init__(self):
        self.matriz = None

    def actualizarTablero(self, head):
        self.matriz = []
        self.generarTableroVisual(head)

    #metodo 
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