from Game import LinkedList, LinkedListVisual

class Game:
    def __ini__(self):
        self.tablero = None

    def run(self):
        print("Bienvenido a Quoridor")
        filas = input("de cuantas filas quiere que sea su tablero? : ")
        columnas = input("de cuantas columnas quiere que sea su tablero? : ")
        print("el que jugador que primero llegue a la ultima casilla gana!!")
        tablero = Tablero()
        tablero.generarTablero(filas,columnas)
        self.tablero = tablero
        jugador = "player1"
        while(True):
            self.tablero.tableroVisual.imprimirTablero()
            opcion = input(f"{jugador} precione 1 para poner bloqueo y presione 2 para moverse")
            if opcion not in ["1","2"]:
                print("digite una opcion valida")
                continue
            elif opcion == "1":
                while(True):
                    fila = input("ingrese la fila donde quiere poner el bloqueo")
                    columna = input("ingrese la columna donde quiere poner el bloqueo")
                    if fila.isdigit() == False or columna.isdigit() == True:
                        print("caracteres invalidos...")
                        continue
                    elif fila >= self.tablero.filas: 
                        print("fila invalida")
                        continue
                    elif columna >= self.tablero.columnas:
                        print("columna invalida")
                        continue
            elif opcion == "2":
                while(True):
                    opcion = input("digite 1 para ir arriba, 2 para abajo, 3 para derecha y 4 para izquierda")
                    if opcion.isdigit() == False:
                        print("digito invalido...")
                    elif opcion not in ["1","2","3","4"]:
                        print("numero invalido solo entre 1 y 4 >:(")

                    elif opcion == "1":
                        movimiento = self.tablero.desplazarArriba(jugador)
                        if movimiento == True:
                            print(f"{jugador} GANADORRRRRRRR")
                            return
                        elif movimiento == False:
                            continue
                        else:
                            break
                    elif opcion == "2":
                        movimiento = self.tablero.desplazarAbajo(jugador)
                        if movimiento == True:
                            print(f"{jugador} GANADORRRRRRRR")
                            return
                        elif movimiento == False:
                            continue
                        else:
                            break
                    elif opcion == "3":
                        movimiento = self.tablero.desplazarDerecha(jugador)
                        if movimiento == False:
                            continue
                        else: 
                            break
                    elif opcion == "4":
                        movimiento = self.tablero.desplazarIzquierda(jugador)
                        if movimiento == False:
                            continue
                        else:
                            break
                if jugador == "player1":
                    jugador = "player2"
                else:
                    jugador = "player1"


                
            


class Tablero:

    def __init__(self):
        self.tablero = None
        self.tableroVisual = None

    def generarTablero(self, filas, columnas):
        tablero = LinkedList()
        tablero.generarTablero(int(filas),int(columnas))
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
        currentNode = currentLinkedList.value.head
        contfila = 0
        contcolumna = 0
        while(currentLinkedList):
            if columna == contcolumna:
                while(currentNode):
                    if contcolumna == columna:
                        return currentNode
                    currentNode = currentNode.right
                    contcolumna += 1
            currentLinkedList = currentLinkedList.right
            contfila += 1

    def desplazarArriba(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.up is None:
            if jugador == "player1":
                print("no te puedes mover a la nada")
                return False

        if nodoJugador.up is not None:
            if nodoJugador.up.value =="#":
                print("hay un bloqueo donde te quieres desplzar")
                return False
            if nodoJugador.up.value != None:
                print("no te puedes mover a la casilla en la que hay un jugador")
                return False
            if nodoJugador.up.up == None:
                return True
             
            nodoJugador.value = None
            nodoJugador.up.value = jugador
            self.tableroVisual.actualizarTablero(self.tablero.head)
        

    def desplazarAbajo(self, jugador):
        nodoJugador = self.getNodojugador(jugador)
        if nodoJugador.down is None:
            if jugador == "player2":
                return False
        if nodoJugador.down.value != None:
            return 
        if nodoJugador.down.down is None:
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
    


juego = Game()
juego.run()
    



            

