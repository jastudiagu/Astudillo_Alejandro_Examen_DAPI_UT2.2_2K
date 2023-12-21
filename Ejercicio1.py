nombre_fichero = input('Escribe el nombre de la lista: ')


def LeerDocumento(nombre_fichero):

    """ Función que lee un fichero y devuelve  una lista donde
        cada dato es una línea del fichero.

    Parámetros:
        - nombre_fichero: El nombre del fichero a leer.

    Salida:
            Lista con los datos del fichero.
    
    """

    with open(nombre_fichero, 'r') as fichero:
        lista_lineas = fichero.readlines()

    return lista_lineas


LeerDocumento(nombre_fichero)

def IdentificarPagado(lista):

    """ Función que crea un fichero con todas las líneas del documento
        en las que pone PAGADO
    
    Parámetros:

        - lista: Nombre de la lista recibida
    """

    lista = LeerDocumento(nombre_fichero)
    fichero = open('PAGADO.txt', 'w')

    for i in lista:
        if i[26:32] == 'PAGADO':
            fichero.write(i)
    fichero.close()

IdentificarPagado(LeerDocumento(nombre_fichero))







