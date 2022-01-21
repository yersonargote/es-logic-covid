from copy import deepcopy
from logic import *
from covid import *


test_symptomatic = And(
    test,
    Not(dyspnea),
    fever,
    cough,
    incomplete_scheme,
    comorbidities
)


test_asymptomatic = And(
    test,
    Not(dyspnea),
    Not(fever),
    Not(cough),
    complete_scheme
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


def main():
    symp: And  = deepcopy(knowledge)
    asymp: And = deepcopy(knowledge)
    res_dis: And = deepcopy(knowledge)
    healthy: And = deepcopy(knowledge)

    # Tests
    symp.add(test_symptomatic)
    asymp.add(test_asymptomatic)
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


if __name__ == '__main__':
    main()
