from Tablero import Tablero

class Game:
    def __init__(self):
        self.tablero = None

    def menuTablero(self):
        print("Bienvenido a Quoridor")
        while True:
            filas = input("De cuantas filas quiere que sea su tablero? : ")
            columnas = input("De cuantas columnas quiere que sea su tablero? : ")
            if int(filas) >= 2 and int(columnas) >= 2:
                break
            print("El tamaño debe ser minimo de 2x2")
        print("¡El primer jugador que llegue a la última casilla gana!")
        tablero = Tablero()
        tablero.generarTablero(int(filas), int(columnas))
        self.tablero = tablero

    def run(self):
        self.menuTablero()
        jugador = "Player1"
        while True:
            self.tablero.tableroVisual.imprimirTablero()
            opcion = input(f"{jugador} Presione 1 para poner bloqueo y presione 2 para moverse: ")
            if opcion not in ["1", "2"]:
                print("Digite una opción valida")
                continue
            elif opcion == "1":
                if self.bloqueo() == False:
                    print("Bloqueo no puesto...")
                    continue
                print("Bloqueo puesto")
            elif opcion == "2":
                if self.mover(jugador) == True:
                    return
            jugador = self.setearJugador(jugador)

    def bloqueo(self):
        while (True):
            fila = input("Ingrese la fila donde quiere poner el bloqueo: ")
            columna = input("Ingrese la columna donde quiere poner el bloqueo: ")
            if fila.isdigit() == False or columna.isdigit() == False:
                print("Caracteres invalidos...")
                continue
            elif int(fila) > self.tablero.tablero.filas:
                print("Fila invalida")
                continue
            elif int(columna) > self.tablero.tablero.columnas:
                print("Columna invalida")
                continue
            bloqueo = self.tablero.bloqueo(int(fila), int(columna))
            self.tablero.tableroVisual.actualizarTablero(self.tablero.tablero.head)
            return bloqueo

    def mover(self, jugador):
        while (True):
            opcion = input("Digite 1 para ir arriba, 2 para abajo, 3 para derecha y 4 para izquierda: ")
            if opcion.isdigit() == False:
                print("Digito invalido...")
            elif opcion not in ["1", "2", "3", "4"]:
                print("Número invalido solo entre 1 y 4 >:(")
            elif opcion == "1":
                movimiento = self.tablero.desplazarArriba(jugador)
                if movimiento == True:
                    print(f"{jugador} GANADORRRRRRRR")
                    return True
                elif movimiento == False:
                    continue
                else:
                    break
            elif opcion == "2":
                movimiento = self.tablero.desplazarAbajo(jugador)
                if movimiento == True:
                    print(f"{jugador} GANADORRRRRRRR")
                    return True
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

    def setearJugador(self, jugador):
        if jugador == "Player1":
            return "Player2"
        else:
            return "Player1"
