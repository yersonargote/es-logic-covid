from logic import *

# Diagnostic
symptomatic = Symbol("Sintomatico")
asymptomatic = Symbol("Asintomatico")
respiratory_disease = Symbol("Enfermedad respiratoria")
healthy = Symbol("Sano")

# Test
test = Symbol("Test")

# Syntom
cough = Symbol("Tos")
fever = Symbol("Fiebre")
dyspnea = Symbol("Disnea")
symtom =  Or(cough, fever, dyspnea)
no_symtom = And(Not(cough), Not(fever), Not(dyspnea))


# knowledge
knowledge = And(
    Implication(And(test, symtom), symptomatic),
    Implication(And(test, no_symtom), asymptomatic),
    Implication(And(Not(test), symtom), respiratory_disease),
    Implication(And(Not(test), no_symtom), healthy)
)

# Diagnostics
diagnostics = [symptomatic, asymptomatic, respiratory_disease, healthy]
