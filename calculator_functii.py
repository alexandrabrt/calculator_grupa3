
def adunare(x: float, y: float) -> float:
    """

    :param x: primul numar introdus de la tastatura
    :param y: al doilea numar introdus de la tastatura
    :return: suma numerelor
    """
    return x + y


def scadere(x: float, y: float) -> float:
    """

    :param x: primul numar introdus de la tastatura
    :param y: al doilea numar introdus de la tastatura
    :return: diferenta numerelor
    """
    return x - y


def inmultire(x: float, y: float) -> float:
    """

    :param x: primul numar introdus de la tastatura
    :param y: al doilea numar introdus de la tastatura
    :return: produsul celor doua numere
    """
    return x * y


def impartire(x: float, y: float) -> str:
    """

    :param x: primul numar introdus de la tastatura
    :param y: al doilea numar introdus de la tastatura
    :return: rezulatul impartii celor doua numere
    """
    if y == 0:
        return "Nu stiu deastea."
    elif y != 0:
        return f"{x / y}"


def calculator(primul_input: float, al_doilea_input: str, al_treilea_input: float) -> str:
    """

    :param primul_input: primul numar introdus de la tastatura
    :param al_doilea_input: operatia artimetica
    :param al_treilea_input: al doilea numar introdus de la tastatura
    :return: un mesaj cu rezultatul
    """
    calcul = None

    if al_doilea_input == "+":
        calcul = adunare(primul_input, al_treilea_input)
    elif al_doilea_input == "-":
        calcul = scadere(primul_input, al_treilea_input)
    elif al_doilea_input == "*":
        calcul = inmultire(primul_input, al_treilea_input)
    elif al_doilea_input == "/":
        calcul = impartire(primul_input, al_treilea_input)

    return f"Rezultatul este: {calcul}"


def recalculare():
    """
    :return: inceperea unei noi operatii
    """

    alta_operatie = input("Doriti sa faceti o alta operatie Da / Nu: ").upper()
    joc = False
    if alta_operatie == "DA":
        joc = True
    return joc


def main():

    reincercare = True
    while reincercare:
        primul_input = float(input("Alegeti un numar: "))
        al_doilea_input = input("Alegeti semnul matematic: ")
        al_treilea_input = float(input("Alegeti un numar: "))
        print(calculator(primul_input, al_doilea_input, al_treilea_input))
        reincercare = recalculare()


main()
