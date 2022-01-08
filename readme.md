# Proyecto Diagnóstico Covid-19

Usted ha sido contratado para desarrollar un sistema experto para diagnosticar el estado de salud de una
persona con respecto al Coronavirus1 de Wuhan.
El experto de la salud señala que una persona puede tener el virus y no presentar sintomatología. Los
síntomas más comunes de la enfernedad son fiebre, tos y dificultad para respirar (disnea). Se debe realizar
una prueba de laboratorio a la persona para poder identificar la presencia del virus.
Según la información del experto se puede determinar el estado de salud de una persona a partir de la
prueba y la presencia de síntomas. La siguiente tabla recopila los datos suministrados por el experto:

| Estado de salud         | Prueba   | Fiebre | Tos   | Disnea |
| ----------------------- | -------- | ------ | ----- | ------ |
| Covid asintomatico      | Positiva | Si/No  | Si/No | Si/No  |
| Covid sintomatico       | Positiva | Si/No  | Si/No | Si/No  |
| Enfermedad respiratoria | Negativa | Si/No  | Si/No | Si/No  |
| Sano                    | Negativa | Si/No  | Si/No | Si/No  |

**Implementar el sistema experto en python utilizando el módulo logic.py. Puede guiarse con el ejemplo
visto en clase sobre el juego Clue.**
1. Defina todos los simbolos que considere necesarios. Para ello identifique primero objetos y sus
posibles valores.
2. Redefina el método check_knowledge(knowledge)
3. Defina todas las reglas iniciales que debe tener la base de conocimiento (knowledge). Escríbalas
primero en notación de lógica proposicional y luego si implementelas en Python.
4. Agregue hechos con el método add a la base de conocimiento para comprobar que el programa
hace inferencias correctas para cada uno de los 4 posibles diagnósticos. Es obligatorio que el código
incluya por lo menos un ejemplo para cada diagnóstico.
5. Implemente funcionalidades adicionales a las pedidas en el enunciado según su creatividad y el
conocimiento que usted tiene acerca del virus. El factor diferenciador influirá notablemente en su
calificación.
6. Realice un video de máximo 3 minutos donde muestre el funcionamiento de su programa.
7. Entrega: La solución debe ser entregada de manera individual en el Classroom antes de la fecha
límite. Se puede realizar el trabajo en parejas y para ello debe registrar en los comentarios de esta
tarea en el Classroom los integrantes del grupo o si va a trabajar individual. La nota de la
sustentación será individual. Para poder ser evaluado debe registrar esta información antes del día
de la sustentación.
