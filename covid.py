from logic import *


# Check knowledge
def check_knowledge(knowledge, symbols):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"    {symbol}")
 

# Diagnostic
symptomatic = Symbol("Covid_Sintomatico")
asymptomatic = Symbol("Covid_Asintomatico")
respiratory_disease = Symbol("Enfermedad_Respiratoria")
healthy = Symbol("Sano")

# Covid
covid = Or(asymptomatic, symptomatic)

# Vaccine scheme
no_scheme = Symbol("Sin_Esquema")
incomplete_scheme = Symbol("Esquema_Incompleto")
complete_scheme = Symbol("Esquema_Completo")


# Mortality
high_deathly = Symbol("Mortalidad_Alta")
average_deathly = Symbol("Mortalidad_Media")
low_deahtly = Symbol("Mortalidad_Baja")

# Comorbidities
comorbidities = Symbol("Comorbilidades")

# Test
test = Symbol("Prueba")

# Syntoms
cough = Symbol("Tos")
fever = Symbol("Fiebre")
dyspnea = Symbol("Disnea")
symtom =  Or(cough, fever, dyspnea)
no_symtom = And(Not(cough), Not(fever), Not(dyspnea))

# Variants
omicron = Symbol("Omicron")
delta = Symbol("Delta")

# Recomendaciones
finish_scheme = Symbol("Terminar_Esquema")

# knowledge == reglas
knowledge = And(
    Implication(And(test, symtom), symptomatic),
    Implication(And(test, no_symtom), asymptomatic),
    Implication(And(Not(test), symtom), respiratory_disease),
    Implication(And(Not(test), no_symtom), healthy),
    # Additional
    Implication(And(covid, Or(delta, omicron), complete_scheme, Not(comorbidities)) , low_deahtly),
    Implication(And(covid, Or(delta, omicron), complete_scheme, comorbidities) , average_deathly),
    Implication(And(covid, Or(delta, omicron), incomplete_scheme, Not(comorbidities)), average_deathly),
    Implication(And(covid, Or(delta, omicron), incomplete_scheme, comorbidities), high_deathly),
    Implication(And(covid, Or(delta, omicron), no_scheme, Not(comorbidities)), high_deathly),
    Implication(And(covid, Or(delta, omicron), no_scheme, comorbidities), high_deathly),
    Implication(Or(no_scheme, incomplete_scheme), finish_scheme),
)

# Diagnostics
diagnostics = [symptomatic, asymptomatic, respiratory_disease, healthy, high_deathly, average_deathly, low_deahtly, finish_scheme]
