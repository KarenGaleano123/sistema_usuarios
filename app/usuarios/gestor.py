from app.usuarios.validaciones import validar_nombre, validar_edad

usuarios = []


def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre: ")
        validar_nombre(nombre)

        edad = input("Ingrese la edad: ")
        validar_edad(edad)

        usuario = {
            "nombre": nombre,
            "edad": int(edad)
        }

        usuarios.append(usuario)

        print("\n Usuario registrado correctamente")

    except ValueError as error:
        print(f"\n Error: {error}")


def listar_usuarios():
    if not usuarios:
        print("\n No hay usuarios registrados")
        return

    print("\n LISTA DE USUARIOS")

    for index, usuario in enumerate(usuarios, start=1):
        print(f"{index}. {usuario['nombre']} - {usuario['edad']} años")


def buscar_usuario():
    nombre_busqueda = input("\nIngrese el nombre a buscar: ")

    encontrados = [
        usuario for usuario in usuarios
        if usuario["nombre"].lower() == nombre_busqueda.lower()
    ]

    if encontrados:
        print("\n Usuario encontrado:")
        for usuario in encontrados:
            print(f"- {usuario['nombre']} ({usuario['edad']} años)")
    else:
        print("\n Usuario no encontrado")