from random import choice
import random
import marcador


algoritmo = marcador.PUNTUACION_ALGORITMO.copy()

class candidatos:
    def __init__(self,ratio,pos,tipo,tablero):
        self.ratio = ratio
        self.pos = pos
        self.tipo = tipo
        self.tablero = tablero



def marcar_mov(casilla, pieza ,PIEZAS_CPU, PIEZAS_JUGADOR, tablero):
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
    if pieza[0] == "p":
        if casilla[0] == 6:
            mov_posibles.append((casilla[0] + 1, casilla[1]))
            check = False
            mov_posibles.append((casilla[0] + 2, casilla[1]))
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
            mov_posibles.append((casilla[0] + 1, casilla[1] + 1))
            mov_posibles.append((casilla[0] + 1, casilla[1] - 1))
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
            mov_posibles.append((casilla[0] + 1, casilla[1]))
            for mov in mov_posibles:
                for piez in tablero:
                    if mov == piez[0] and piez[1] == "vacio.png":
                        mov_correcto_paso.append(mov)
            mov_posibles = []
            mov_posibles.append((casilla[0] + 1, casilla[1] + 1))
            mov_posibles.append((casilla[0] + 1, casilla[1] - 1))
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
        mov_posibles.append((casilla[0] + 1, casilla[1] + 2))
        mov_posibles.append((casilla[0] + 2, casilla[1] + 1))
        mov_posibles.append((casilla[0] - 1, casilla[1] - 2))
        mov_posibles.append((casilla[0] - 2, casilla[1] - 1))
        mov_posibles.append((casilla[0] - 1, casilla[1] + 2))
        mov_posibles.append((casilla[0] - 2, casilla[1] + 1))
        mov_posibles.append((casilla[0] + 1, casilla[1] - 2))
        mov_posibles.append((casilla[0] + 2, casilla[1] - 1))
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
            jugada = (casilla[0] - (n + 1), casilla[1])
            jugada2 = (casilla[0] + (n + 1), casilla[1])
            jugada3 = (casilla[0], casilla[1] - (n + 1))
            jugada4 = (casilla[0], casilla[1] + (n + 1))
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
            jugada = (casilla[0] - (n + 1), casilla[1] - (n + 1))
            jugada2 = (casilla[0] + (n + 1), casilla[1] + (n + 1))
            jugada3 = (casilla[0] + (n + 1), casilla[1] - (n + 1))
            jugada5 = (casilla[0] - (n + 1), casilla[1] + (n + 1))
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
            jugada = (casilla[0] - (n + 1), casilla[1] - (n + 1))
            jugada2 = (casilla[0] + (n + 1), casilla[1] + (n + 1))
            jugada3 = (casilla[0] + (n + 1), casilla[1] - (n + 1))
            jugada4 = (casilla[0] - (n + 1), casilla[1] + (n + 1))
            jugada5 = (casilla[0] - (n + 1), casilla[1])
            jugada6 = (casilla[0], casilla[1] - (n + 1))
            jugada7 = (casilla[0] + (n + 1), casilla[1])
            jugada8 = (casilla[0], casilla[1] + (n + 1))
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

        jugada = (casilla[0] - 1, casilla[1] - 1)
        jugada2 = (casilla[0] + 1, casilla[1] + 1)
        jugada3 = (casilla[0] + 1, casilla[1] - 1)
        jugada4 = (casilla[0] - 1, casilla[1] + 1)
        jugada5 = (casilla[0] - 1, casilla[1])
        
        jugada6 = (casilla[0], casilla[1] - 1)
        jugada7 = (casilla[0] + 1, casilla[1])
        jugada8 = (casilla[0], casilla[1] + 1)
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
            
    
    return mov_correcto_paso, mov_correcto_comer, mov_defensa

#mejor candidato de la simulacion
def ratio_simulacion(candidatos):
    ratio = 0
    max_ratio_pieza = 0
    mejor_candidato = []
    for candi in candidatos:
        if candi[0] > max_ratio_pieza:
            max_ratio_pieza = candi[0]
            mejor_candidato.append(candi)
        ratio += candi[0]
    return mejor_candidato, ratio, max_ratio_pieza


def peligro(tablero, pos, bando, piezas_cpu, piezas_jugador):
    if bando == "blancas":
        medio = "negras"
    else:
        medio = "blancas"
    for tab in tablero:
        if tab[0] == pos:
            candidatos = calcular_ratio_peligro(tablero, piezas_cpu, piezas_jugador, medio)
            for candi in candidatos:
                for mov in candi[:3]:
                    if mov == pos:
                        return True
    return False

def calcular_ratio_peligro(tablero, piezas_cpu, piezas_jugador,bando):
    ratio = 0
    if bando == "blancas":
        set_piezas = piezas_jugador
    else:
        set_piezas = piezas_cpu
    simulacion_candidatos = []
    for tab in tablero:
        if tab[1] in set_piezas:
            mov_paso, mov_comer, mov_defensa = marcar_mov(tab[0],tab[1],piezas_cpu,piezas_jugador,tablero)
            for mov in mov_comer:
                for tab2 in tablero:
                    if tab2[0] == mov:
                        #comprobar si va ha ser comida
                        check_peligro = peligro(tablero, mov, "negras", piezas_cpu, piezas_jugador)
                        if check_peligro == True:
                            ratio -= 10000000000
                        selecion_pi = tab2[1]
                        pi = selecion_pi[:3]
                        if pi == "rey":
                            ratio += 10
                        if pi == "rei":
                            ratio += 8
                        if pi == "alf" or pi == "cab" or pi == "tor":
                            ratio += 6
                        if pi == "peo":
                            ratio += 3
            for mov in mov_paso:
                ratio += 1
            for mov in mov_defensa:
                for tab2 in tablero:
                    if tab2[0] == mov:
                        selecion_pi = tab2[1]
                        pi = selecion_pi[:3]
                        if pi == "rei":
                            ratio -= 50
                        if pi == "alf" or pi == "cab" or pi == "tor":
                            ratio -= 15
                        if pi == "peo":
                            ratio -= 5
            simulacion_candidatos.append((tab[0], tab[1], ratio, mov_comer, mov_paso, mov_defensa))
            ratio = 0
    return simulacion_candidatos

#simulacion de candidato posibles
def calcular_ratio(tablero, piezas_cpu, piezas_jugador,bando):
    ratio = 0
    if bando == "blancas":
        set_piezas = piezas_jugador
    else:
        set_piezas = piezas_cpu
    simulacion_candidatos = []
    all_moves = []
    for tab in tablero:
        if tab[1] in set_piezas:
            mov_paso, mov_comer, mov_defensa = marcar_mov(tab[0],tab[1],piezas_cpu,piezas_jugador,tablero)
            for mov in mov_comer:
                for tab2 in tablero:
                    if tab2[0] == mov:
                        #comprobar si va ha ser comida
                        check_peligro = peligro(tablero, mov, "negras", piezas_cpu, piezas_jugador)
                        if check_peligro == True:
                            ratio -= 10000000000
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        selecion_pi = tab2[1]
                        pi = selecion_pi[:3]
                        if pi == "rey":
                            ratio += 10000000
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        if pi == "rei":
                            ratio += 8
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        if pi == "alf" or pi == "cab" or pi == "tor":
                            ratio += 6
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        if pi == "peo":
                            ratio += 3
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
            
            for mov in mov_paso:
                check_peligro = peligro(tablero, mov, "negras", piezas_cpu, piezas_jugador)
                if check_peligro == True:
                    ratio -= 10000000000
                    all_moves.append((ratio, tab[0], tab[1], mov))
                    ratio = 0
                else:
                    ratio += 1
                    all_moves.append((ratio, tab[0], tab[1], mov))
                    ratio = 0
            
            for mov in mov_defensa:
                for tab2 in tablero:
                    if tab2[0] == mov:
                        selecion_pi = tab2[1]
                        pi = selecion_pi[:3]
                        if pi == "rei":
                            ratio -= 50
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        if pi == "alf" or pi == "cab" or pi == "tor":
                            ratio -= 15
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
                        if pi == "peo":
                            ratio -= 5
                            all_moves.append((ratio, tab[0], tab[1], mov))
                            ratio = 0
            
    return all_moves
    

def generar_tablero_simulado(tablero,pos_pieza,pieza, prx_pos):
    tablero_simulado = []
    for tab in tablero:
        if tab[0] == pos_pieza:
            ficha = (tab[0], "vacio.png")
            tablero_simulado.append(ficha)
        elif tab[0] == prx_pos:
            ficha = (tab[0], pieza)
            tablero_simulado.append(ficha)
        else:
            tablero_simulado.append(tab)
    return tablero_simulado

def jugada_facil(tablero, piezas_cpu, piezas_jugador):
    ciclo = 0
    n_pieza_ciclo = 0
    ratio = 0
    candidatos = []
    elecion = ()
    ratio_elecion = 0
    original_tablero = tablero
    nuevo_tablero = []
    candidatos = calcular_ratio(tablero,piezas_cpu,piezas_jugador, "negras")
    jugada_final = []
    mejor_candidato = []
    nuevo_ratio = 0
    ratio_global = 0
    #genero nuevos tableros para la simulacion
    candidatos_finales = []
    for candi in candidatos:
        #comer
        candidatos_comer = []
        ciclo_mov = 0
        for elemento in candi:
            if ciclo_mov == 3:
                #1º ciclo simulacion
                simulacion_tablero = generar_tablero_simulado(tablero, candi[1], candi[1], elemento)
                candidatos_enemigos = calcular_ratio(simulacion_tablero, piezas_cpu, piezas_jugador, "blancas")
                nuevo_ratio = ratio + candi[0]
                for candi2 in candidatos_enemigos:
                    #2º ciclo simulacion
                    for elemento2 in candi2:
                        if ciclo_mov == 3:
                            simulacion_tablero = generar_tablero_simulado(simulacion_tablero, candi2[1], candi2[1], elemento2)
                            candidatos_aliados = calcular_ratio(simulacion_tablero, piezas_cpu, piezas_jugador, "blancas")
                            nuevo_ratio = ratio + candi2[0]
                            for candi3 in candidatos_aliados:
                                for elemento3 in candi3:
                                    if ciclo_mov == 3:
                                        #1º ciclo simulacion
                                        simulacion_tablero = generar_tablero_simulado(simulacion_tablero, candi3[1], candi3[1], elemento3)
                                        candidatos_enemigos2 = calcular_ratio(simulacion_tablero, piezas_cpu, piezas_jugador, "blancas")
                                        nuevo_ratio = ratio + candi3[0]
                                        for candi4 in candidatos_enemigos2:
                                            #2º ciclo simulacion
                                            for elemento3 in candi4:
                                                if ciclo_mov == 3:
                                                    simulacion_tablero = generar_tablero_simulado(simulacion_tablero, candi4[1], candi4[1],
                                                                                                   elemento4)
                                                    candidatos_aliados2 = calcular_ratio(simulacion_tablero, piezas_cpu, piezas_jugador, "blancas")
                                                    nuevo_ratio = ratio + candi4[0]
        ficha_paso = ((candi[0] + nuevo_ratio), candi[1], candi[2], candi[3])
        jugada_final.append(ficha_paso)
    for jugadas in jugada_final:
        
        if jugadas[0] > ratio_global:
            antigua_pos = jugadas[1]
            tipo_ficha = jugadas[2]
            nueva_pos = jugadas[3]
            ratio_global = jugadas[0]
    
    

    return antigua_pos, tipo_ficha, nueva_pos

