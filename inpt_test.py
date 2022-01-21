from logic import *
from covid import *

def yes_no():
    exit = False
    response = 0
    while not exit:
        inpt = input("1. si.\n2. no.\n3. salir.\n")
        if inpt == '1':
            response = 1
        elif inpt == '2':
            response = 2
        elif inpt == '3':
            response = 3
        exit = (response > 0 and response < 4)
    return response


def test_with_inpt():
    valid = False
    exit = False
    info = And()

    while not exit:
        print('Diagnostico del covid-19')
        while not valid:
            print('Indique estado de la prueba de covid-19.')
            print('1. positiva.')
            print('2. negativa.')
            print('3. salir')
            inpt = input()
            if inpt == '1':
                info.add(test)
            elif inpt == '2':
                info.add(Not(test))
            else:
                exit = True
            valid = (inpt == '1' or inpt == '2' or inpt == '3')

        if exit:
            continue

        print('Presenta fiebre.')
        response = yes_no()
        if response == 1:
            info.add(fever)
        elif response == 2:
            info.add(Not(fever))
        else:
            exit = True
            continue

        print('Presenta tos.')
        response = yes_no()
        if response == 1:
            info.add(cough)
        elif response == 2:
            info.add(Not(cough))
        else:
            exit = True
            continue

        print('Presenta disnea.')
        response = yes_no()
        if response == 1:
            info.add(dyspnea)
        elif response == 2:
            info.add(Not(dyspnea))
        else:
            exit = True
            continue

        knowledge.add(info)
        print('Diagnostico: ', end='')
        check_knowledge(knowledge=knowledge, symbols=diagnostics)
        exit = (input("1. salir.") == '1')


