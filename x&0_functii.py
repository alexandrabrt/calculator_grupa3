import random

# Printam plansa de joc.


def desenam_plansa(tabla: dict):
    """

    :param tabla: dictionarul cu pozitile ocupate
    :return: deseneaza tabla de joc
    """

    string_de_printat = str(' ' + tabla[1] + ' | ' + tabla[2] + ' | ' + tabla[3] + "\n"
                            + '-----------' + "\n"
                            + ' ' + tabla[4] + ' | ' + tabla[5] + ' | ' + tabla[6] + "\n"
                            + '-----------' + "\n" +
                            ' ' + tabla[7] + ' | ' + tabla[8] + ' | ' + tabla[9] + "\n")
    return print(string_de_printat)


# Se verifica toate posibilitatile castigatoare.


def verificare_stadiu_joc(verificare: dict, player: str):
    """

    :param verificare: dictionarul cu pozitile ocupate
    :param player: caracterul jucatorului / calculatorului
    :return: status joc (castigat sau nu)
    """

    joc_castigat = False
    if verificare[1] == verificare[2] == verificare[3] == player:
        joc_castigat = True
    elif verificare[4] == verificare[5] == verificare[6] == player:
        joc_castigat = True
    elif verificare[7] == verificare[8] == verificare[9] == player:
        joc_castigat = True
    elif verificare[1] == verificare[4] == verificare[7] == player:
        joc_castigat = True
    elif verificare[2] == verificare[5] == verificare[8] == player:
        joc_castigat = True
    elif verificare[3] == verificare[6] == verificare[9] == player:
        joc_castigat = True
    elif verificare[1] == verificare[5] == verificare[9] == player:
        joc_castigat = True
    elif verificare[7] == verificare[5] == verificare[3] == player:
        joc_castigat = True
    return joc_castigat


def main_game():

    # Dictionarul de valori ce corespunde tablei:
    plansa = {1: " ", 2: " ", 3: " ",
              4: " ", 5: " ", 6: " ",
              7: " ", 8: " ", 9: " "}

    # Atribuire litera pentru jucator/calculator
    jucator = input("Alegeti cu ce incepeti (X sau 0) \n").upper()
    calculator = None
    if jucator == "X":
        calculator = "0"
    elif jucator == "0":
        calculator = "X"
    else:
        print("Ati ales un caracter invalid! V-a fost alocat automat caracterul '0' ")
        jucator == "0"
        calculator = "X"
    # Atribuire random a celui care incepe primul (calculator sau jucator)
    jucator_sau_calculator = ["jucator", "calculator"]
    cine_incepe = random.choice(jucator_sau_calculator)
    print(f"Jucatorul care incepe este: {cine_incepe}")

    # Executam functia pentru printare
    desenam_plansa(plansa)

    # Lista pentru a determina ce key ale dictionarului mai sunt libere
    locuri_libere = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        # Se verifica daca mai exista locuri libere pentru a determina daca e egalitate sau nu.
        if not locuri_libere:
            print("Tie!")
            desenam_plansa(plansa)
            break

        # Se alege prima pozitie din joc.
        elif cine_incepe == "jucator":
            # Se alege pozitia literei jucatorului.
            alege_pozitia = input("Alege pozitia: \n")
            # Dupa ce jucatorul si-a terminat tura, incepe tura calculatorului.
            cine_incepe = "calculator"
            # Se verifica disponibilitatea pozitiei si se completeaza daca este disponibila.
            if alege_pozitia.isdigit():
                if int(alege_pozitia) in locuri_libere:
                    # Se sterge din lista de verificare pozitia aleasa.
                    locuri_libere.remove(int(alege_pozitia))
                    plansa[int(alege_pozitia)] = jucator
                # Se anunta jucatorul ca pozitia este deja ocupata.
                elif int(alege_pozitia) not in locuri_libere:
                    print("Spatiu ocupat deja sau inexistent!")
                    # Se pastreaza tura jucatorului in cazul in care a accesat o pozitie deja ocupata.
                    cine_incepe = "jucator"
            else:
                print("Ati ales un caracter invalid! Introduceti un caracter numeric corespunzator pozitiei!")
                cine_incepe = "jucator"
            # Se verifica daca jucatorul a castigat.
            if verificare_stadiu_joc(plansa, jucator):
                print("A castigat jucatorul!")
                desenam_plansa(plansa)
                break

        elif cine_incepe == "calculator":
            # Calculatorul alege random una din pozitiile ramase.
            alege_pozitia = random.choice(locuri_libere)
            # Se completeaza pozitia aleasa de calculator.
            plansa[alege_pozitia] = calculator
            # Se sterge din lista de verificare pozitia aleasa.
            locuri_libere.remove(int(alege_pozitia))
            # Se verifica daca calculatorul a castigat.
            if verificare_stadiu_joc(plansa, calculator):
                print("A castigat calculatorul!")
                desenam_plansa(plansa)
                break
            # Dupa ce calculatorul si-a terminat tura, incepe tura jucatorului.
            cine_incepe = "jucator"

        desenam_plansa(plansa)


def main():

    retry = True
    while retry:

        main_game()
        aux = input("Doriti sa incepe un joc nou ? Raspundeti cu da sau nu!) \n")
        if aux == "nu":
            retry = False
            break
        elif aux != "da":
            print("Text nerecunoscut! Oprire joc!")
            retry = False
            break
