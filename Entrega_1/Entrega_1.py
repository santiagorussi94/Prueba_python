import json


def ingreso_usuario(nombre_de_usuario, clave):
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = {}

    usuarios[nombre_de_usuario] = clave

    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)


def nuevo_usuario():
    nombre_de_usuario = input("Ingrese su usuario: ")

    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = {}

    if nombre_de_usuario in usuarios:
        print("El usuario ingresado ya se encuentra en la base de datos.")
    else:
        clave = input("Ingrese su clave: ")
        ingreso_usuario(nombre_de_usuario, clave)
        print("Usuario registrado con éxito.")


nuevo_usuario()

# menu = input (print("Menu:\n 1-Nuevo Usuario \n 2-Verificar usuario \n 3-Salir"))
# if menu == 1
#     nuevo_usurio()
#     else