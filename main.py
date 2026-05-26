from app.usuarios.gestor import (
    registrar_usuario,
    listar_usuarios,
    buscar_usuario
)

from app.config.settings import (
    APP_NAME,
    APP_VERSION,
    ADMIN_USER
)


def mostrar_menu():
    print("\n" + "=" * 40)
    print(f"{APP_NAME} - Versión {APP_VERSION}")
    print(f"Administrador: {ADMIN_USER}")
    print("=" * 40)

    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")


def main():

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            print("\n Cerrando sistema...")
            break

        else:
            print("\n Opción inválida")


if __name__ == "__main__":
    main()