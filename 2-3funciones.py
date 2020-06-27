def saludar(nombre):
    if len(nombre)<5:
        print(f'hola {nombre}')
    else:
        print(f'que onda {nombre}')

personas=['juan','pedrito','fulanito']

for p in personas:
    saludar(p)




