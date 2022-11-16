#datos de entrada:
    #base del rectángulo
    #altura del rectangulo
#datos de salida:
    #perimetro del rectangulo
    #area del rectangulo
#identificadores:
    #base del rectangulo(base)
    #altura del rectangulo (altura)
    #perimetro(perimetro)
    #area(area)
#proceso:
    #perimetro=base*2 + altura*2
    #area=base por altura


def rectangulo():
    base=float(input('Cual es la base del rectangulo: '))
    altura=float(input('Cual es la altura del rectangulo: '))

    perimetro=base*2+altura*2
    base=base*altura

    print(f'El perimetro es {perimetro} y la base es {base}.')
rectangulo()
