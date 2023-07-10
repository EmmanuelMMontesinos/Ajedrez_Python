import time
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

def marcar_mov(casilla, pieza):
    mov_correcto_paso = []
    mov_correcto_comer = []
    if pieza[0] == "p":
        if casilla[0] == 6:
            mov_posibles = []
            mov_posibles.append((casilla[0] - 1, casilla[1]))
            mov_posibles.append((casilla[0] - 2, casilla[1]))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] == "vacio.png":
                        mov_correcto_paso.append(mov)
            mov_posibles.append((casilla[0] - 1, casilla[1] - 1))
            mov_posibles.append((casilla[0] - 1, casilla[1] + 1))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        mov_correcto_comer.append(mov)
    return mov_correcto_paso, mov_correcto_comer

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
            for i in tablero:
                if op == i[0]:
                    n = (i[0], sprite)
                    nuevo_tablero2.append(n)
                else:
                    nuevo_tablero2.append(i)
            tablero = nuevo_tablero2
            nuevo_tablero = []
            ventana[op].update(image_filename=RUTA_PIEZAS_CLASICAS + sprite)

            ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
            actualizar_color_botones()
            pieza_seleccionada = None
            movimientos_posibles = []


    

ventana.close()