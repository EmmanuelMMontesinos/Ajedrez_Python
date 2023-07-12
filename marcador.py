import PySimpleGUI as sg

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
                