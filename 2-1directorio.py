contactos=[]
while len(contactos) <1:
    print('AGREGA CONTACTO')
    nombre=input('nombre:')
    tel=input('telefono:')
    email=input('email:')
    contacto={
        'nombre':nombre,
        'telefono':tel,
        'email':email
    }
    contactos.append(contacto)
    print(f'nuestro directorio tiene {len(contactos)}')

print('------------')
#print(f'directorio contiene {len(contactos)}')
#print(contactos)

for persona in contactos:
    print('| '+persona.get('nombre')
    ,persona.get('telefono')
    ,persona.get('email')+' |')

