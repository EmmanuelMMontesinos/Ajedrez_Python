import time
import tkinter as tk
import PySimpleGUI as sg
import ajedrez

BLANCO = '#F0D9B5'
NEGRO = '#B58863'
RUTA_PIEZAS_CLASICAS = "./Piezas/Piezas_Clasicas/"
POSICION_INICIAL = [(0, "t"), (1, "c"), (2, "a"), (3, "x"), (4, "y"), (5, "a"), (6, "c"), (7, "t"),
                    (8, "d"), (9, "d"), (10, "d"), (11, "d"), (12, "d"), (13, "d"), (14, "d"), (15, "d"),
                    (48, "P"), (49, "P"), (50, "P"), (51, "P"), (52, "P"), (53, "P"), (54, "P"), (55, "P"),
                    (56, "T"), (57, "C"), (58, "A"), (59, "X"), (60, "Y"), (61, "A"), (62, "C"), (63, "T")]

PIEZAS_JUGADOR = ["peon_blanco.png", "torre_blanca.png",
                "alfil_blanco.png", "caballo_blanco.png",
                "rey_blanco.png", "reina_blanca.png"]
PIEZAS_CPU = ["peon_negro.png", "torre_negra.png",
                "alfil_negro.png", "caballo_negro.png",
                "rey_negro.png", "reina_negra.png"]

checks_torres = {
    "torre1b" : (7,0),
    "torre2b" : (7,7),
    "torre1n" : (0,0),
    "torre2n" : (0,7)}
checks_enrroque = {
    "torre1b" : None, "torre2b" : None,
    "torre1n" : None, "torre2n" : None,
    "reyb" : None, "reyn" : None
}

def crear_tablero():
    layout = []
    tablero = []
    contador = 0
    for filas in range(8):
        fila_layout = []
        for columnas in range(8):
            color_casilla = BLANCO if (filas + columnas) % 2 == 0 else NEGRO
            pieza = " "
            for piez in POSICION_INICIAL:
                if piez[0] == contador:
                    pieza = piez[1]
            sprite = None
            if pieza != " ":
                if pieza == "t":
                    sprite = "torre_negra.png"
                elif pieza == "c":
                    sprite = "caballo_negro.png"
                elif pieza == "a":
                    sprite = "alfil_negro.png"
                elif pieza == "x":
                    sprite = "reina_negra.png"
                elif pieza == "y":
                    sprite = "rey_negro.png"
                elif pieza == "d":
                    sprite = "peon_negro.png"
                elif pieza == "T":
                    sprite = "torre_blanca.png"
                elif pieza == "C":
                    sprite = "caballo_blanco.png"
                elif pieza == "A":
                    sprite = "alfil_blanco.png"
                elif pieza == "X":
                    sprite = "reina_blanca.png"
                elif pieza == "Y":
                    sprite = "rey_blanco.png"
                elif pieza == "P":
                    sprite = "peon_blanco.png"
            if sprite != None:
                tablero.append(((filas, columnas), sprite))
                ruta = RUTA_PIEZAS_CLASICAS + sprite
                casilla = sg.Button("", button_color=color_casilla, key=(filas, columnas), pad=(1, 1), image_filename=ruta)
            else:
                tablero.append(((filas, columnas), "vacio.png"))
                ruta = RUTA_PIEZAS_CLASICAS + "vacio.png"
                casilla = sg.Button("", button_color=color_casilla, key=(filas, columnas), pad=(1, 1), image_filename=ruta)
                    
            fila_layout.append(casilla)
            contador += 1
        layout.append(fila_layout)
    return layout, tablero      

#Funcion para cambiar el peon
def cambiar_pieza():
    lista = []
    for p in PIEZAS_JUGADOR:
        lista.append(p[0:-4])
    cambio = [[sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "torre_blanca.png", key="-torre-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "caballo_blanco.png", key="-caballo-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "alfil_blanco.png", key="-alfil-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "reina_blanca.png", key="-reina-")]]
    emergente = sg.Window("Peon Coronado", cambio)
    eventos2, valores2 = emergente.read()
    if isinstance:
        emergente.close()
        if eventos2 == "-torre-":
            pi = "torre_blanca.png"
        elif eventos2 == "-caballo-":
            pi = "caballo_blanco.png"
        elif eventos2 == "-alfil-":
            pi = "alfil_blanco.png"
        elif eventos2 == "-reina-":
            pi = "reina_blanca.png"
        return pi

def enroque(pieza):
    if pieza == "rey_negro.png":
        if checks_enrroque["reyn"] == None or checks_enrroque["torre1n"] == None or checks_enrroque["torre2n"]:
            for pw in tablero:
                pwd = pw[0]
                if pwd == 0:
                    if pw[1] != "vacio.png":
                        return False
                    else:
                        pass
    if pieza == "rey_blanco.png":
        if checks_enrroque["reyb"] == None or checks_enrroque["torre1b"] == None or checks_enrroque["torre2b"]:
            for pw in tablero:
                pwd = pw[0]
                if pwd == 7:
                    if pw[1] != "vacio.png":
                        return False
                    else:
                        pass
        return True
                    


#Funcion que muestra los movimentos posibles
def marcar_mov(casilla, pieza):
    prueba = pieza[:3]
    mov_correcto_paso = []
    mov_correcto_comer = []
    mov_posibles = []
    if pieza[0] == "p":
        if casilla[0] == 6:
            mov_posibles.append((casilla[0] - 1, casilla[1]))
            check = False
            mov_posibles.append((casilla[0] - 2, casilla[1]))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        check = True
                    if mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                        check = True
                    if mov == piez[0] and piez[1] == "vacio.png" and check == False:
                        mov_correcto_paso.append(mov)
            mov_posibles = []
            mov_posibles.append((casilla[0] - 1, casilla[1] - 1))
            mov_posibles.append((casilla[0] - 1, casilla[1] + 1))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        mov_correcto_comer.append(mov)
            
        else:
            mov_posibles = []
            mov_posibles.append((casilla[0] - 1, casilla[1]))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] == "vacio.png":
                        mov_correcto_paso.append(mov)
            mov_posibles = []
            mov_posibles.append((casilla[0] - 1, casilla[1] - 1))
            mov_posibles.append((casilla[0] - 1, casilla[1] + 1))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        mov_correcto_comer.append(mov)
    elif pieza[0] == "c":
        mov_posibles = []
        mov_posibles.append((casilla[0] - 1, casilla[1] - 2))
        mov_posibles.append((casilla[0] - 2, casilla[1] - 1))
        mov_posibles.append((casilla[0] + 1, casilla[1] + 2))
        mov_posibles.append((casilla[0] + 2, casilla[1] + 1))
        mov_posibles.append((casilla[0] + 1, casilla[1] - 2))
        mov_posibles.append((casilla[0] + 2, casilla[1] - 1))
        mov_posibles.append((casilla[0] - 1, casilla[1] + 2))
        mov_posibles.append((casilla[0] - 2, casilla[1] + 1))
        for mov in mov_posibles:
            for piez in tablero:
                if mov == piez[0] and piez[1] == "vacio.png":
                    mov_correcto_paso.append(mov)
        for mov in mov_posibles:
            for piez in tablero:
                if mov == piez[0] and piez[1] in PIEZAS_CPU:
                    mov_correcto_comer.append(mov)
    elif pieza[0] == "t":
        checks = {"check_arriba" : False,
            "check_abajo" : False,
            "check_derecha" : False,
            "check_izquierda" : False
            }
        for n in range(8):
            jugada = (casilla[0] + (n + 1), casilla[1])
            jugada2 = (casilla[0] - (n + 1), casilla[1])
            jugada3 = (casilla[0], casilla[1] + (n + 1))
            jugada5 = (casilla[0], casilla[1] - (n + 1))
            for cosas in tablero:
                if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                    mov_correcto_paso.append(jugada)
                elif jugada == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_derecha"] = True
                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_izquierda"] = True
                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_arriba"] = True
                if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada5)
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada5)
                    checks["check_abajo"] = True
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_abajo"] = True
    elif pieza[0] == "a":
        checks = {"check_arriba" : False,
            "check_abajo" : False,
            "check_derecha" : False,
            "check_izquierda" : False
            }
        for n in range(8):
            jugada = (casilla[0] + (n + 1), casilla[1] + (n + 1))
            jugada2 = (casilla[0] - (n + 1), casilla[1] - (n + 1))
            jugada3 = (casilla[0] - (n + 1), casilla[1] + (n + 1))
            jugada5 = (casilla[0] + (n + 1), casilla[1] - (n + 1))
            for cosas in tablero:
                if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                    mov_correcto_paso.append(jugada)
                elif jugada == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_derecha"] = True
                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_izquierda"] = True
                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_arriba"] = True
                if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada5)
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada5)
                    checks["check_abajo"] = True
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_abajo"] = True
    elif pieza[:3] == "rei":
        checks = {"check_arriba" : False,
            "check_abajo" : False,
            "check_derecha" : False,
            "check_izquierda" : False,
            "check_arriba_derecha" : False,
            "check_arriba_izquierda" : False,
            "check_abajo_derecha" : False,
            "check_abajo_izquierda" : False
            }
        for n in range(8):
            jugada = (casilla[0] + (n + 1), casilla[1] + (n + 1))
            jugada2 = (casilla[0] - (n + 1), casilla[1] - (n + 1))
            jugada3 = (casilla[0] - (n + 1), casilla[1] + (n + 1))
            jugada4 = (casilla[0] + (n + 1), casilla[1] - (n + 1))
            jugada5 = (casilla[0] + (n + 1), casilla[1])
            jugada6 = (casilla[0], casilla[1] + (n + 1))
            jugada7 = (casilla[0] - (n + 1), casilla[1])
            jugada8 = (casilla[0], casilla[1] - (n + 1))
            for cosas in tablero:
                if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                    mov_correcto_paso.append(jugada)
                elif jugada == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_derecha"] = True

                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_izquierda"] = True

                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_arriba"] = True

                if jugada4 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada4)
                elif jugada4 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada4)
                    checks["check_abajo"] = True
                elif jugada4 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_abajo"] = True

                if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_derecha"] != True:
                    mov_correcto_paso.append(jugada5)
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba_derecha"] != True:
                    mov_correcto_comer.append(jugada5)
                    checks["check_arriba_derecha"] = True
                elif jugada5 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_arriba_derecha"] = True

                if jugada6 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_izquierda"] != True:
                    mov_correcto_paso.append(jugada6)
                elif jugada6 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba_izquierda"] != True:
                    mov_correcto_comer.append(jugada6)
                    checks["check_arriba_izquierda"] = True
                elif jugada6 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_arriba_izquierda"] = True

                if jugada7 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_derecha"] != True:
                    mov_correcto_paso.append(jugada7)
                elif jugada7 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo_derecha"] != True:
                    mov_correcto_comer.append(jugada7)
                    checks["check_abajo_derecha"] = True
                elif jugada7 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_abajo_derecha"] = True

                if jugada8 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_izquierda"] != True:
                    mov_correcto_paso.append(jugada8)
                elif jugada8 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo_izquierda"] != True:
                    mov_correcto_comer.append(jugada8)
                    checks["check_abajo_izquierda"] = True
                elif jugada8 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                    checks["check_abajo_izquierda"] = True
    elif pieza[:3] =="rey":
        checks = {"check_arriba" : False,
            "check_abajo" : False,
            "check_derecha" : False,
            "check_izquierda" : False,
            "check_arriba_derecha" : False,
            "check_arriba_izquierda" : False,
            "check_abajo_derecha" : False,
            "check_abajo_izquierda" : False
            }
        jugada = (casilla[0] + 1, casilla[1] + 1)
        jugada2 = (casilla[0] - 1, casilla[1] - 1)
        jugada3 = (casilla[0] - 1, casilla[1] + 1)
        jugada4 = (casilla[0] + 1, casilla[1] - 1)
        jugada5 = (casilla[0] + 1, casilla[1])
        jugada6 = (casilla[0], casilla[1] + 1)
        jugada7 = (casilla[0] - 1, casilla[1])
        jugada8 = (casilla[0], casilla[1] - 1)
        for cosas in tablero:
            if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                mov_correcto_paso.append(jugada)
            elif jugada == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_derecha"] != True:
                mov_correcto_comer.append(jugada)
                checks["check_derecha"] = True
            elif jugada == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_derecha"] = True

            if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                mov_correcto_paso.append(jugada2)
            elif jugada2 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_izquierda"] != True:
                mov_correcto_comer.append(jugada2)
                checks["check_izquierda"] = True
            elif jugada2 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_izquierda"] = True

            if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                mov_correcto_paso.append(jugada3)
            elif jugada3 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba"] != True:
                mov_correcto_comer.append(jugada3)
                checks["check_arriba"] = True
            elif jugada3 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_arriba"] = True

            if jugada4 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                mov_correcto_paso.append(jugada4)
            elif jugada4 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo"] != True:
                mov_correcto_comer.append(jugada4)
                checks["check_abajo"] = True
            elif jugada4 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_abajo"] = True

            if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_derecha"] != True:
                mov_correcto_paso.append(jugada5)
            elif jugada5 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba_derecha"] != True:
                mov_correcto_comer.append(jugada5)
                checks["check_arriba_derecha"] = True
            elif jugada5 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_arriba_derecha"] = True

            if jugada6 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_izquierda"] != True:
                mov_correcto_paso.append(jugada6)
            elif jugada6 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_arriba_izquierda"] != True:
                mov_correcto_comer.append(jugada6)
                checks["check_arriba_izquierda"] = True
            elif jugada6 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_arriba_izquierda"] = True

            if jugada7 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_derecha"] != True:
                mov_correcto_paso.append(jugada7)
            elif jugada7 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo_derecha"] != True:
                mov_correcto_comer.append(jugada7)
                checks["check_abajo_derecha"] = True
            elif jugada7 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_abajo_derecha"] = True

            if jugada8 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_izquierda"] != True:
                mov_correcto_paso.append(jugada8)
            elif jugada8 == cosas[0] and cosas[1] in PIEZAS_CPU and checks["check_abajo_izquierda"] != True:
                mov_correcto_comer.append(jugada8)
                checks["check_abajo_izquierda"] = True
            elif jugada8 == cosas[0] and cosas[1] in PIEZAS_JUGADOR:
                checks["check_abajo_izquierda"] = True

    return mov_correcto_paso, mov_correcto_comer
#funcion para volver el tablero sin marcas de movimientos posibles
def actualizar_color_botones():
    for mov in movimientos_posibles:
        color_casilla = BLANCO if (mov[0] + mov[1]) % 2 == 0 else NEGRO
        ventana[mov].update(button_color=("", color_casilla))
mesa, tablero = crear_tablero()
ventana = sg.Window("Ajedrez-Bot by Morzan", mesa, resizable=True)

pieza_seleccionada = None
movimientos_posibles = []

while True:
    eventos, valores = ventana.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif isinstance(eventos, tuple):
        fila, columna = eventos
        op = (fila, columna)
        casilla = ventana[op]
        if op not in movimientos_posibles:
            actualizar_color_botones()
            movimientos_posibles = []
            pieza_seleccionada = None
        if not pieza_seleccionada:
            for ele in tablero:
                if eventos == ele[0]:
                    if ele[1] != "vacio.png":
                        if ele[1] in PIEZAS_JUGADOR:
                            mov_paso, mov_comer = marcar_mov(eventos, ele[1])
                            
                            for mov in mov_paso:
                                ventana[mov].update(button_color=("","green"))
                                movimientos_posibles.append(mov)
                            for mov in mov_comer:
                                ventana[mov].update(button_color=("", "red"))
                                movimientos_posibles.append(mov)
                            pieza_seleccionada = op
        elif pieza_seleccionada:
            nuevo_tablero = []
            for i in tablero:
                if pieza_seleccionada == i[0]:
                    sprite = i[1]
                    nv = (i[0], "vacio.png")
                    nuevo_tablero.append(nv)
                else:
                    nuevo_tablero.append(i)
            tablero = nuevo_tablero
            nuevo_tablero2 = []
            if op[0] == 0 and sprite[0] == "p":
                sprite = cambiar_pieza()
                ventana[op].update(image_filename=RUTA_PIEZAS_CLASICAS + sprite)
                ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                actualizar_color_botones()
                
                movimientos_posibles = []
            

            else:
                ventana[op].update(image_filename=RUTA_PIEZAS_CLASICAS + sprite)
                ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                actualizar_color_botones()
                
                movimientos_posibles = []
            for i in tablero:
                if op == i[0]:
                    n = (i[0], sprite)
                    nuevo_tablero2.append(n)
                else:
                    nuevo_tablero2.append(i)
            for tab in tablero:
                if tab[0] == n[0]:
                    if n[1] == "torre_blanca.png" or n[1] == "torre_negra.png" or n[1] == "rey_blanco.png" or n[1] == "rey_negro.png":
                        for item in checks_torres.keys():
                            if checks_torres[item] == pieza_seleccionada:
                                checks_enrroque[item] = False
            tablero = nuevo_tablero2
            nuevo_tablero = []
            pieza_seleccionada = None


    

ventana.close()