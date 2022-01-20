from logic import *

# Diagnostic
symptomatic = Symbol("Covid sintomatico")
asymptomatic = Symbol("Covid asintomatico")
respiratory_disease = Symbol("Enfermedad respiratoria")
healthy = Symbol("Sano")

# Covid
covid = Or(asymptomatic, symptomatic)

# Vaccine scheme
no_scheme = Symbol("Sin esquema")
incomplete_scheme = Symbol("Esquema incompleto")
complete_scheme = Symbol("Esquema completo")


# Deathly
high_deathly = Symbol("Mortalidad Alta")
average_deathly = Symbol("Mortalidad Media")
low_deahtly = Symbol("Mortalidad Baja")

# Comorbidities
comorbidities = Symbol("Comorbilidades")

# Test
test = Symbol("Test")

# Syntoms
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
    Implication(And(Not(test), no_symtom), healthy),
    # Additional
    Implication(And(covid, complete_scheme) , low_deahtly),
    Implication(And(covid, incomplete_scheme), average_deathly),
    Implication(And(covid, no_scheme), high_deathly),
    Implication(And(covid, complete_scheme, comorbidities), average_deathly),
    Implication(And(covid, incomplete_scheme, comorbidities), high_deathly),
    Implication(And(covid, no_scheme, comorbidities), high_deathly)
)

# Diagnostics
diagnostics = [symptomatic, asymptomatic, respiratory_disease, healthy, high_deathly, average_deathly, low_deahtly]
