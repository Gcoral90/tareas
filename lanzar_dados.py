'''
PROGRAMA QUE SIMULA EL LANZAMIENTO DE UN DADO 
Y TE ENTREGA EL RESULTADO EN UN STRING'''
import random

def lanzar_dados():
    resultado=random.randint(1,6)
    return resultado

print(lanzar_dados())
print(type(lanzar_dados()))
def mostrar_menu():
    print('\t 1-.lanzar datos')
    print('\t 2-.Salir)
    opcion=int(input('\n'))
    return opcion

if opcion==1:
    lanzar_dados()
elif opcion==2:
    print('opcion invalida')





