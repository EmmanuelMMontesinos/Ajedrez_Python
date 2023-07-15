import PySimpleGUI as sg

PUNTUACION_ALGORITMO = {"jaque" : 10,
                        "c_reina" : 8,
                        "c_pieza" : 6,
                        "a_reina" : 5,
                        "a_pieza" : 3,
                        "c_peon" : 2,
                        "mover" : 1,
                        "desprotejer" : -2}

marcador_blanco = {"partida_ganada" : 0,
                   "torre_blanca" : 2,
                   "peon_blanco" : 8,
                   "alfil_blanco" : 2,
                   "caballo_blanco" : 2,
                   "reina_blanca" : 1,
                   "rey_blanco" : 1
                   }
marcador_blanco2 = {"partida_ganada" : 0,
                   "torre_blanca" : 2,
                   "peon_blanco" : 8,
                   "alfil_blanco" : 2,
                   "caballo_blanco" : 2,
                   "reina_blanca" : 1,
                   "rey_blanco" : 1
                   }
marcador_negro = {"partida_ganada" : 0,
                   "torre_negra" : 2,
                   "peon_negro" : 8,
                   "alfil_negro" : 2,
                   "caballo_negro" : 2,
                   "reina_negra" : 1,
                   "rey_negro" : 1
                   }
marcador_negro2 = {"partida_ganada" : 0,
                   "torre_negra" : 2,
                   "peon_negro" : 8,
                   "alfil_negro" : 2,
                   "caballo_negro" : 2,
                   "reina_negra" : 1,
                   "rey_negro" : 1
                   }

casillas_tablero = {
    (0, 0): "A8",
    (0, 1): "B8",
    (0, 2): "C8",
    (0, 3): "D8",
    (0, 4): "E8",
    (0, 5): "F8",
    (0, 6): "G8",
    (0, 7): "H8",
    (1, 0): "A7",
    (1, 1): "B7",
    (1, 2): "C7",
    (1, 3): "D7",
    (1, 4): "E7",
    (1, 5): "F7",
    (1, 6): "G7",
    (1, 7): "H7",
    (2, 0): "A6",
    (2, 1): "B6",
    (2, 2): "C6",
    (2, 3): "D6",
    (2, 4): "E6",
    (2, 5): "F6",
    (2, 6): "G6",
    (2, 7): "H6",
    (3, 0): "A5",
    (3, 1): "B5",
    (3, 2): "C5",
    (3, 3): "D5",
    (3, 4): "E5",
    (3, 5): "F5",
    (3, 6): "G5",
    (3, 7): "H5",
    (4, 0): "A4",
    (4, 1): "B4",
    (4, 2): "C4",
    (4, 3): "D4",
    (4, 4): "E4",
    (4, 5): "F4",
    (4, 6): "G4",
    (4, 7): "H4",
    (5, 0): "A3",
    (5, 1): "B3",
    (5, 2): "C3",
    (5, 3): "D3",
    (5, 4): "E3",
    (5, 5): "F3",
    (5, 6): "G3",
    (5, 7): "H3",
    (6, 0): "A2",
    (6, 1): "B2",
    (6, 2): "C2",
    (6, 3): "D2",
    (6, 4): "E2",
    (6, 5): "F2",
    (6, 6): "G2",
    (6, 7): "H2",
    (7, 0): "A1",
    (7, 1): "B1",
    (7, 2): "C1",
    (7, 3): "D1",
    (7, 4): "E1",
    (7, 5): "F1",
    (7, 6): "G1",
    (7, 7): "H1"
}


def info_jugada(nueva):
        if isinstance(nueva, tuple) != True:
                return nueva
        info = casillas_tablero[nueva]
        return info

def act_marc_piezas(pieza, bando, ventana):
        prueba = pieza[-9:-4]
        if pieza[-9:-4] == "blanca" or pieza[-9:-4] == "blanco":
                for i in bando.keys():
                        if i != "partida_ganada":
                                result1 = bando[i]
                                result2 = marcador_blanco[i]
                                result = result1 - result2
                                bando[i] = result
                                result = str(result)
                                ventana[i].update(f"{result}")
        
        if pieza[-9:-4] == "negra" or pieza[-9:-4] == "negro":
                for i in bando.keys():
                        if i != "partida_ganada":
                                result1 = bando[i]
                                result2 = marcador_negro[i]
                                result = result1 - result2
                                bando[i] = result
                                result = str(result)
                                ipo = i + ".ficha"
                                ventana[ipo].update(f"{result}")

