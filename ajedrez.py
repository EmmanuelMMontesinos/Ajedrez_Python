


def victoria(tablero):
    check_negro = False
    check_blanco = False
    for tab in tablero:
        if tab[1] == "rey_blanco.png":
            check_blanco = True
        elif tab[1] == "rey_negro.png":
            check_negro = True
    return check_blanco, check_negro