import json


def get_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = {}

    return usuarios


def ingreso_usuario(nombre_de_usuario, clave):
    usuarios = get_usuarios()
    usuarios[nombre_de_usuario] = clave

    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)


def nuevo_usuario():
    usuarios = get_usuarios()
    nombre_de_usuario = input("Ingrese su usuario: ")

    if nombre_de_usuario in usuarios:
        print("El usuario ingresado ya se encuentra en la base de datos.")
    else:
        clave = input("Ingrese su clave: ")
        ingreso_usuario(nombre_de_usuario, clave)
        print("Usuario registrado con éxito.")


while True:
    print("\n1. Ingresa tu Usuario")

    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nuevo_usuario()
    elif opcion == "2":
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")        


nuevo_usuario()
