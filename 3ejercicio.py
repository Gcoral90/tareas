lista_usuarios = []
usuario_uno = {
    'nombre': 'Galileo',
    'descuento': '5%',
    'curso': 'Python 3'
}
usuario_dos = {
    'nombre': 'Mike',
    'descuento': '15%',
    'curso': 'Analisis de datos con python'
}
lista_usuarios.append(usuario_uno)
lista_usuarios.append(usuario_dos)


for usuario in lista_usuarios:
    nombre=usuario.get('nombre')
    curso=usuario.get('curso')
    plantilla_email = f'Hola {nombre}\n bienvenido al curso de {curso}'
    print(plantilla_email)