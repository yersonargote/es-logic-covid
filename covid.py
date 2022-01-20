from typing import List
from copy import deepcopy
from logic import *
from globals import *


def check_knowledge(knowledge, symbols):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}")
   
    return knowledge, diagnostics


def test_symptomatic(knowledge: And, diagnostics: List[Symbol]):
    knowledge.add(
        And(
            test,
            Not(dyspnea),
            fever,
            cough,
            complete_scheme
        )
    )

    check_knowledge(knowledge=knowledge, symbols=diagnostics)


def test_asymptomatic(knowledge: And, diagnostics: List[Symbol]):
    knowledge.add(
        And(
            test,
            Not(dyspnea),
            Not(fever),
            Not(cough),
            incomplete_scheme
        )
    )

    check_knowledge(knowledge=knowledge, symbols=diagnostics)


def test_respiratory_disease(knowledge: And, diagnostics: List[Symbol]):
    knowledge.add(
        And(
            Not(test),
            Not(dyspnea),
            fever,
            Not(cough)
        )
    )

    check_knowledge(knowledge=knowledge, symbols=diagnostics)



def test_healthy(knowledge: And, diagnostics: List[Symbol]):
    knowledge.add(
        And(
            Not(test),
            Not(dyspnea),
            Not(fever),
            Not(cough)
        )
    )
    check_knowledge(knowledge=knowledge, symbols=diagnostics)


def main():

    symp = deepcopy(knowledge)
    asymp = deepcopy(knowledge)
    res_dis = deepcopy(knowledge)
    healthy = deepcopy(knowledge)

# Test symptomatic
    print('Test para covid sintomatico.')
    print('- Diagnostico: ', end='')
    test_symptomatic(symp, diagnostics)

# Test asymptomatic
    print('Test para covid asintomatico.')
    print('- Diagnostico: ', end='')
    test_asymptomatic(asymp, diagnostics)

# Test respiratory disease
    print('Test para enfermedad respiratoria.')
    print('- Diagnostico: ', end='')
    test_respiratory_disease(res_dis, diagnostics)

# Test healthy
    print('Test para sano.')
    print('- Diagnostico: ', end='')
    test_healthy(healthy, diagnostics)


if __name__ == '__main__':
    main()
