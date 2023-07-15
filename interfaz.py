import time
import tkinter as tk
import PySimpleGUI as sg
from random import choice
import ajedrez
import marcador
import cpu

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
    "torre1b" : (7,2),
    "torre2b" : (7,6),
    "torre1n" : (0,2),
    "torre2n" : (0,6)}
checks_enrroque = {
    "torre1b" : None, "torre2b" : None,
    "torre1n" : None, "torre2n" : None,
    "reyb" : None, "reyn" : None}
blancas = marcador.marcador_blanco.copy()
negras = marcador.marcador_negro.copy()
marcador_blanco = blancas["partida_ganada"]
marcador_negro = negras["partida_ganada"]


movimiento_enrroque = []
mov_final_enrroque = []
ultima_casilla = "Movimiento Inicial"

#actualiza cementerio de interfaz
def calculo_piezas(op):
    reyn = 1
    reyb = 1
    reinan = 1
    reinab = 1
    alfiln = 2
    alfilb = 2
    caban = 2
    cabab = 2
    torren = 2
    torreb = 2
    peonn = 8
    peonb = 8
    for tab in tablero:
        if tab[1] == "rey_negro.png":
            reyn -= 1
        if tab[1] == "rey_blanco.png":
            reyb -= 1
        if tab[1] == "reina_negra.png":
            reinan -= 1
        if tab[1] == "reina_blanca.png":
            reinab -= 1
        if tab[1] == "alfil_negro.png":
            alfiln -= 1
        if tab[1] == "alfil_blanco.png":
            alfilb -= 1
        if tab[1] == "caballo_negro.png":
            caban -= 1
        if tab[1] == "caballo_blanco.png":
            cabab -= 1
        if tab[1] == "torre_negra.png":
            torren -= 1
        if tab[1] == "torre_blanca.png":
            torreb -= 1
        if tab[1] == "peon_negro.png":
            peonn -= 1
        if tab[1] == "peon_blanco.png":
            peonb -= 1
    resultado = ((reyn , "rey_negro.ficha"),
                    (reyb , "rey_blanco.ficha"),
                    (reinan , "reina_negra.ficha"),
                    (reinab , "reina_blanca.ficha"),
                    (alfiln , "alfil_negro.ficha"),
                    (alfilb , "alfil_blanco.ficha"),
                    (caban , "caballo_negro.ficha"),
                    (cabab , "caballo_blanco.ficha"),
                    (torren , "torre_negra.ficha"),
                    (torreb , "torre_blanca.ficha"),
                    (peonn , "peon_negro.ficha"),
                    (peonb , "peon_blanco.ficha"))
    return resultado


#reinicia el tablero
def rendirse():
    global blancas
    global negras
    global ultima_casilla
    mesa, tablero2 = crear_tablero()
    for i in tablero2:
        ventana[i[0]].update("", image_filename=RUTA_PIEZAS_CLASICAS + i[1])
    tablero = tablero2
    blancas = marcador.marcador_blanco.copy()
    negras = marcador.marcador_negro.copy()
    
    nuevo_tablero = []
    for i in blancas.keys():
        piezza = i
        pieza = piezza[-9:-4]
        i_correcta1 = piezza
        i_correcta = i_correcta1 + ".ficha" 
        if i != "partida_ganada":
            result1 = blancas[i]
            result2 = marcador.marcador_blanco[i]
            result = result1 - result2
            
            result3 = str(result)
            ventana[i_correcta].update(result3)
    for n in negras.keys():
        piezza = i
        pieza = piezza[-9:-4]
        i_correcta1 = piezza[:-4]
        i_correcta = i_correcta1 + ".ficha"
        if n != "partida_ganada":
            i_correcta = n + ".ficha"
            if piezza[:-4] == n:
                negras[n] -= 1
            result1 = negras[n]
            result2 = marcador.marcador_negro2[n]
            result = result2 - result1
            result3 = str(result)
            
            ventana[i_correcta].update(result3)
            
        
    return tablero, mesa
#crea el tablero por defecto
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
    fila_layout = []
    for i in blancas:
        if i != "partida_ganada":
            boton = sg.Button(button_text="", image_size=(26, 48),pad=1, image_filename=RUTA_PIEZAS_CLASICAS + i + ".png", key=i + ".png")
            marca = sg.Text("0",  key=i + ".ficha")
            fila_layout.append(boton)
            fila_layout.append(marca)
    layout.append(fila_layout)
    fila_layout = []
    for i in negras.keys():
        if i != "partida_ganada":
            result1 = negras[i]
            result2 = marcador.marcador_negro[i]
            result = result1 - result2
            boton = sg.Button(button_text="", image_size=(26, 48), pad=1, image_filename=RUTA_PIEZAS_CLASICAS + i + ".png", key=i + ".png")
            marca = sg.Text(f"{result}", key=i + ".ficha")
            fila_layout.append(boton)
            fila_layout.append(marca)
    layout.append(fila_layout)
    fila_layout = []
    
    marcador_bla = sg.Text(f"Blancas:{int(marcador_blanco)}", pad=0)
    marcador_ne = sg.Text(f"Negras:{int(marcador_negro)}", pad=0)
    info_jugada = sg.Text(f"Ultimo movimiento:\n{ultima_casilla}", key="-info-", pad=0)
    nivel_cpu = sg.Button("Dificuldad", key="-nivel-", size=(10, None), pad=0)
    rendirse = sg.Button("Reiniciar", key="-reiniciar-", size=(10, None), pad=0)
    fila_layout.append(nivel_cpu)
    fila_layout.append(marcador_bla)
    fila_layout.append(info_jugada)
    fila_layout.append(marcador_ne)
    fila_layout.append(rendirse)
    layout.append(fila_layout)
    return layout, tablero      

#Coronar peones
def cambiar_pieza(op):
    lista = []
    for p in PIEZAS_JUGADOR:
        lista.append(p[0:-4])
    cambio = [[sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "torre_blanca.png", key="-torre-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "caballo_blanco.png", key="-caballo-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "alfil_blanco.png", key="-alfil-"),
        sg.Button("", image_filename=RUTA_PIEZAS_CLASICAS + "reina_blanca.png", key="-reina-")]]
    emergente = sg.Window("Coronado", cambio, icon="icono.ico")
    eventos2, valores2 = emergente.read()
    if isinstance:
        if eventos2 == "-torre-":
            pi = "torre_blanca.png"
        elif eventos2 == "-caballo-":
            pi = "caballo_blanco.png"
        elif eventos2 == "-alfil-":
            pi = "alfil_blanco.png"
        elif eventos2 == "-reina-":
            pi = "reina_blanca.png"
        emergente.close()
        
        return pi
#detecta y ejecuta el enrroque del rey
def enroque(pieza):
    check_1 = True
    check_2 = True
    if pieza == "rey_negro.png":
        for tab in tablero:
            if tab == ((0, 3), "reina_negra.png"):
                check_2 = False
            if ((0, 1), "caballo_blanco.png") == tab:
                check_2 = False
            if tab == ((0, 2), "alfil_blanco.png"):
                check_2 = False
            if tab == ((0, 5), "alfil_blanco.png"):
                check_1 = False
            if tab == ((0, 6), "caballo_blanco.png"):
                check_1 = False
        return check_1, check_2
    if pieza == "rey_blanco.png":
        for tab in tablero:
            if tab == ((7, 3), "reina_blanca.png"):
                check_1 = True#derecha
                check_2 = False
            if ((7, 1), "caballo_blanco.png") == tab:
                check_1 = True
                check_2 = False
            if tab == ((7, 2), "alfil_blanco.png"):
                check_1 = True
                check_2 = False
            if tab == ((7, 5), "alfil_blanco.png"):
                check_1 = False
                check_2 = True
            if tab == ((7, 6), "caballo_blanco.png"):
                check_1 = False
                check_2 = True
        return check_1, check_2

                    
def jaque(pos_rey, bando_rey, mov_correcto_paso):
    if bando_rey == "blancas":
        bando = PIEZAS_JUGADOR
    else:
        bando = PIEZAS_CPU
    for tab in tablero:
        if tab[1] in bando:
            mov_paso, mov_comer, mov_defensa, mov_enrroque = marcar_mov(tab[0], tab[1])
            if pos_rey in mov_comer:
                return True
    else:
        return False


#muestra los movimentos posibles
def marcar_mov(casilla, pieza):
    prueba = pieza
    if pieza in PIEZAS_JUGADOR:
        atacante = PIEZAS_JUGADOR
        defensor = PIEZAS_CPU
    else:
        atacante = PIEZAS_CPU
        defensor = PIEZAS_JUGADOR
    mov_correcto_paso = []
    mov_correcto_comer = []
    mov_defensa = []
    mov_enrroque = []
    mov_posibles = []
    mov_enrroque_final = []
    mov_enrroque_decidido = []
    if pieza[0] == "p":
        if casilla[0] == 6:
            mov_posibles.append((casilla[0] - 1, casilla[1]))
            check = False
            mov_posibles.append((casilla[0] - 2, casilla[1]))
            for mov in mov_posibles:
                for piez in tablero:
                    if prueba in PIEZAS_JUGADOR:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            check = True
                            mov_correcto_comer.append(mov)
                        if mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                            check = True
                            mov_defensa.append(mov)
                        if mov == piez[0] and piez[1] == "vacio.png" and check == False:
                            mov_correcto_paso.append(mov)
                    else:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            check = True
                            mov_defensa.append(mov)
                        if mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                            check = True
                            mov_correcto_comer.append(mov)
                        if mov == piez[0] and piez[1] == "vacio.png" and check == False:
                            mov_correcto_paso.append(mov)
            mov_posibles = []
            mov_posibles.append((casilla[0] - 1, casilla[1] - 1))
            mov_posibles.append((casilla[0] - 1, casilla[1] + 1))
            for mov in mov_posibles:
                for piez in tablero:
                    if prueba in PIEZAS_JUGADOR:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            mov_correcto_comer.append(mov)
                        elif mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                            mov_defensa.append(mov)
                    else:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            mov_defensa.append(mov)
                        elif mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
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
                    if prueba in PIEZAS_JUGADOR:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            mov_correcto_comer.append(mov)
                        elif mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                            mov_defensa.append(mov)
                    else:
                        if mov == piez[0] and piez[1] in PIEZAS_CPU:
                            mov_defensa.append(mov)
                        elif mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
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
                if prueba in PIEZAS_JUGADOR:
                    if mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
                        mov_defensa.append(mov)
                else:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        mov_defensa.append(mov)
        for mov in mov_posibles:
            for piez in tablero:
                if prueba in PIEZAS_JUGADOR:
                    if mov == piez[0] and piez[1] in PIEZAS_CPU:
                        mov_correcto_comer.append(mov)
                else:
                    if mov == piez[0] and piez[1] in PIEZAS_JUGADOR:
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
            jugada4 = (casilla[0], casilla[1] - (n + 1))
            for cosas in tablero:
                if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                    mov_correcto_paso.append(jugada)
                elif jugada == cosas[0] and cosas[1] in defensor and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in atacante and checks["check_derecha"] != True:
                    mov_defensa.append(jugada)
                    checks["check_derecha"] = True
                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in defensor and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in atacante and checks["check_izquierda"] != True:
                    mov_defensa.append(jugada2)
                    checks["check_izquierda"] = True
                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in defensor and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in atacante and checks["check_arriba"] != True:
                    mov_defensa.append(jugada3)
                    checks["check_arriba"] = True
                if jugada4 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada4)
                elif jugada4 == cosas[0] and cosas[1] in defensor and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada4)
                    checks["check_abajo"] = True
                elif jugada4 == cosas[0] and cosas[1] in atacante and checks["check_abajo"] != True:
                    mov_defensa.append(jugada4)
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
                elif jugada == cosas[0] and cosas[1] in defensor and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in atacante and checks["check_derecha"] != True:
                    mov_defensa.append(jugada)
                    checks["check_derecha"] = True
                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in defensor and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in atacante and checks["check_izquierda"] != True:
                    mov_defensa.append(jugada2)
                    checks["check_izquierda"] = True
                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in defensor and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in atacante and checks["check_arriba"] != True:
                    mov_defensa.append(jugada3)
                    checks["check_arriba"] = True
                if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada5)
                elif jugada5 == cosas[0] and cosas[1] in defensor and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada5)
                    checks["check_abajo"] = True
                elif jugada5 == cosas[0] and cosas[1] in atacante and checks["check_abajo"] != True:
                    mov_defensa.append(jugada5)
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
                elif jugada == cosas[0] and cosas[1] in defensor and checks["check_derecha"] != True:
                    mov_correcto_comer.append(jugada)
                    checks["check_derecha"] = True
                elif jugada == cosas[0] and cosas[1] in atacante and checks["check_derecha"] != True:
                    mov_defensa.append(jugada)
                    checks["check_derecha"] = True

                if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                    mov_correcto_paso.append(jugada2)
                elif jugada2 == cosas[0] and cosas[1] in defensor and checks["check_izquierda"] != True:
                    mov_correcto_comer.append(jugada2)
                    checks["check_izquierda"] = True
                elif jugada2 == cosas[0] and cosas[1] in atacante and checks["check_izquierda"] != True:
                    mov_defensa.append(jugada2)
                    checks["check_izquierda"] = True

                if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                    mov_correcto_paso.append(jugada3)
                elif jugada3 == cosas[0] and cosas[1] in defensor and checks["check_arriba"] != True:
                    mov_correcto_comer.append(jugada3)
                    checks["check_arriba"] = True
                elif jugada3 == cosas[0] and cosas[1] in atacante and checks["check_arriba"] != True:
                    mov_defensa.append(jugada3)
                    checks["check_arriba"] = True

                if jugada4 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                    mov_correcto_paso.append(jugada4)
                elif jugada4 == cosas[0] and cosas[1] in defensor and checks["check_abajo"] != True:
                    mov_correcto_comer.append(jugada4)
                    checks["check_abajo"] = True
                elif jugada4 == cosas[0] and cosas[1] in atacante and checks["check_abajo"] != True:
                    mov_defensa.append(jugada4)
                    checks["check_abajo"] = True

                if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_derecha"] != True:
                    mov_correcto_paso.append(jugada5)
                elif jugada5 == cosas[0] and cosas[1] in defensor and checks["check_arriba_derecha"] != True:
                    mov_correcto_comer.append(jugada5)
                    checks["check_arriba_derecha"] = True
                elif jugada5 == cosas[0] and cosas[1] in atacante and checks["check_arriba_derecha"] != True:
                    mov_defensa.append(jugada5)
                    checks["check_arriba_derecha"] = True

                if jugada6 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_izquierda"] != True:
                    mov_correcto_paso.append(jugada6)
                elif jugada6 == cosas[0] and cosas[1] in defensor and checks["check_arriba_izquierda"] != True:
                    mov_correcto_comer.append(jugada6)
                    checks["check_arriba_izquierda"] = True
                elif jugada6 == cosas[0] and cosas[1] in atacante and checks["check_arriba_izquierda"] != True:
                    mov_defensa.append(jugada6)
                    checks["check_arriba_izquierda"] = True

                if jugada7 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_derecha"] != True:
                    mov_correcto_paso.append(jugada7)
                elif jugada7 == cosas[0] and cosas[1] in defensor and checks["check_abajo_derecha"] != True:
                    mov_correcto_comer.append(jugada7)
                    checks["check_abajo_derecha"] = True
                elif jugada7 == cosas[0] and cosas[1] in atacante and checks["check_abajo_derecha"] != True:
                    mov_defensa.append(jugada7)
                    checks["check_abajo_derecha"] = True

                if jugada8 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_izquierda"] != True:
                    mov_correcto_paso.append(jugada8)
                elif jugada8 == cosas[0] and cosas[1] in defensor and checks["check_abajo_izquierda"] != True:
                    mov_correcto_comer.append(jugada8)
                    checks["check_abajo_izquierda"] = True
                elif jugada8 == cosas[0] and cosas[1] in atacante and checks["check_abajo_izquierda"] != True:
                    mov_defensa.append(jugada8)
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
        check_1 , check_2 = enroque(pieza)
        if check_1 == True and pieza == "rey_blanco.png":
            mov_enrroque.append((7, 6))
        if check_1 == True and pieza == "rey_negro.png":
            mov_enrroque.append((0, 6))
        if check_2 == True and pieza == "rey_blanco.png":
            mov_enrroque.append((7, 2))
        if check_2 == True and pieza == "rey_negro.png":
            mov_enrroque.append((0, 2))
        jugada = (casilla[0] + 1, casilla[1] + 1)
        jugada2 = (casilla[0] - 1, casilla[1] - 1)
        jugada3 = (casilla[0] - 1, casilla[1] + 1)
        jugada4 = (casilla[0] + 1, casilla[1] - 1)
        jugada5 = (casilla[0] + 1, casilla[1])
        if mov_enrroque:
            check_enrroque_posible = True
        jugada6 = (casilla[0], casilla[1] + 1)
        jugada7 = (casilla[0] - 1, casilla[1])
        jugada8 = (casilla[0], casilla[1] - 1)
        for cosas in tablero:
            if jugada == cosas[0] and cosas[1] == "vacio.png" and checks["check_derecha"] != True:
                mov_correcto_paso.append(jugada)
            elif jugada == cosas[0] and cosas[1] in defensor and checks["check_derecha"] != True:
                mov_correcto_comer.append(jugada)
                checks["check_derecha"] = True
            elif jugada == cosas[0] and cosas[1] in atacante and checks["check_derecha"] != True:
                mov_defensa.append(jugada)
                checks["check_derecha"] = True

            if jugada2 == cosas[0] and cosas[1] == "vacio.png" and checks["check_izquierda"] != True:
                mov_correcto_paso.append(jugada2)
            elif jugada2 == cosas[0] and cosas[1] in defensor and checks["check_izquierda"] != True:
                mov_correcto_comer.append(jugada2)
                checks["check_izquierda"] = True
            elif jugada2 == cosas[0] and cosas[1] in atacante and checks["check_izquierda"] != True:
                mov_defensa.append(jugada2)
                checks["check_izquierda"] = True

            if jugada3 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba"] != True:
                mov_correcto_paso.append(jugada3)
            elif jugada3 == cosas[0] and cosas[1] in defensor and checks["check_arriba"] != True:
                mov_correcto_comer.append(jugada3)
                checks["check_arriba"] = True
            elif jugada3 == cosas[0] and cosas[1] in atacante and checks["check_arriba"] != True:
                mov_defensa.append(jugada3)
                checks["check_arriba"] = True

            if jugada4 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo"] != True:
                mov_correcto_paso.append(jugada4)
            elif jugada4 == cosas[0] and cosas[1] in defensor and checks["check_abajo"] != True:
                mov_correcto_comer.append(jugada4)
                checks["check_abajo"] = True
            elif jugada4 == cosas[0] and cosas[1] in atacante and checks["check_abajo"] != True:
                mov_defensa.append(jugada4)
                checks["check_abajo"] = True

            if jugada5 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_derecha"] != True:
                mov_correcto_paso.append(jugada5)
            elif jugada5 == cosas[0] and cosas[1] in defensor and checks["check_arriba_derecha"] != True:
                mov_correcto_comer.append(jugada5)
                checks["check_arriba_derecha"] = True
            elif jugada5 == cosas[0] and cosas[1] in atacante and checks["check_arriba_derecha"] != True:
                mov_defensa.append(jugada5)
                checks["check_arriba_derecha"] = True

            
            if jugada6 == cosas[0] and cosas[1] == "vacio.png" and checks["check_arriba_izquierda"] != True:
                mov_correcto_paso.append(jugada6)
            elif jugada6 == cosas[0] and cosas[1] in defensor and checks["check_arriba_izquierda"] != True:
                mov_correcto_comer.append(jugada6)
                checks["check_arriba_izquierda"] = True
            elif jugada6 == cosas[0] and cosas[1] in atacante and checks["check_arriba_izquierda"] != True:
                mov_defensa.append(jugada6)
                checks["check_arriba_izquierda"] = True
            
            if jugada7 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_derecha"] != True:
                mov_correcto_paso.append(jugada7)
            elif jugada7 == cosas[0] and cosas[1] in defensor and checks["check_abajo_derecha"] != True:
                mov_correcto_comer.append(jugada7)
                checks["check_abajo_derecha"] = True
            elif jugada7 == cosas[0] and cosas[1] in atacante and checks["check_abajo_derecha"] != True:
                mov_defensa.append(jugada7)
                checks["check_abajo_derecha"] = True

            if jugada8 == cosas[0] and cosas[1] == "vacio.png" and checks["check_abajo_izquierda"] != True:
                mov_correcto_paso.append(jugada8)
            elif jugada8 == cosas[0] and cosas[1] in defensor and checks["check_abajo_izquierda"] != True:
                mov_correcto_comer.append(jugada8)
                checks["check_abajo_izquierda"] = True
            elif jugada8 == cosas[0] and cosas[1] in atacante and checks["check_abajo_izquierda"] != True:
                mov_defensa.append(jugada8)
                checks["check_abajo_izquierda"] = True
            if mov_enrroque:
                for mov in mov_enrroque:
                    if mov not in mov_enrroque:
                        mov_enrroque_decidido.append(mov)
    try:
        
        return mov_correcto_paso, mov_correcto_comer, mov_defensa, mov_enrroque_decidido
    except:
        mov_enrroque_decidido = mov_final_enrroque
        return mov_correcto_paso, mov_correcto_comer, mov_defensa, mov_enrroque_decidido
#limpiar marcas de movimientos posibles
def actualizar_color_botones():
    for mov in movimientos_posibles:
        color_casilla = BLANCO if (mov[0] + mov[1]) % 2 == 0 else NEGRO
        ventana[mov].update(button_color=("", color_casilla))
    for mov in movimientos_defensa:
        color_casilla = BLANCO if (mov[0] + mov[1]) % 2 == 0 else NEGRO
        ventana[mov].update(button_color=("", color_casilla))
    if len(mov_final_enrroque) > 0:
        for ilem in mov_final_enrroque:
            if ilem != []:
                if ilem == (7,2) or ilem == (7,6):
                    color_casilla = BLANCO if (ilem[0] + ilem[1] - 1) % 2 == 0 else NEGRO
                    ventana[mov_enrroque].update(button_color=("", color_casilla))
    
mesa, tablero = crear_tablero()
ventana = sg.Window("Ajedrez-Bot by Emmanuel M Montesinos", mesa, resizable=True, icon="icono.ico",
                    finalize=True)

#Variables generales de logica
pieza_seleccionada = None
movimientos_posibles = []
movimientos_defensa = []
nueva_pos = None
nuevo_tablero2 = []
nivel_cpu = "-facil-"
check_disparador_enrroque1 = False
check_disparador_enrroque2 = False
jaque_blancas = False
pos_jaque_blancas = None
jaque_negras = False
pos_jaque_negras = None
turno = 0
cpu_turno = 1

ultima_ficha = []
#inicio de aplicacion
while True:
    if turno >= 1 and turno == cpu_turno:
        if nivel_cpu == "-facil-":
            nuevo_tablero = []
            antigua_pos, tipo_ficha, nueva_pos = cpu.jugada_facil(tablero,
                                                                  PIEZAS_CPU,
                                                                  PIEZAS_JUGADOR)
            if isinstance(nueva_pos, list):
                if len(nueva_pos) == 1:
                    for un in nueva_pos:
                        nueva_pos2 = un
                        nueva_pos = nueva_pos2
                else:
                    nueva_pos = choice(nueva_pos)
            for tab in tablero:
                if tab[0] == nueva_pos:
                    nombre_arreglado = tab[1]
                    nombre_arreglado = nombre_arreglado[:-4]
                    arreglo = [tab[0], tipo_ficha]
                    nuevo_tablero.append(arreglo)
                elif tab[0] == antigua_pos:
                    arreglo = [tab[0], "vacio.png"]
                    nombre_paso = tab[1]
                    nombre_abre = nombre_paso[:-4]
                    
                    nuevo_tablero.append(arreglo)
                else:
                    nuevo_tablero.append(tab)
            
            ventana[nueva_pos].update(image_filename=RUTA_PIEZAS_CLASICAS + tipo_ficha)
            ventana[antigua_pos].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
            tablero = nuevo_tablero
            resultado = calculo_piezas(nombre_arreglado)
            if resultado != "":
                for res in resultado:
                    ventana[res[1]].update(res[0])
            cpu_turno += 1

    if nueva_pos == None:
        nueva_pos = "Inicio"
    ultima_casilla = marcador.info_jugada(nueva_pos)
    ventana["-info-"].update(f"{ultima_casilla}")
    eventos, valores = ventana.read()
    
            
    if eventos == sg.WINDOW_CLOSED:
        break
    #boton reinicio
    if eventos == "-reiniciar-":
        tablero, mesa = rendirse()
        actualizar_color_botones()
        pieza_seleccionada = None
        movimientos_posibles = []
        movimientos_defensa = []
        nuevo_tablero2 = []
        ventana["-info-"].update("Inicio")
        check_disparador_enrroque1 = False
        check_disparador_enrroque2 = False
    #boton selector de nivel
    if eventos == "-nivel-":
        selector_nivel = [[sg.Button("Facil", key="-facil-"),
                        sg.Button("Normal", key="-normal-"),
                        sg.Button("Dificil", key="-dificil-")]]
        ventana_nivel = sg.Window(nivel_cpu, selector_nivel, icon="icono.ico")
        eventos2, valores2 = ventana_nivel.read()
        if eventos2 == "-facil-":
            nivel_cpu = eventos2
            ventana_nivel.close()
        if eventos2 == "-normal-":
            nivel_cpu = eventos2
            ventana_nivel.close()
        if eventos2 == "-dificil-":
            nivel_cpu = eventos2
            ventana_nivel.close()
    #pulsacion en la ventana
    elif isinstance(eventos, tuple):
        sprite = ""
        fila, columna = eventos
        op = (fila, columna)
        casilla = ventana[op]
        #comprueba condicion de enrroque
        if mov_final_enrroque != [[]] and len(movimientos_posibles) > 0:
            if op == mov_final_enrroque[0] and check_disparador_enrroque2 == False:
                for tab in tablero:
                    button_element = ventana[tab[0]]
                    background_color = button_element.TKButton.cget('background')
                    if background_color == 'yellow':
                        for sitios in checks_torres.values():
                            if sitios == op:
                                nuevo_tablero2 = []
                                turno += 1
                                ventana[sitios].update(image_filename=RUTA_PIEZAS_CLASICAS + "torre_blanca.png")
                                for tab2 in tablero:
                                    if tab2[0] == sitios:
                                        nv2 = (tab2[0], "rey_blanco.png")
                                        ventana[sitios].update(image_filename=RUTA_PIEZAS_CLASICAS + "rey_blanco.png")
                                        nuevo_tablero2.append(nv2)
                                    else:
                                        nuevo_tablero2.append(tab2)
                                tablero = nuevo_tablero2
                                nuevo_tablero2 = []
                                for tab2 in tablero:
                                    if tab2[0] == pieza_seleccionada:
                                        nv2 = (tab2[0], "vacio.png")
                                        nuevo_tablero2.append(nv2)
                                        ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                                    else:
                                        nuevo_tablero2.append(tab2)
                                tablero = nuevo_tablero2
                                actualizar_color_botones()
                                nuevo_tablero2 = []
                                 
                                if sitios == (7, 6):
                                    for tab2 in tablero:
                                        if tab2[0] == (7, 5):
                                            nv2 = (tab2[0], "torre_blanca.png")
                                            nuevo_tablero2.append(nv2)
                                            ventana[(7, 5)].update(image_filename=RUTA_PIEZAS_CLASICAS + "torre_blanca.png")
                                        else:
                                            nuevo_tablero2.append(tab2)
                                    tablero = nuevo_tablero2
                                    nuevo_tablero2 = []
                                    for tab2 in tablero:
                                        if tab2[0] == (7, 7):
                                            nv2 = (tab2[0], "vacio.png")
                                            nuevo_tablero2.append(nv2)
                                            ventana[(7, 7)].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                                        else:
                                            nuevo_tablero2.append(tab2)
                                    tablero = nuevo_tablero2
                                    actualizar_color_botones()
                                    
                                if sitios == (7, 2):
                                    for tab2 in tablero:
                                        if tab2[0] == (7, 3):
                                            nv2 = (tab2[0], "torre_blanca.png")
                                            nuevo_tablero2.append(nv2)
                                            ventana[(7, 3)].update(image_filename=RUTA_PIEZAS_CLASICAS + "torre_blanca.png")
                                        else:
                                            nuevo_tablero2.append(tab2)
                                    tablero = nuevo_tablero2
                                    nuevo_tablero2 = []
                                    for tab2 in tablero:
                                        if tab2[0] == (7, 0):
                                            nv2 = (tab2[0], "vacio.png")
                                            nuevo_tablero2.append(nv2)
                                            ventana[(7, 0)].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                                        else:
                                            nuevo_tablero2.append(tab2)
                                    
                                        
                                tablero = nuevo_tablero2
                                actualizar_color_botones()
                                pieza_seleccionada = None
                                check_disparador_enrroque1 = True
                                check_disparador_enrroque2 = True
                                
        actualizar_color_botones()
        if not pieza_seleccionada and check_disparador_enrroque1 == False:
            for ele in tablero:
                if eventos == ele[0]:
                    if ele[1] != "vacio.png":
                        if ele[1] in PIEZAS_JUGADOR:
                            mov_paso, mov_comer, mov_defensa, mov_enrroque = marcar_mov(eventos, ele[1])
                            
                            pieza_seleccionada = op
                            mov_final_enrroque = []
                            mov_final_enrroque.append(mov_enrroque)
                            for mov in mov_paso:
                                ventana[mov].update(button_color=("","green"))
                                movimientos_posibles.append(mov)
                            for mov in mov_comer:
                                ventana[mov].update(button_color=("", "red"))
                                movimientos_posibles.append(mov)
                            for mov in mov_defensa:
                                ventana[mov].update(button_color=("", "blue"))
                                movimientos_defensa.append(mov)
                            if (7, 2) in mov_final_enrroque or (7, 6) in mov_final_enrroque:
                                for cord in mov_final_enrroque:
                                    ventana[cord].update(button_color=("", "yellow"))
                                    movimientos_posibles.append(cord)
            
                            
        elif pieza_seleccionada:
            nuevo_tablero = []
            sprite = ""
            sprite_eliminado = ""
            for i in tablero:
                if pieza_seleccionada == i[0]:
                    sprite = i[1]
                    nv = (i[0], "vacio.png")
                    nuevo_tablero.append(nv) 
                elif op == i[0] and i[1] != "vacio.png":
                    pase = i[1]
                    pase2 = pase[:-4]
                    sprite_eliminado = pase             
                    nuevo_tablero.append(i)
                elif i[1] == "rey_blanco.png":
                    pos_rey = i[0]
                    nuevo_tablero.append(i)
                else:
                    nuevo_tablero.append(i)
            #Coronar Peon
            if op[0] == 0 and sprite[0] == "p":
                
                check_jaque = cpu.peligro_2(tablero, pos_rey, "blancas", PIEZAS_CPU, PIEZAS_JUGADOR)
                if check_jaque != True:
                    if op in movimientos_posibles:
                        if sprite_eliminado != "":
                            pieza_comida = sprite_eliminado[:-4]

                            negras[pieza_comida] -= 1
                            result1 = negras[pieza_comida]
                            result2 = marcador.marcador_negro2[pieza_comida]
                            result = result2 - result1
                            result3 = str(result)
                            pieza_final = pieza_comida + ".ficha"
                            ventana[pieza_final].update(result3)
                        sprite = cambiar_pieza(op)

                        ventana[op].update(image_filename=RUTA_PIEZAS_CLASICAS + sprite)
                        ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                        actualizar_color_botones()
                        turno += 1              
                        movimientos_posibles = []
                        movimientos_posibles = []
                        pieza_seleccionada = None
                        tablero = nuevo_tablero
                        nuevo_tablero = []
                        for i in tablero:
                            if op == i[0]:
                                nv = (op, sprite)
                                nuevo_tablero.append(nv)
                            else:
                                nuevo_tablero.append(i)
                        tablero = nuevo_tablero
                        nuevo_tablero = []
               
            if op in movimientos_posibles:
                check_jaque = cpu.peligro(tablero,pos_rey, "blancas", PIEZAS_CPU, PIEZAS_JUGADOR)  
                if check_jaque != True:
                    ventana[op].update(image_filename=RUTA_PIEZAS_CLASICAS + sprite)
                    ventana[pieza_seleccionada].update(image_filename=RUTA_PIEZAS_CLASICAS + "vacio.png")
                    actualizar_color_botones()
                    turno += 1
                    movimientos_posibles = []
                    pieza_seleccionada = None
                    tablero = nuevo_tablero
                    nuevo_tablero = []
                    for i in tablero:
                        if op == i[0]:
                            nv = (op, sprite)
                            nuevo_tablero.append(nv)
                            piezza = i[1]
                            pieza = piezza[-9:-4]
                            i_correcta1 = piezza[:-4]
                            i_correcta = i_correcta1 + ".ficha"
                            
                            
                        else:
                            nuevo_tablero.append(i)
                    tablero = nuevo_tablero
                    nuevo_tablero = []


            


            elif op not in movimientos_posibles:
                actualizar_color_botones()
                movimientos_posibles = []
                pieza_seleccionada = None
        
                    
                      
            
                                
                            
                

        
        check_disparador_enrroque1 = False

    

ventana.close()