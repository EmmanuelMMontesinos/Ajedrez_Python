import os

TABLERO = {
    "a1": "t", "b1": "c", "c1": "a", "d1": "x", "e1": "y", "f1": "a", "g1": "c", "h1": "t",
    "a2": "d", "b2": "d", "c2": "d", "d2": "d", "e2": "d", "f2": "d", "g2": "d", "h2": "d",
    "a3": " ", "b3": " ", "c3": " ", "d3": " ", "e3": " ", "f3": " ", "g3": " ", "h3": " ",
    "a4": " ", "b4": " ", "c4": " ", "d4": " ", "e4": " ", "f4": " ", "g4": " ", "h4": " ",
    "a5": " ", "b5": " ", "c5": " ", "d5": " ", "e5": " ", "f5": " ", "g5": " ", "h5": " ",
    "a6": " ", "b6": " ", "c6": " ", "d6": " ", "e6": " ", "f6": " ", "g6": " ", "h6": " ",
    "a7": "P", "b7": "P", "c7": "P", "d7": "P", "e7": "P", "f7": "P", "g7": "P", "h7": "P",
    "a8": "T", "b8": "C", "c8": "A", "d8": "X", "e8": "Y", "f8": "A", "g8": "C", "h8": "T"}
Jugador = []
Cpu = []
COLUMNAS = ["A", "B", "C", "D", "E", "F", "G", "H"]
FILAS = ["1", "2", "3", "4", "5", "6", "7", "8"]
PEON = "P"
TORRE = "T"
CABALLO = "C"
ALFIL = "A"
REINA = "X"
REY = "Y"


def generar_piezas():
    for n in range(8):
        Jugador.append(PEON)
        Cpu.append(PEON)
    for n in range(2):
        Jugador.append(TORRE)
        Cpu.append(TORRE)
    for n in range(2):
        Jugador.append(CABALLO)
        Cpu.append(CABALLO)
    for n in range(2):
        Jugador.append(ALFIL)
        Cpu.append(ALFIL)
    Jugador.append(REINA)
    Jugador.append(REY)
    Cpu.append(REINA)
    Cpu.append(REY)


def limpiar_Pantalla():
    try:
        os.system("cls")
    except OSError:
        os.system("clear")


def casilla_libre(mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero):
    colum_inicio = mov_prev[0]
    colum_final = mov_prox[0]
    fila_inicio = mov_prev[1]
    fila_final = mov_prox[1]
    fila_inicio = int(fila_inicio)
    fila_final = int(fila_final)
    check = True
    if colum_inicio == colum_final and fila_inicio != fila_final:
        paso = 0
        camino = fila_inicio - fila_final
        for n in range(fila_final, fila_inicio):
            indice = colum_final + str(n)
            if check == False:
                return False
            elif tablero[indice] in piezas_cpu or tablero[indice] in piezas_jugador:
                if indice == mov_prox:
                    if check == True:
                        return True
                    else:
                        return False
                else:
                    return False
            if tablero[indice] == " ":
                check = True
            else:
                return False
        if check == True:
            return True
        else:
            return False
    elif colum_inicio != colum_final and fila_inicio == fila_final:
        paso = 0
        camino = fila_inicio - fila_final
        for n in range(fila_final, fila_inicio):
            indice = colum_final + str(n)
            if check == False:
                return False
            elif tablero[indice] in piezas_cpu or tablero[indice] in piezas_jugador:
                if indice == mov_prox:
                    if check == True:
                        return True
                    else:
                        return False
                else:
                    return False
            if tablero[indice] == " ":
                check = True
            else:
                return False
        if check == True:
            return True
        else:
            return False
    elif colum_inicio != colum_final and fila_inicio != fila_final:
        if pieza.upper() == "C":
            guia = {"a": 1, "b": 2, "c": 3, "d": 4,
                    "e": 5, "f": 6, "g": 7, "h": 8}
            if guia[colum_inicio] - guia[colum_final] == 1 and fila_inicio - fila_final == 2:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == 2 and fila_inicio - fila_final == 1:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == -1 and fila_inicio - fila_final == 2:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] == " ":
                    return True
            elif guia[colum_inicio] - guia[colum_final] == -2 and fila_inicio - fila_final == 1:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == 1 and fila_inicio - fila_final == -2:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == 2 and fila_inicio - fila_final == -1:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == -1 and fila_inicio - fila_final == -2:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
            elif guia[colum_inicio] - guia[colum_final] == -2 and fila_inicio - fila_final == -1:
                if tablero[mov_prox] in piezas_cpu and pieza in piezas_jugador:
                    if check == True:
                        return True
                    else:
                        return False
                elif tablero[mov_prox] in piezas_jugador and pieza in piezas_cpu:
                    if check == True:
                        return True
                    else:
                        return False
        paso = 0
        camino = fila_inicio - fila_final
        for n in range(fila_final, fila_inicio):
            indice = colum_final + str(n)
            if check == False:
                return False
            elif tablero[indice] in piezas_cpu or tablero[indice] in piezas_jugador:
                if indice == mov_prox:
                    if tablero[indice] in piezas_cpu and pieza in piezas_jugador:
                        if check == True:
                            return True
                        else:
                            return False
                    elif tablero[indice] in piezas_jugador and pieza in piezas_cpu:
                        if check == True:
                            return True
                        else:
                            return False
                else:
                    return False
            if tablero[indice] == " ":
                check = True
            else:
                return False
        if check == True:
            return True
        else:
            return False
    return False


def movimientos_permitidos(pieza, mov_prev, mov_prox, tablero):
    piezas_cpu = ["a", "c", "d", "t", "x", "y"]
    piezas_jugador = ["A", "C", "P", "T", "X", "Y"]
    try:
        if pieza == "P":
            if tablero[mov_prox] == " " or tablero[mov_prox] in piezas_cpu:
                # Si el movimiento es no es para comer
                if mov_prev[0] == mov_prox[0]:
                    if "7" == mov_prev[1] and int(mov_prev[1]) - int(mov_prox[1]) == 2:
                        return True
                    elif "7" == mov_prev[1] and int(mov_prev[1]) - int(mov_prox[1]) == 1:
                        return True
                    elif "7" != mov_prev[1] and int(mov_prev[1]) - int(mov_prox[1]) == 1:
                        if tablero[mov_prox] == " " or tablero[mov_prox] == " ":
                            return True
                # Si el movimento es para comer
                elif mov_prev[1] != mov_prox[1]:
                    contador = 0
                    prev = 0
                    prox = 0
                    for colum in COLUMNAS:
                        if mov_prev[0] == colum.lower():
                            prev = contador
                        elif mov_prox[0] == colum.lower():
                            prox = contador
                        contador += 1
                    if prev + 1 == prox or prev - 1 == prox and mov_prev[1] != mov_prox[1]:
                        return True
                    else:
                        return False
        elif pieza == "T":
            if tablero[mov_prox] == " ":
                if mov_prev[0] == mov_prox[0] and mov_prev[1] != mov_prox[1]:
                    permiso = casilla_libre(
                        mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                    return permiso
                elif mov_prev[0] != mov_prox[0] and mov_prev[1] == mov_prox[1]:
                    permiso = casilla_libre(
                        mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                    return permiso
            for piez in piezas_cpu:
                if tablero[mov_prox] == piez:
                    if mov_prev[0] == mov_prox[0] and mov_prev[1] != mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso
                    elif mov_prev[0] != mov_prox[0] and mov_prev[1] == mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso
        elif pieza == "A":
            if tablero[mov_prox] == " ":
                if mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                    permiso = casilla_libre(
                        mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                    return permiso
                else:
                    return False
            for piez in piezas_cpu:
                if tablero[mov_prox] == piez:
                    if mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso
                    elif mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso
        elif pieza == "C":
            if tablero[mov_prox] == " ":
                if mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                    permiso = casilla_libre(
                        mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                    return permiso
                else:
                    return False
            for piez in piezas_cpu:
                if tablero[mov_prox] == piez:
                    if mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso
                    elif mov_prev[0] != mov_prox[0] and mov_prev[1] != mov_prox[1]:
                        permiso = casilla_libre(
                            mov_prev, mov_prox, pieza, piezas_cpu, piezas_jugador, tablero)
                        return permiso

    except:
        limpiar_Pantalla()
        print(f"{pieza}{mov_prev}/{mov_prox} no es un movimiento correcto")
    return False


def movimiento(tablero):
    pantalla(tablero)
    print("P=Peon, T=Torre, C=Caballo, X=Reina, Y=Rey")
    print("Para hacer jugada escriba primero la posicion de la pieza y separado por /, donde se mueve")
    print("EJ: PE7/E5")
    mov = input("")
    if len(mov) == 6:
        mov = mov.lower()
        mov_anterior, prox_mov = mov.split("/")
        pieza = mov_anterior[0].upper()
        mov_anterior = mov_anterior[1:]
        mov_permitido = movimientos_permitidos(
            pieza, mov_anterior, prox_mov, tablero)
        if mov_permitido == True:
            tablero[mov_anterior] = " "
            tablero[prox_mov] = pieza
            return tablero
        elif mov_permitido == False:
            limpiar_Pantalla()
            print(f"{mov.upper()} no es un movimento permitido")
            input("Pulse Enter para volver a la partida")
            return tablero
    else:
        limpiar_Pantalla()
        print(f"{mov} no es un movimiento valido\nEnter para continuar")
        input("")
        return tablero
# def movimiento_cpu(tablero):


def pantalla(tablero):
    limpiar_Pantalla()
    contador = 1
    con_columna = 1
    fila = "-A-B-C-D-E-F-G-H-"
    print(fila)
    for item in tablero.items():
        print("|", end="")
        if contador == 8 and item[1] != " ":
            print(f"{item[1]}|{con_columna}\n", end="")
            con_columna += 1
            contador = 1
        elif item[1] != " ":
            print(f"{item[1]}", end="")
            contador += 1
        elif contador == 8 and item[1] == " ":
            print(f" |{con_columna}\n", end="")
            contador = 1
            con_columna += 1
        elif item[1] == " " and contador < 8:
            print(" ", end="")
            contador += 1

    print(fila)


def main():
    tablero_de_juego = TABLERO
    game = True
    while game:
        tablero_de_juego = movimiento(tablero_de_juego)

        # tablero_de_juego = movimiento_cpu(tablero_de_juego)


if __name__ == "__main__":
    main()
