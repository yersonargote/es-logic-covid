from copy import deepcopy
from logic import *
from globals import *


def check_knowledge(knowledge, symbols):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"    {symbol}")
    

test_symptomatic = And(
    test,
    Not(dyspnea),
    fever,
    cough,
    complete_scheme
)


test_asymptomatic = And(
    test,
    Not(dyspnea),
    Not(fever),
    Not(cough),
    incomplete_scheme
)


test_respiratory_disease = And(
    Not(test),
    Not(dyspnea),
    fever,
    Not(cough)
)


test_healthy = And(
    Not(test),
    Not(dyspnea),
    Not(fever),
    Not(cough)
)


def manual_test():
    symp: And  = deepcopy(knowledge)
    asymp: And = deepcopy(knowledge)
    res_dis: And = deepcopy(knowledge)
    healthy: And = deepcopy(knowledge)

    # Test
    symp.add(test_asymptomatic)
    asymp.add(test_symptomatic)
    res_dis.add(test_respiratory_disease)
    healthy.add(test_healthy)
    tests = [
        ("Test 1.", symp),
        ("Test 2.", asymp),
        ("Test 3.", res_dis),
        ("Test 4.", healthy),
    ]

    for test, know in tests:
        print(test)
        check_knowledge(knowledge=know, symbols=diagnostics)


def yes_no():
    exit = False
    yes = False
    while not exit:
        inpt = input("si/no. 'sal' para salir. ")
        if inpt == 'si':
            yes = True
        exit = (inpt == 'si' or inpt == 'no' or inpt == 'sal')
    return yes


def main():
    valid = False
    info = And()

    print('Diagnostico del covid-19')
    while not valid:
        print('Indique estado de la prueba de covid-19.')
        print('1. Positiva.')
        print('2. Negativa.')
        inpt = input()
        if inpt == '1':
            info.add(test)
        elif inpt == '2':
            info.add(Not(test))
        valid = (inpt == '1' or inpt == '2')

    print('Presenta fiebre.')
    yes = yes_no()
    if yes:
        info.add(fever)
    else:
        info.add(Not(fever))

    print('Presenta tos.')
    yes = yes_no()
    if yes:
        info.add(cough)
    else:
        info.add(Not(cough))

    print('Presenta disnea.')
    yes = yes_no()
    if yes:
        info.add(dyspnea)
    else:
        info.add(Not(dyspnea))

    knowledge.add(info)
    print('Diagnostico: ', end='')
    check_knowledge(knowledge=knowledge, symbols=diagnostics)


if __name__ == '__main__':
    main()
