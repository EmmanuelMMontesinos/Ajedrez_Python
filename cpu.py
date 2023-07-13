from random import choice
import random



def marcar_mov(casilla, pieza ,PIEZAS_CPU, PIEZAS_JUGADOR, tablero, checks_torres):
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
            
    try:
        return mov_correcto_paso, mov_correcto_comer, mov_defensa, mov_enrroque_decidido
    except:
        mov_enrroque_decidido = []
        return mov_correcto_paso, mov_correcto_comer, mov_defensa, mov_enrroque_decidido





def jugada_facil(tablero, piezas_cpu,
                 piezas_jugador, checks_torres,
                 checks_enrroque, ultima_pieza_cpu, ultima_ficha):
    eleccion = []
    eleccion2 = []
    avanzar = []
    comer = []
    defender = []
    enrroque = []
    candidatos = []
    contador = 0
    top_ratio = 0
    while True:
        for tab in tablero:
            if tab[1] in piezas_cpu:
                ficha = tab[1]
                casilla = tab[0]
                ratio_atacar = 0
                ratio_defender = 0
                check_avanzar = False
                check_comer = False
                check_enrroque = False
                check_defensa = False
                mov_correcto_paso, mov_correcto_comer, mov_defensa, mov_enrroque_decidido = marcar_mov(casilla,
                                                                                                        ficha, piezas_cpu,
                                                                                                        piezas_jugador,
                                                                                                        tablero, checks_torres)
                if mov_correcto_paso:
                    for mov in mov_correcto_paso:
                        check_avanzar = True
                        ratio_atacar += 0.5
                        avanzar.append(mov_correcto_paso)
                if mov_correcto_comer:
                    for mov in mov_correcto_comer:
                        check_comer = True
                        ratio_atacar += 4
                        comer.append(mov_correcto_comer)
                if mov_enrroque_decidido:
                    for mov in mov_enrroque_decidido:
                        check_enrroque = True
                        enrroque.append(mov_enrroque_decidido)
                if mov_defensa:
                    for mov in mov_defensa:
                        check_defensa = True
                        ratio_defender += 3
                        defender.append(mov_defensa)
                
                ratio = ((ratio_atacar + 1) / (ratio_defender + 1)) * 2
                if ratio > top_ratio:
                    top_ratio = ratio
                    if len(comer) != 0:
                        for mov in comer:
                            if mov != []:
                                eleccion = [tab[0], tab[1], mov]
                    else:
                        for mov in avanzar:
                            if mov != []:
                                eleccion2 = [tab[0], tab[1], mov]
                
                avanzar = []
                comer = []
                defender = []
                enrroque = []
                candidatos = []
        if len(eleccion) > 2:
            anterior_pos = eleccion[0]
        else:
            anterior_pos = eleccion2[0]
        if anterior_pos != ultima_pieza_cpu:
            if len(eleccion) > 2:
                tipo_ficha = eleccion[1]
                nueva_pos = choice(eleccion[2])
            else:

                tipo_ficha = eleccion2[1]
                nueva_pos = choice(eleccion2[2])
            if ultima_ficha == tipo_ficha and len(eleccion) > 2:
                ultima_pieza_cpu = nueva_pos
                ultima_ficha = eleccion[1]
                return anterior_pos, tipo_ficha, nueva_pos, ultima_pieza_cpu, ultima_ficha

            if ultima_ficha == "":
                ultima_pieza_cpu = nueva_pos
                ultima_ficha = eleccion2[1]
                return anterior_pos, tipo_ficha, nueva_pos, ultima_pieza_cpu, ultima_ficha
        contador += 1
        if contador == 117:
            if len(eleccion) > 2:
                nueva_pos = eleccion[2]
            else:
                nueva_pos = eleccion2[2]
            ultima_pieza_cpu = nueva_pos
            ultima_ficha = eleccion2[1]
            return anterior_pos, tipo_ficha, nueva_pos, ultima_pieza_cpu, ultima_ficha

            
