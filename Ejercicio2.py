nombre = input('¿Cómo te llamas?: ')
lista_temps = []

nombre = {}

km = str(input('Indica el punto kilométrico que has alcanzado: '))
tiempo = str(input('¿A qué hora has alcanzado los {} km?: '.format(km)))

nombre[tiempo] = km
lista_temps.append(tiempo)

pregunta = input('¿Has acabado la carrera? Responde SI o NO: ')
pregunta = pregunta.upper()

while pregunta == 'NO':
    km = input('Indica el punto kilométrico que has alcanzado: ')
    tiempo = input('¿A qué hora has alcanzado los {} km?: '.format(km))

    nombre[tiempo] = km

    pregunta = input('¿Has acabado la carrera? Responde SI o NO: ')
    pregunta = pregunta.upper()

    if pregunta == 'SI':
        break

for i in nombre:
    print('El corredor a las {} estaba en el km {}'.format(i, nombre[i]))
