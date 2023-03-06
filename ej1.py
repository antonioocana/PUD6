nombre = input("introduce tu nombre: ")
valor = 8
# comentario 1 linea

'''
    Comentario lo que sea
'''
def hola(nombre_recibido):
    if valor < 4:
        print("Hola")
    elif valor > 4 and valor < 9:
        print("Adios")
    else:
        print("Buenos dias")
    print("Hola mundo " + nombre_recibido)
    return 1

hola(nombre)