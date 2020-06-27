
libreta=[]
def menu():
    print('Menú de opciones:')
    print('1-Agregar contacto')
    print('2-Mostrar contactos')
    print('3-Borrar contacto')
    print('4-Salir')
    resp=input('que desea hacer?')
    resp=int(resp)
    return resp


def AGREGAR(name,phone,mail):
    contacto={
        'nombre':name,
        'telefono':phone,
        'email':mail
    }
    libreta.append(contacto)
def IMPRIMIR():
    c=1
    for persona in libreta:
            print(f'{c}'+'| '+persona.get('nombre')
            ,persona.get('telefono')
            ,persona.get('email')+' |')
            c=c+1
m=menu()

while m !=4:    
    if m==1:
        nombre=input('nombre:')
        tel=input('telefono:')
        email=input('email:')
        AGREGAR(nombre,tel,email)
    elif m==2:
        IMPRIMIR()
    elif m==3:
        IMPRIMIR()
        borrar=input('a quien quieres eliminar?')
        borrar=int(borrar)
        libreta.pop(borrar-1)
    else:
        print('opción invalida'   )
    m=menu()





#def main():

#if __name_=="__main__":
#        main()

#print('------------')
#print(f'directorio contiene {len(contactos)}')
#print(contactos)

#for persona in contactos:
 #   print('| '+persona.get('nombre')
  #  ,persona.get('telefono')
   # ,persona.get('email')+' |')