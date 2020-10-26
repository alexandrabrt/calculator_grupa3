import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul,  "/": operator.truediv}

joc = True

while joc:
    start = 0
    primul_input = input("Alegeti un numar: ")
    al_doilea_input = input("Alegeti semnul matematic: ")
    al_treilea_input = input("Alegeti un numar: ")
    if al_treilea_input == "0" and al_doilea_input == "/":
        print("Nu stiu deastea.")
    elif al_doilea_input in ops.keys():
        start = ops[al_doilea_input](float(primul_input), float(al_treilea_input))
        print(start)
        alta_operatie = input("Doriti sa faceti o alta operatie Da / Nu: ").upper()
        joc = False
        if alta_operatie == "DA":
            joc = True
            start = 0



