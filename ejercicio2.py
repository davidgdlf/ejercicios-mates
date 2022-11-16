
def media():
    hitoindividual=float(input('dime tu nota individual '))
    notahito=hitoindividual*0.3
    print(notahito)

    hitogrupal=float(input('dime tu nota grupal '))
    notahito2=hitogrupal*0.2
    print(notahito2)

    examen=float(input('dime tu nota del examen '))
    notaexamen=examen*0.5
    print(notaexamen)

    notafinal=notahito + notahito2 + notaexamen
    print(notafinal)

media()




