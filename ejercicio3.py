# • Se pide calcular la nota de tu examen tipo test.
# • Serán 20 preguntas
# • Las preguntas correctas sumarán 0,5
# • Las preguntas incorrectas restarán 0,25 
# • Las preguntas sin contestar tendrán 0 

# Datos de entrada
    # preguntas correctas
    # preguntas incorrectas
    # preguntas sin contestar
# Datos de salida
    # preguntas correctas * 0.5
    # preguntas incorrectas * 0.25
    # nota total

# Identificadores
    # preguntas correctas (correctas)
    # preguntas incorrectas (incorrectas)
    # preguntas sin contestar (enblanco)
    # nota total (total)

# Proceso
    # nota_correctas=correctas*0.5
    # nota_incorrectas=incorrectas*0.25
    # nota_enblanco=0
    # total=nota_correctas-nota_incorrectas

# Python

def test():
    correctas=int(input('Cuantas preguntas has acertado: '))
    incorrectas=int(input('Cuantas preguntas has fallado: '))

    enblanco=20-(correctas+incorrectas)

    nota_correctas=correctas*0.5
    nota_incorrectas=incorrectas*0.25

    total=nota_correctas-nota_incorrectas

    print(f'De 20 preguntas se han acertado {correctas}, se han fallado {incorrectas} y no se han contestado {enblanco}. La nota final es: {total}')
    
test()
