def validar_nombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    if len(nombre) < 3:
        raise ValueError("El nombre debe tener mínimo 3 caracteres")

    return True


def validar_edad(edad):
    if not edad.isdigit():
        raise ValueError("La edad debe ser numérica")

    edad = int(edad)

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    if edad < 18:
        raise ValueError("El usuario debe ser mayor de edad")

    return True