from Game import LinkedList, LinkedListVisual

class Game:
    def __ini__(self):
        pass

    def run(self):
        print("Bienvenido a Quoridor")
        columnas = input("de cuantas filas quiere que sea su tablero? : ")
        filas = input("de cuantas filas quiere que sea su tablero? : ")
        print("el que jugador que primero llegue a la ultima casilla gana!!")
        TableroLinkedList = LinkedList()
        TableroLinkedList.generarTablero(filas,columnas)
        TableroLinkedList.cuadrarNodos()
        TableroVisual = LinkedListVisual()
        TableroVisual.actualizarTablero(TableroLinkedList.head)
        while(True):
            TableroVisual.imprimirTablero()   
